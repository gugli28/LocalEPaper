#!/usr/bin/env python
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import urllib2
import wget
import os
import download
import pdf_merger
import Cur_date
import Delete_Files
import get_pages
import checkFileSize


import send_email
import configg
import datetime
##Cron job 
import checkCronJob

import TorFirefox
import PdfCompressor




pdf_docs_del = [] # this will store the file_path of the files to be deleted
pdf_docs_merge = [] ## this will store the file_path of the files to be merged and then deleted


## this is use webdriver without display. We will start and close it when needed
display = Display(visible=0, size=(1024, 768))
def main():
	Hindustan()


def Hindustan():
	status = checkCronJob.checkCronStatus("/home/gugli/Documents/script_py/Dainik_Jagron/checkCronStatusH.txt")
	# print status

	if(status == 0):
		print "[[[[[[==Hindustans' JOB's already done==]]]]]]"
		return
	print "==================HINDUSTAN====================="
	### used ctrl+u to get the javascript of the webpage
	#===================================================================
	TorFirefox.startDisplay(display)
	browser = TorFirefox.getFirefoxBrowser()
	url = 'http://pdfcompressor.com/'
	browser.get(url)
	#===================================================================
	dir_path = os.path.dirname(os.path.realpath(__file__))
	todaysDate = Cur_date.strfTime()

	totalPages = get_pages.getPagesHindustan()
	print type(totalPages), totalPages

	# totalPages = 20
	for pageno in xrange(1,totalPages+1):

	# for pageno in xrange(1,5):

		url = "http://epaper.livehindustan.com/epaper/Bihar/Sitamarhi/"+todaysDate+"/108/Page-"+ str(pageno)+".html"
		# url = "http://epaper.livehindustan.com/epaper/Bihar/Sitamarhi/2018-05-04/108/Page-"+ str(pageno)+".html"
		print url
		html_page = urllib2.urlopen(url)
			
		soup = BeautifulSoup(html_page,"html.parser")
		try:
			src = soup.find('img',{'id':'imgpage_'+str(pageno)})['src'].replace('ll.jpg', '.pdf').replace('s.png', '.pdf').replace('.jpg', '.pdf');
			
		except Exception as e:
			print e
			print "+++++++++++++++++++IMG tag with id imgpage not found +++++++++++++++++++++"
			continue

		# print src
		### they have removed below junk part .. well its good but I had to change the code
		# pdf_url = src.replace("../../../../..","http://epaper.livehindustan.com")
		pdf_url = "http://epaper.livehindustan.com"+ src
		print pdf_url
		#this filepath is uploaded on the Compression website
		file_path_del = dir_path + "/h" + str(pageno)+".pdf"
		#this variable stores the file name of the compressed file yet to be downloaded
		file_path_merge = dir_path + "/h" + str(pageno)+ "-min" +".pdf" 
		print "Downloading...page no = ", pageno
		flag = download.download_file2(pdf_url,file_path_del, browser)

		## check valid pdf
		if(flag == 0):
			pdf_docs_del.append(file_path_del)

			pdf_docs_merge.append(file_path_merge) 
		else:
			# os.remove(file_path)
			print "-------------PAGE NO ",pageno, "DONT EXIST ----------------------------"
			continue

	##Downloading all compressed file in zip format 
	

	flag1 = PdfCompressor.downloadCompPDF(browser)
	## and unzipping it in the current folder
	# print os.getcwd()
	if(flag1): #flag1 =0 when there is no fle to be downloaded
		TorFirefox.unzipFile(os.getcwd()+"/pdfcompressor.zip",os.getcwd())
		os.remove(os.getcwd()+"/pdfcompressor.zip")

	## Merging all the individual files
	final_file_path = dir_path + "/h" + todaysDate+".pdf"
	# print pdf_docs_merge
	# print final_file_path
	pdf_merger.FileMerger(pdf_docs_merge, final_file_path)


	#close the browser and display after doint all the shit
	TorFirefox.closeBrowser(browser)
	TorFirefox.closeDisplay(display)
	##==========================================================================================
	##we will now check if the file size is under limit or not ( < 25 MB for attachment in gmail)
	checkSizeFlag = checkFileSize.check(final_file_path)
	k = 1

	while checkSizeFlag: # true is returned if size>25
		os.remove(final_file_path) # have to remove becoz pdf_merger only merges if the file dont exist

		pdf_merger.FileMerger(pdf_docs_merge[:-k], final_file_path)
		checkSizeFlag = checkFileSize.check(final_file_path)
		print "++++++++++ Removed last %s" %(k),'file +++++++++++++'
		k = k + 1 

	##==========================================================================================

	##==========================================================================================
	## now we are ready to send email
	##Hindi text 
	akhbaar = u'\u0905'  + u'\u0916' +  u'\u093c'+ u'\u092c' + u'\u093e' + u'\u0930'
	dinakit =  u'\u0926' + u'\u093f'  +  u'\u0928'+ u'\u093e' + u'\u0902' + u'\u0915' + u'\u093f'  + u'\u0924'
	# print akhbaar +' ' +dinakit

	subject = "Hindustan "+ akhbaar +' ' +dinakit+' ' + todaysDate

	try:
		## done in case when the more than one scripts run simultaneously. 
		##this can happen when network is slow or the script 1 is taking long enough time to execute
		print "Checking if mail is already sent ..... "
		status = checkCronJob.checkCronStatus("/home/gugli/Documents/script_py/Dainik_Jagron/checkCronStatusH.txt")
		print status
		if(status == 0):
			print "Mail has been sent already..."
			return
		print "SENDING EMAIL..............."
		send_email.send_mail(configg.fromaddr,configg.password,configg.toaddr,subject,todaysDate+".pdf",final_file_path)

		pdf_docs_merge.append(final_file_path)
		Delete_Files.del_files(pdf_docs_merge)
		Delete_Files.del_files(pdf_docs_del)
		print "FILES DELETED"
		##updating cron Flag file when the job is done for the day

		with open('/home/gugli/Documents/script_py/Dainik_Jagron/checkCronStatusH.txt','w') as outFile:
			outFile.write( Cur_date.strfTime())

		
	except Exception as e:
		# Delete_Files.del_files(pdf_docs)
		print "COULDNOT SEND MAIL...."
		print e



if __name__ == "__main__":
    main()
# <img alt="Image" border="0" class="map" id="imgpage" onclick="javascript:hidescrolldiv();" src="../../../../../epaperimages/17042018/17mz_stm06_muz_sitacity5ll.jpg" usemap="#Mapll"/>
# [Finished in 3.0s]