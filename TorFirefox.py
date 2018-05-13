'''

getFirefoxBrowser():
	This file creates the object for Firefox webdriver with Tor settings.
	It also set the downloading preferences and blocks the window pop-up that is shown in firefox after file is downloaded


https://medium.com/@mr_rigden/using-tor-with-the-python-request-library-79015b2606cb
https://github.com/c0r3dump3d/checktor/blob/master/checktor.py

check how to locate in selenium python
http://selenium-python.readthedocs.io/locating-elements.html
'''
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display

import os
import time


def main():
	print os.getcwd()
	# unzipFile("/home/gugli/Documents/script_py/Dainik_Jagron/pdfcompressor.zip","/home/gugli/Documents/script_py/Dainik_Jagron")
	b = getFirefoxBrowser()
	time.sleep(10)
	b.get('http://pdfcompressor.com/')
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
	browser=webdriver.Firefox(firefox_profile=profile,executable_path=os.getcwd()+'/geckodriver')
	print "[################ IP === %s #################]"%(getIP(browser))
	return browser
	# return browser,display
	# browser.get("http://yahoo.com")
	# browser.save_screenshot("screenshot.png")
	# browser.close()



def closeBrowser(browser):
	browser.close()
	
	print "=======Browser Closed===="

def closeDisplay(display):
	display.stop()
	print "=======Display Closed===="

def startDisplay(display):
	display.start()
	print "======= Invisible Display Started [visible=0, size=(1024, 768)]===="

def getIP(browser):
	r = browser.get('http://httpbin.org/ip')
	# element = browser.find_element_by_tag_name('body')
	page_src = browser.page_source
	soup = BeautifulSoup(page_src,"html.parser")
	json = soup.find('div',{'id':'json'})
	print json.text.strip()
	# print r
	# print r.text
	# print element.text
	return json.text.strip()

if __name__ == "__main__":
    main()