import urllib2
import os
import CompressFile
import pdf_merger

from tqdm import tqdm
import requests
import math


import PdfCompressor
def main():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/" + "doc.pdf"
    download_file("http://epaper.jagran.com/epaperimages/25032018/muzaffarpur/24smt-pg1-0.pdf",file_path)
   
    # download_file("https://drive.google.com/file/d/1EqS7SQMGCz-XE5_Th7Lp_VXHZiuI12Vg/view",'hindu28feb.pdf')
    # filestatus = os.path.isfile('2.pdf')
    # if filestatus :
    #     print "file already downloaded"

def download_file(download_url,file_path):
	## check if file already exists
	filestatus = os.path.isfile(file_path)
	if filestatus :
		print "(((((((((( file already downloaded :)))))))))))"
		return 0
	dir_path = os.path.dirname(os.path.realpath(__file__))
	dup_file_path = dir_path + "/" +"comp.pdf"

	## file written in duplicate file name that is later compressed and file name is changed to file_path
	'''
	response = urllib2.urlopen(download_url)
	file = open( dup_file_path , 'w')
	file.write(response.read())
	file.close()
	print("Completed")
	'''
	Download_with_progress(download_url, dup_file_path)

	### compress only valid pdf file
	flag = pdf_merger.check_valid_pdf(dup_file_path)
	if(flag == 0):
		print "Hurray got a valid Pdf.. Now we gonna compress it !! "
		CompressFile.compress( dup_file_path, file_path )
		os.remove(dup_file_path)

	print "FLAG = ", flag
	return flag


## this is  for hindustan paper
def download_file2(download_url,file_path, browser):
	## check if file already exists
	filestatus = os.path.isfile(file_path)
	if filestatus :
		# flag = pdf_merger.check_valid_pdf(file_path)
		# if (flag == 0):
		print "((((((((((= file already downloaded =)))))))))))"
		return 0
		##if file is present and corrupt then
		# os.remove(file_path) ##if the file was somehow bad format this will retry dowloading it again
		

	'''
	response = urllib2.urlopen(download_url)
	file = open( file_path , 'w')
	file.write(response.read())
	file.close()
	'''
	Download_with_progress(download_url, file_path)

	flag = pdf_merger.check_valid_pdf(file_path)
	if(flag == 0):
		print("valid pdf download Completed Now we will compress it")
		## Compressing file using Selenium TOR and the" http://pdfcompressor.com/" website
		PdfCompressor.compressPDF(browser, file_path)
		print " ||||||| pdf = ", file_path, "uploaded ||||||||||"
	else:
		if(os.path.isfile(file_path)):
			os.remove(file_path)
	return flag


## this function shows the progress of the downloading file	
def Download_with_progress(download_url, file_path):
	r = requests.get(download_url, stream=True)

	# Total size in bytes.
	total_size = int(r.headers.get('content-length', 0)); 
	block_size = 1024
	wrote = 0 
	with open(file_path, 'wb') as f:
	    for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
	        wrote = wrote  + len(data)
	        f.write(data)
	if total_size != 0 and wrote != total_size:
	    print("ERROR, something went wrong")  

            
            


if __name__ == "__main__":
    main()