#!/usr/bin/python
import os
 
## get input ##
# filename=raw_input("Type file name to remove: ")
 
## delete only if file exists ##

def del_files(pdfs):
	for pdf in pdfs:
		if os.path.exists(pdf):
			os.remove(pdf)
		else:
			print("Sorry, I can not remove %s file." % pdf)

	print "FILES DELETED"