from PyPDF2 import PdfFileMerger
import os
merger = PdfFileMerger()



def main():
	pdfs = ['1.pdf', '2.pdf']
	FileMerger(pdfs, "/home/gugli/Documents/script_py/Dainik_Jagron/01.pdf")

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
	filestatus = os.path.isfile(file_path)
	if filestatus :
		print "file already MERGED :)))))))))))"
		return
		
	for pdf in pdfs:
		merger.append(pdf)
	merger.write(file_path)

	print "CONGRATS !!!! PDF MERGED !!!!"
	


if __name__ == "__main__":
    main()