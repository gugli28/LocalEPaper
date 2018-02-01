import os

import configg
import pip

os.system("python -m pip install bs4")

print  type(os.system('pwd'))

print type(os.path.join("data", "filenames[0]"))

# a = os.getcwd()

# print a + 'e'

dir_path = os.path.dirname(os.path.realpath(__file__))

print os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print dir_path+"/"+ "sa.pdf"
print os.path.abspath(__file__)
print "This is test file"