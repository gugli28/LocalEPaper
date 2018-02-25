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
	first_name = u'\u092e' + u'\u0928' + u'\u094b' + u'\u091c'
	last_name = u'\u0905' + u'\u0935' + u'\u0938' + u'\u094d' \
	+ u'\u0925' + u'\u0940'
 
	print first_name + ' ' + last_name
	send_mail(configg.fromaddr,configg.password,configg.toaddr, first_name + ' ' + last_name ,"text.txt","/home/gugli/Documents/script_py/Dainik_Jagron/text.txt")


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

	a = u'\u0905'  + u'\u0916' +  u'\u093c'+ u'\u092c' + u'\u093e' + u'\u0930'
	k = u'\u0915'  + u'\u0943' +  u'\u092a'+ u'\u092f' + u'\u093e' 
	s = u'\u0938'  + u'\u0902' +  u'\u0932'+ u'\u0917' + u'\u094d' + u'\u0928'
	d = u'\u0922'  + u'\u0942' +  u'\u0902'+ u'\u0922' + u'\u093f' + u'\u090f'

	##Hindi translation for "Please find attached newspaper"
	body =  k+ ' ' + s + ' ' +a+ ' ' + d + '. . .'
	
	 
	# attach the body with the msg instance
	# msg.attach(MIMEText(body, 'plain')) ##in case of english font: no unicode char
	msg.attach(MIMEText(body.encode('utf-8'), 'plain'))
	 
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