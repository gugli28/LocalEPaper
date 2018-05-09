'''
getFirefoxBrowser():
	This file creates the object for Firefox webdriver with Tor settings.
	It also set the downloading preferences and blocks the window pop-up that is shown in firefox after file is downloaded

unzipFile(filepath,destination_folder):
	Unzips file nly after the it is confirmed that file s completely downloaded
	
	checkDownStatus.txt:
		this file is updated by the file `watchdogg.py` after the zip file is completely downloaded
'''

from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display

import os
import time

import multiprocessing
import watchdogg

def main():
	print os.getcwd()
	# unzipFile("/home/gugli/Documents/script_py/Dainik_Jagron/pdfcompressor.zip","/home/gugli/Documents/script_py/Dainik_Jagron")
	b = getFirefoxBrowser()
	time.sleep(20)
	b.close()

def getFirefoxBrowser():
	print "===== getFirefoxBrowser"
	profile=webdriver.FirefoxProfile()
	profile.set_preference('network.proxy.type', 1)
	profile.set_preference('network.proxy.socks', '127.0.0.1')
	profile.set_preference('network.proxy.socks_port', 9150)


	profile.set_preference("browser.download.folderList", 2) # 0 means to download to the desktop, 1 means to download to the default "Downloads" directory, 2 means to use the directory 
	# profile.set_preference("browser.helperApps.alwaysAsk.force", False) 
	# profile.set_preference("browser.download.manager.showWhenStarting",False) 
	# profile.set_preference("browser.download.dir", "/home/gugli/Downloads") 

	# profile.set_preference('browser.download.folderList', 2)
	# profile.set_preference('browser.download.folderList', 2)
	profile.set_preference('browser.download.manager.showWhenStarting', False)
	profile.set_preference('browser.download.dir', os.getcwd())
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/xml,text/plain,text/xml,image/jpeg,text/eml,application/zip");        

	print "======profile set===="
	'''
	options = Options()
	options.add_argument( "--headless" )
	# options.add_argument( "--screenshot test.jpg http://google.com/" )
	# driver = webdriver.Firefox( firefox_options=options )


	browser=webdriver.Firefox(firefox_profile=profile,firefox_options=options)
	'''

	
	# display.start()
	browser=webdriver.Firefox(profile)
	return browser
	# return browser,display
	# browser.get("http://yahoo.com")
	# browser.save_screenshot("screenshot.png")
	# browser.close()


def unzipFile(filepath,destination_folder):
	startWatchdog()
	print "===== unzipFile"
	cmd = "unzip " + filepath + " -d " +  destination_folder

	# cmd = "jar xvf" + filepath
	# filestatus = os.path.isfile(filepath)
	# while( os.path.isfile(filepath) == 0) :
	# 	time.sleep(5)
	# 	print "=======File not present, already slept 5 sec since I last checked;======="
	# 	continue
	'''
		while not os.path.exists(filepath):
			print "     ----sleeping----"
			time.sleep(10)
	'''
	### read checkDownStatus for for the status of the file
	fileObject = open(os.getcwd()+"/checkDownStatus.txt" ,"r")
	status = fileObject.read()

	print status

	while( status != "DONE"):
		fileObject = open(os.getcwd()+"/checkDownStatus.txt" ,"r")
		status = fileObject.read()
		print "     ----sleeping----" , status, status != "DONE"
		time.sleep(5)

	## this check isn't necessary now
	if os.path.isfile(filepath):
		os.system(cmd)
	else:
		raise ValueError("%s isn't a file!" % filepath)

	fileObject.close()

	
	# try:
	# 	with io.FileIO(filepath, "r+") as fileObj:

	# 	'''
	# 	Deal with case where FTP client uses extensions such as ".part" and '.filepart" for part of the incomplete downloaded file.
	# 	To do this, make sure file exists before adding it to list of completedFiles.
	# 	'''
	# 	if(os.path.isfile(fileName)):
	# 		completedFiles.append(fileName)
	# 	print "File=" + file_path + " has completely loaded."
	# except IOError as ioe:
	# 	print str(ioe)
	
	# while(1):
	# 	try:
	# 		os.system(cmd)
	# 		print "++++++++++++++++++++"
	# 		break
	# 	except Exception as e:
	# 		time.sleep(5)
	# 		print "=======File not present, already slept 5 sec since I last checked;======="
	# 		continue


def closeBrowser(browser):
	browser.close()
	
	print "=======Browser Closed===="

def closeDisplay(display):
	display.stop()
	print "=======Display Closed===="

def startDisplay(display):
	display.start()
	print "======= Invisible Display Started [visible=0, size=(1024, 768)]===="

	
def watchdog():
	### running daemon that checks if the file is downoaded completely or not
	w = watchdogg.Watcher()
	w.run()

def startWatchdog():
	'''
	### below updation is necessary in order to open watchdog
	coz after the last step is done (prev run) the file is updated to "DONE"
	and this same string is also required to close watchdog after all unzipping is done
	'''
	with open(os.getcwd()+"/checkDownStatus.txt",'w') as outFile:
			outFile.write("blah")



	p1 = multiprocessing.Process(name='p1', target=watchdog)
	p1.start()
	# p2 = multiprocessing.Process(name='p', target=sud)
	# p2.start()


if __name__ == "__main__":
    main()