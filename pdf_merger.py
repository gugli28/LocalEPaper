from PyPDF2 import PdfFileMerger
import os
# merger = PdfFileMerger()
import checkFileSize


def main():
	# pdfs = ['1.pdf', '2.pdf']
	k = 1

	# while checkSizeFlag:
	# 	os.remove(final_file_path) # have to remove becoz pdf_merger only merges if th ethe file dont exist
	# 	pdf_docs1 = pdf_docs[:-k]
	# 	print pdf_docs1
	# 	pdf_merger.FileMerger(pdf_docs1, final_file_path)
	# 	checkSizeFlag = checkFileSize.check(final_file_path)
	# 	print "++++++++++ Removed last %s" %(k),'file +++++++++++++'
	# 	k = k + 1 
	pdfs = ['/home/gugli/Documents/script_py/Dainik_Jagron/1.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/2.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/3.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/4.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/5.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/6.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/7.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/8.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/9.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/10.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/11.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/12.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/13.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/14.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/15.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/16.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/17.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/18.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/19.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/20.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/21.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/22.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/23.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/24.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/25.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/26.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/27.pdf', '/home/gugli/Documents/script_py/Dainik_Jagron/28.pdf']
	
	final_file_path = "/home/gugli/Documents/script_py/Dainik_Jagron/01aaaa.pdf"

	FileMerger(pdfs, final_file_path)
	checkSizeFlag = checkFileSize.check(final_file_path)

	while checkSizeFlag:
		os.remove(final_file_path)
		FileMerger(pdfs[:-k], final_file_path)
		checkSizeFlag = checkFileSize.check(final_file_path)
		k = k+1
		print checkSizeFlag
	print check_valid_pdf('1.pdf')


def check_valid_pdf(file_path):
	
	# dir_path = os.path.dirname(os.path.realpath(__file__))
	# file_path = dir_path +"/"+filename
	merger2 = PdfFileMerger()
	try:
		merger2.append(file_path)
	except Exception as e:
		print "========GOT ERROR WHILE APPENDING FILE==========", file_path
		print e
		return 1
	return 0	 
		
		
def FileMerger(pdfs, file_path):
	# dir_path = os.path.dirname(os.path.realpath(__file__))
	merger = PdfFileMerger()
	filestatus = os.path.isfile(file_path)
	if filestatus :
		print "[[[[[[[[[[[ file already MERGED :]]]]]]]]"
		return
		
	for pdf in pdfs:
		merger.append(pdf)
	merger.write(file_path)

	print "CONGRATS !!!! PDF MERGED !!!!"
	


if __name__ == "__main__":
    main()