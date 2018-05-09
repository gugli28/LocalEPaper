'''
compressPDF(browser, filepath):
	this function upload the file to the browser object.( the browseris theone that compreses it !)

downloadCompPDF(browser):
	After all the files are compressed it downloads the zip file.
	It first waits for the button to get enable before cicking
	Return 0 when there is no file to download.
'''

from selenium import webdriver
import os
import time

import TorFirefox

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


if __name__ == "__main__":
    main()