 # Python code to illustrate Sending mail with attachments
# from your Gmail account 
 
# libraries to be imported
#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
  

import configg

def main():
    send_mail(configg.fromaddr,configg.password,configg.toaddr,"NewsPaper","text.txt","/home/gugli/Documents/script_py/Dainik_Jagron/text.txt")


def send_mail(fromaddr,password,toaddr,subject,file_name,file_path):
	# instance of MIMEMultipart
	msg = MIMEMultipart()
	 
	# storing the senders email address  
	msg['From'] = fromaddr
	 
	# storing the receivers email address 
	msg['To'] = toaddr
	 
	# storing the subject 
	msg['Subject'] = subject
	 
	# string to store the body of the mail
	body = "Please Find Attached NewsPaper"
	 
	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))
	 
	# # open the file to be sent 
	# filename = "File_name_with_extension"
	# attachment = open("Path of the file", "rb")

	filename = file_name
	attachment = open(file_path, "rb")

	 
	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')
	 
	# To change the payload into encoded form
	p.set_payload((attachment).read())
	 
	# encode into base64
	encoders.encode_base64(p)
	  
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	# attach the instance 'p' to instance 'msg'
	msg.attach(p)
	 
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	 
	# start TLS for security
	s.starttls()
	 
	# Authentication
	s.login(fromaddr, password)
	 
	# Converts the Multipart msg into a string
	text = msg.as_string()
	 
	# sending the mail
	# s.sendmail(fromaddr, toaddr, text)
	s.sendmail(msg['From'], msg["To"].split(","),text)
	 
	# terminating the session
	s.quit()

	print "EMAIL SENT -------------------------"

if __name__ == "__main__":
    main()


## sending multiple recepeint and also for the cc
# https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib