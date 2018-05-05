'''
this file checks the log in the file path and returns 1 when the date in the log file is not updated

'''

import datetime
import Cur_date

def main():
	checkCronStatus()


def checkCronStatus(filepath):
	fileObject = open(filepath ,"r")
	# data = fileObject.read()

	# status = data.split(" ") 
	 # status = checkCronJob.checkCronStatus().split(" ") 

	# str_date = status[0]
	str_date = fileObject.read()
	fileObject.close()
	# print str_date
	# flag = status[1]
	# li = status.split(" ")
	# print status

	# print "date = ",str_date ,"====", "flag = ", flag
	return checkDate(str_date)

'''
def checkCronStatusH():
	fileObject = open("/home/gugli/Documents/script_py/Dainik_Jagron/checkCronStatusH.txt" ,"r")
	
	str_date = fileObject.read()
	fileObject.close()
	return checkDate(str_date)
'''
def checkDate(str_date):
	logged_date = datetime.datetime.strptime(str_date, '%Y-%m-%d')

	# print "logged_date = ", logged_date
	str_today_date = datetime.datetime.strptime(Cur_date.strfTime(), '%Y-%m-%d')
	# print "str_today_date = ",str_today_date

	if( str_today_date > logged_date ):
		print "NOT SENT"
		return 1 ## the job is not done today.. YET . returns 1 so that further process is to be initiated
	else:
		# print "Logged date is same as todays date"
		return 0 ## return 0 coz job is already done today

if __name__ == "__main__":
    main()