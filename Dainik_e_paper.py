import import_lib
import_lib.check_lib()


import download
import pdf_merger
import Cur_date
import os
import Delete_Files
import get_pages
import checkFileSize

import send_email
import configg
import datetime
##Cron job 
import checkCronJob


def main():
	now = datetime.datetime.now()
	print "* Time of RUN : ",now
	if (datetime.datetime.today().hour < 12):
		print "This script is scheduled to run only after 1200hrs; "
		print "change it in the code if you want otherwise"
		print "------------------------SLEEP TIME-------------------------------"
		return

	hack_paper()


def hack_paper():
	
	status = checkCronJob.checkCronStatus()
	# print status

	if(status == 0):
		print "JOB's already done"
		return


	todaysDate = Cur_date.getCurDate()

	pdf_docs = []
	pages = get_pages.getPages()+1

	# pages = 2

	dir_path = os.path.dirname(os.path.realpath(__file__))

	for pageno in xrange(1,pages):
		
		
		for city in ['smt','mdb','bgh']:
			url = "http://epaper.jagran.com/epaperimages/"+todaysDate+"/muzaffarpur/"+str(Cur_date.getPrevDayDate())+city+"-pg"+ str(pageno) +"-0.pdf"
			# url = "http://epaper.jagran.com/epaperimages/"+"26012018"+"/muzaffarpur/"+"25"+city+"-pg"+ str(pageno) +"-0.pdf"

			print url

			##sending file path
			## file path also contains the file name of the downloaded file
			file_path = dir_path + "/" + str(pageno)+".pdf"
			print "Downloading...page no = ", pageno

			## this fn ret value that ensures if we have got valid pdf, if not loop continues
			flag = download.download_file(url,file_path)

			
			# flag = pdf_merger.check_valid_pdf(file_path)

			if(flag == 0):
				pdf_docs.append(file_path)
				break #As soon as it gets a valid pdf add to the list 'pdf_docs' else skip
			else:
				# os.remove(file_path)
				print "PAGE NO",pageno,"with city =", city, "DONT EXIST"
				continue
			
		


	# print pdf_docs
	final_file_path = dir_path + "/" + todaysDate+".pdf"
	pdf_merger.FileMerger(pdf_docs, final_file_path)

	## if the compression dont compress to the required size than the last option is to eliminate some files;
	checkSizeFlag = checkFileSize.check(final_file_path)
	k = 1

	while checkSizeFlag:
		os.remove(final_file_path) # have to remove becoz pdf_merger only merges if th ethe file dont exist

		pdf_merger.FileMerger(pdf_docs[:-k], final_file_path)
		checkSizeFlag = checkFileSize.check(final_file_path)
		print "++++++++++ Removed last %s" %(k),'file +++++++++++++'
		k = k + 1 
	##=======================================================================================================

	##Hindi text 
	akhbaar = u'\u0905'  + u'\u0916' +  u'\u093c'+ u'\u092c' + u'\u093e' + u'\u0930'
	dinakit =  u'\u0926' + u'\u093f'  +  u'\u0928'+ u'\u093e' + u'\u0902' + u'\u0915' + u'\u093f'  + u'\u0924'
	# print akhbaar +' ' +dinakit

	subject = akhbaar +' ' +dinakit+' ' + todaysDate

	# file_path = dir_path + "/" + final_file_name

	###for qpython -- files download in this directory
	# cd_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	# file_path = cd_dir_path + "/" + final_file_name

	try:
		## done in case when the more than one scripts run simultaneously. 
		##this can happen when network is slow or the script 1 is taking long enough time to execute
		print "Checking if mail is already sent ..... "
		status = checkCronJob.checkCronStatus()
		print status
		if(status == 0):
			print "Mail has been sent already..."
			return
		print "SENDING EMAIL..............."
		send_email.send_mail(configg.fromaddr,configg.password,configg.toaddr,subject,todaysDate+".pdf",final_file_path)

		pdf_docs.append(final_file_path)
		Delete_Files.del_files(pdf_docs)

		##updating cron Flag file when the job is done for the day

		with open('/home/gugli/Documents/script_py/Dainik_Jagron/checkCronStatus.txt','w') as outFile:
			outFile.write( Cur_date.strfTime())

		
	except Exception as e:
		Delete_Files.del_files(pdf_docs)
		print "COULDNOT SEND MAIL...."
		print e


if __name__ == "__main__":
    main()