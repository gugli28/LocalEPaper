import pip
import os
def install(package):
    pip.main(['install', package])

# Example
# if __name__ == '__main__':
#     install('argh')

def check_lib():
	try:
		import urllib3
	except Exception as e:
		print "+++++++++++ NO urllib3 ++++++++++++++++", e
	else:
		try:
			install('urllib3')
		except Exception as e:
			print "==============cant install urllib3 ================="
		

	try:
		from PyPDF2 import PdfFileMerger
	except Exception as e:
		print "+++++++++++ NO PyPDF2 ++++++++++++++++",e
	else:
		try:
			install('PyPDF2')
		except Exception as e:
			print "==============cant install PyPDF2 ================="
		
	try:
		import datetime
	except Exception as e:
		print "+++++++++++ NO datetime ++++++++++++++++",e
	else:
		try:
			install('datetime')
		except Exception as e:
			print "==============cant install datetime ================="
		
	try:
		from bs4 import BeautifulSoup
	except Exception as e:
		print "+++++++++++ NO bs4 ++++++++++++++++",e
	else:
		try:
			install('bs4')
		except Exception as e:
			print "==============cant install datetime ================="


	# os.system('ls')

	print " =================================================================== "

	
# try:
# 	pass
# except Exception as e:
# 	raise e
# finally:
# 	pass

