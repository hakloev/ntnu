import os

def main():
	# lager fil på desktop
	os.system("touch ~/Desktop/ test.py")
	os.system("open -a TextEdit.app ~/.bash_profile")

main()
