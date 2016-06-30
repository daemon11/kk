import os

def run(**args):
	print "[*] Indirlister module"
	files = os.listdir(".")
	return str(files)


