My Papa asked me how do I get local newspaper online.
And this script was created. B:)
I thought of creating a cron job in my android but apparently it requires the android system to be rooted.
Used Qpython Application on Android to run this script. 

However I have Added Cron job on my ubuntu that executes the script once a day. I have not fixed a particular time rather I have made it conditional. 



## What does this script do ?
  * This script basically dowloads the individual pdf file of the news paper present on the website `http://epaper.jagran.com/homepage.aspx` .
  * It then merges the individual pdfs.
  * After the pdf merging it sends an email with an attachment ( e-paper ) to the email id.
  * As my main motto was to run it on android I have separated what lib are to be imported and what cmd are needed to install them in QPython ( Android App ).

## Conditional Cron
  * when ever my system is started the script first checks the txt file.
  * If the logged date is of today than the script dont run
  * else the script is run and after completon it logs todays date in the txt( ` checkCronStatus.txt` ) file 

## IN QPython 
  * install Qpython 
  * open terminal 
  * execute `pip.main(['install', 'bs4'])`
  * execute `pip.main(['install', 'PyPDF2'])`

## RUN
  * change the config file
  * import the libraries mentioned in the `import_lib.py`
  * add `to` id `from` id
  * run `python Dainik_e_paper.py`


## ERROR
  * you might have to turn on "Allow less secure apps for your emailid"
  ## SMTPAuthenticationError
    * https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
