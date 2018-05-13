'''
compressPDF(browser, filepath):
	this function upload the file to the browser object.( the browseris theone that compreses it !)

downloadCompPDF(browser):
	After all the files are compressed it downloads the zip file.
	It first waits for the button to get enable before cicking
	Return 0 when there is no file to download.
unzipFile(filepath,destination_folder):
	Unzips file nly after the it is confirmed that file s completely downloaded
	
	checkDownStatus.txt:
		this file is updated by the file `watchdogg.py` after the zip file is completely downloaded

'''

from selenium import webdriver
import os
import time

import TorFirefox

import multiprocessing
import watchdogg



def main():
	browser = TorFirefox.getFirefoxBrowser()
	url = 'http://pdfcompressor.com/'
	browser.get(url)
	dir_path = os.path.dirname(os.path.realpath(__file__))
	file_path = dir_path + "/" + "2.pdf"
	print file_path
	compressPDF(browser, file_path)
	downloadCompPDF(browser)
	TorFirefox.unzipFile(os.getcwd()+"/pdfcompressor.zip",os.getcwd())
	reset_all(browser)
	time.sleep(5)
	browser.close()

def compressPDF(browser, filepath):

	# browser = sel_tor1.getFirefoxBrowser()
	# url = 'http://pdfcompressor.com/'
	# browser.get(url)

	# btn = browser.find_element_by_id('download-all')
	# print btn.get_attribute('disabled')
	print "======== compressPDF =========="

	element = browser.find_element_by_xpath("//input[@type='file']")
	element.send_keys(filepath)

	ul = browser.find_element_by_id('filelist')
	'''
	# https://stackoverflow.com/questions/24795198/get-all-child-elements
	all_children_by_xpath = ul.find_elements_by_xpath(".//*")
	print 'len(all_children_by_xpath): ' + str(len(all_children_by_xpath))
	'''

def downloadCompPDF(browser):

	# https://stackoverflow.com/questions/24795198/get-all-child-elements
	##check if there is file to be downloaded

	ul = browser.find_element_by_id('filelist')
	all_children_by_xpath = ul.find_elements_by_xpath(".//*")
	print 'len(all_children_by_xpath): ' + str(len(all_children_by_xpath))
	if (len(all_children_by_xpath) == 0):
		print "NO file to dowload... Exit"
		return 0

		
	#download compressed pdf in zip file
	print "======== DownloadCompPDF =========="
	btn = browser.find_element_by_id('download-all')

	i=1
	print btn.get_attribute('disabled')
	while( btn.get_attribute('disabled') ):  # this condition returns true when the btn is disabled
		time.sleep(5)
		print "trial no = ", i
		i = i + 1

	print btn.get_attribute('disabled') 
	print "Buttton is now clickable"
	browser.find_element_by_id('download-all').click()
	
	# print elem

	print browser 
	return 1



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



## PDFcompressor takes atmost 20 files 
def reset_all(browser):
	print "======== ResettingPDFCompressor =========="
	btn = browser.find_element_by_id('reset-all')
	btn.click()


if __name__ == "__main__":
    main()