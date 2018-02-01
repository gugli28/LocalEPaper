import datetime
# from datetime import datetime, 

# getting current date and time
'''
d = datetime.datetime.today()
print('Current date and time: ', d)
 
# getting current year
print('Current year: ', d.year)
 
#getting current month
print('Current month: ', d.month)
 
#getting current day
print('Current day: ', d.day)
 
# getting current hour
print('Current hour: ', d.hour)
 
# getting current minutes
print('Current minutes: ', d.minute)
 
# getting current Seconds
print('Current seconds: ', d.second)
 
# getting current microsecond
print('Current micro seconds: ', d.microsecond)

'''
def main():
	date = getCurDate()
	print "DATE=====" , date
	print getAbbMon()
	getPrevDayDate()


def getPrevDayDate():
	yesterday = datetime.datetime.today() - datetime.timedelta(days = 1)
	# yesterday.strftime('%m%d%y')

	# print "YESTER = ",yesterday.day

	return yesterday.day

def getDay():
	d = datetime.datetime.today()
	day = d.day
	day = str(0)+str(day) if day<10 else str(day)
	return day
	

def getAbbMon():
	d = datetime.datetime.now()
	mon = d.strftime("%b")
	return mon.lower()

def getCurDate():
	d = datetime.datetime.today()
	year = d.year
	month = d.month
	month = str(0)+str(month) if month<10 else str(month)
	day = d.day
	day = str(0)+str(day) if day<10 else str(day)

	date = (day)+(month)+str(year)

	return date

if __name__ == "__main__":
    main()