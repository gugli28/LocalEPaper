from crontab import CronTab

# https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231

# cron gyan
# https://serverfault.com/questions/449651/why-is-my-crontab-not-working-and-how-can-i-troubleshoot-it
# http://kvz.io/blog/2007/07/29/schedule-tasks-on-linux-using-crontab/

my_cron = CronTab(user='gugli')
def main():
	# remove_chron()
	# add_chron('cd /home/gugli/Documents/script_py/Dainik_Jagron && /usr/bin/python /home/gugli/Documents/script_py/Dainik_Jagron/Dainik_e_paper.py','e-dainik')
	# add_chron('cd /home/gugli/Documents/script_py/Dainik_Jagron && /usr/bin/python /home/gugli/Documents/script_py/Dainik_Jagron/writeDate.py', 'dateinfo')
	add_chron('"/home/gugli/Downloads/tor-browser_en-US/Browser/start-tor-browser" --detach','TOR')
def remove_chron():
	for job in my_cron:
		my_cron.remove(job)
		my_cron.write()

def add_chron(cmd,com):
	job = my_cron.new(command= cmd, comment= com )
	#wrinting cron job to cron tab
	my_cron.write()

	#scheduling the job
	# job.minute.every(1) 
	job.day.every(1) 

	## MANUALLY UPDATED crontab (`crontab -e`) the frequecy * */2 * * * [ at interval of 2 hrs atarting from 0000]

	## */10 * * * * cd /home/gugli/Documents/script_py/Dainik_Jagron && /usr/bin/python /home/gugli/Documents/script_py/Dainik_Jagron/Dainik_e_paper.py >>/home/gugli/Documents/script_py/Dainik_Jagron/logfile.tx$

	## 0,10,20,30,40,50 */1 * * * cd /home/gugli/Documents/script_py/Dainik_Jagron && /usr/bin/python /home/gugli/Documents/script_py/Dainik_Jagron/Dainik_e_paper.py >>/home/gugli/Documents/script_py/Dainik_Jag$

	##check og of scheduled jobs
	## vi /var/log/syslog

if __name__ == "__main__":
    main()
