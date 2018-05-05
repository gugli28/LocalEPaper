#!/usr/bin/env python
from bs4 import BeautifulSoup

import urllib2
#import urllib3
import Cur_date

# browser = webdriver.Firefox()


def main():
	getPages()


def getPages():
	print "GETTING PAGES.........."
	day = Cur_date.getDay()
	mon = Cur_date.getAbbMon()
	
	url = "http://epaper.jagran.com/epaper/"+str(day)+"-"+mon+"-2018-218-Sitamarhi-Page-1.html#"

	# url = "http://epaper.jagran.com/epaper/01-feb-2018-218-Sitamarhi-Page-1.html#"
	# url = "http://epaper.jagran.com/epaper/31-jan-2018-218-Sitamarhi-Page-1.html#"
	print url
	html_page = urllib2.urlopen(url)
	# http = urllib3.PoolManager()

	# html_page = http.request('GET', url)
	# soup = BeautifulSoup(html_page.data,'lxml')
	# soup = BeautifulSoup(html_page.data,"lxml")
	soup = BeautifulSoup(html_page,"html.parser")
	# print soup.prettify()

	select = soup.find('select',{'id':'Gotopage'})
	# print select.prettify()
	pages = select.find_all('option')

	print "NO of Pages == ",len(pages)
	print "   ===================================================     "
	return len(pages)

def getPagesHindustan():
	todaysDate = Cur_date.strfTime()
	url = "http://epaper.livehindustan.com/epaper/Bihar/Sitamarhi/"+todaysDate+"/108/Page-"+ str(1)+".html"
	# url = "http://epaper.livehindustan.com/epaper/Bihar/Sitamarhi/2018-05-03/108/Page-"+ str(1)+".html"
	print url
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page,"html.parser")
	totalPages = soup.find('input',{'id':'totalpages'})['value']

	return int(totalPages)
if __name__ == "__main__":
    main()