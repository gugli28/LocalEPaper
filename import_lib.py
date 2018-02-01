import pip
import os
def install(package):
    pip.main(['install', package])

# Example
# if __name__ == '__main__':
#     install('argh')

def check_lib():
	try:
		import urllib2
	except Exception as e:
		print "+++++++++++ NO urllib2 ++++++++++++++++", e
		# COPY THIS pip.main(['install', 'urllib2'])
		print "Execute === " , "pip.main(["+'install'+"," +'urllib2'+ "])"
	# else:
		# try:
		# 	install('urllib3')
		# except Exception as e:
		# 	print "==============cant install urllib3 ================="

	try:
		from PyPDF2 import PdfFileMerger
	except Exception as e:
		print "+++++++++++ NO PyPDF2 ++++++++++++++++",e
		# COPY THIS pip.main(['install', 'PyPDF2'])
		print "Execute === " , "pip.main(["+'install'+"," +'PyPDF2'+ "])"
	# else:
		# try:
		# 	install('PyPDF2')
		# except Exception as e:
		# 	print "==============cant install PyPDF2 ================="
	try:
		import datetime
	except Exception as e:
		print "+++++++++++ NO datetime ++++++++++++++++",e
	# else:
	# 	try:
	# 		install('datetime')
	# 	except Exception as e:
	# 		print "==============cant install datetime ================="
		
	try:
		from bs4 import BeautifulSoup
	except Exception as e:
		print "+++++++++++ NO bs4 ++++++++++++++++",e
		# COPY THIS pip.main(['install', 'bs4'])
		print "Execute === " , "pip.main(["+'install'+"," +'bs4'+ "])"
	# else:
		# try:
		# 	install('bs4')
		# except Exception as e:
		# 	print "==============cant install datetime ================="

	# os.system('ls')

	print " =============Above cmd in QPython================================ "

	
# try:
# 	pass
# except Exception as e:
# 	raise e
# finally:
# 	pass

