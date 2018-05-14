import os
import time
import checkCronJob
import Cur_date
from pyvirtualdisplay import Display
import TorFirefox

display = Display(visible=0, size=(1024, 768))
# os.system("cd /home/gugli/Downloads/tor-browser_en-US")

# print os.getcwd()

# cmd = sh -c '"/home/gugli/Downloads/tor-browser_en-US/Browser/start-tor-browser" --detach || ([ !  -x "/home/gugli/Downloads/tor-browser_en-US/Browser/start-tor-browser" ] && "$(dirname "$*")"/Browser/start-tor-browser --detach)' dummy %k
def main():
	torStatus = checkCronJob.checkCronStatus(os.getcwd()+"/checkTorStartStatus.txt")
	print torStatus
	if (torStatus):
		 start()
	else:
		print "Tor is already active"
	TorFirefox.startDisplay(display)
	browser = TorFirefox.getFirefoxBrowser()

	TorFirefox.closeBrowser(browser)
	TorFirefox.closeDisplay(display)


def start():
	display.start() ## this thread will be active and will be only termination after is closed
	os.system('"/home/gugli/Downloads/tor-browser_en-US/Browser/start-tor-browser" --detach')
	print "  $$$$$$$$$$$$$$$$$$ TOR started... $$$$$$$$$$$$$$$$$$$$$$"
	print "sleeping..."
	time.sleep(2)
	# display.stop()

	with open(os.getcwd()+"/checkTorStartStatus.txt",'w') as outFile:
			outFile.write( Cur_date.strfTime())
	#starting watchdog
	# print "starting watchdog"
	# cmd = " cd /home/gugli/Documents/script_py && /usr/bin/python /home/gugli/Documents/script_py/watchdogg.py >>/home/gugli/Documents/script_py/logfile.txt"
	# os.system(cmd)
	# * */1 * * * cd /home/gugli/Documents/script_py/Dainik_Jagron && /usr/bin/python /home/gugli/Documents/script_py/Dainik_Jagron/startTor.py >>/home/gugli/Documents/script_py/Dainik_Jagron/starttor.txt

	# print "   $$$$$$$$$$$$$$$$$$ watchdog started $$$$$$$$$$$$$$$$$$$$$$$$"


if __name__ == "__main__":
    main()