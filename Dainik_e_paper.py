import import_lib
import_lib.check_lib()


import download
import pdf_merger
import Cur_date
import os
import Delete_Files
import get_pages

import send_email
import configg


todaysDate = Cur_date.getCurDate()

pdf_docs = []
pages = get_pages.getPages()+1

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

		download.download_file(url,file_path)

		
		flag = pdf_merger.check_valid_pdf(file_path)
		if(flag == 0):
			pdf_docs.append(file_path)
			break #As soon as it gets a valid pdf add to the list 'pdf_docs' else skip
		else:
			os.remove(file_path)
			print "PAGE NO",pageno,"with city =", city, "DONT EXIST"
		
		
	# pdf_docs.append(file_path)



final_file_path = dir_path + "/" + todaysDate+".pdf"
pdf_merger.FileMerger(pdf_docs, final_file_path)


subject = "epaper dated "+ todaysDate

# file_path = dir_path + "/" + final_file_name

###for qpython -- files download in this directory
# cd_dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# file_path = cd_dir_path + "/" + final_file_name

try:
	print "SENDING EMAIL..............."
	send_email.send_mail(configg.fromaddr,configg.password,configg.toaddr,subject,todaysDate+".pdf",final_file_path)

	pdf_docs.append(final_file_path)
	Delete_Files.del_files(pdf_docs)
	
except Exception as e:
	Delete_Files.del_files(pdf_docs)
	print "COULDNOT SEND MAIL...."
	print e