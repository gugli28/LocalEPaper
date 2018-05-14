My Papa asked me how do I get local newspaper online.
And this script was created. B:)
I thought of creating a cron job in my android but apparently it requires the android system to be rooted.
Used Qpython Application on Android to run this script. 

However I have Added Cron job on my `ubuntu` that executes the script once a day. I have not fixed a particular time rather I have made it conditional. 


## What does this script do ?
  * This script basically dowloads the individual pdf file of the news paper present on the website `http://epaper.jagran.com/homepage.aspx` and `http://epaper.livehindustan.com/`
  * It then merges the individual pdfs.
  * After the pdf merging it sends an email with an attachment ( e-paper ) to the email id.
  * As my main motto was to run it on android I have separated what lib are to be imported and what cmd are needed to install them in QPython ( Android App ).

## Conditional Cron
  * whenever my system starts the script first checks the txt file.
  * If the logged date is of today than the script doesn't execute
  * Else the script is executed and after completon it logs todays date in the txt file 
  * First it checks if tor browser is started for the day `checkStartTorStatus.txt`.
  * Same check is done with `checkCronStatus.txt` and `checkCronStatusH.txt`.

## Pdf Compression
  * I was blown to see the bytes of the pdf file downloaded from `http://epaper.livehindustan.com/` website. The file size is over 10 Mb. In some cases it exceeds 20Mb. Yes one pdf file. So just do the math for 20 pages of news paper.
  * I initially used System cmd to compress file but it was not very efficient `CompressFile.py`.
  * So I choose to use online website `http://pdfcompressor.com/` . Its amazingly awesome. This site compressed file by 90%.
  * checkout the file `PdfCompressor.py`.


## TOR - Python - Selenium - webdriver
  * These tools are no less than  _Bramhastra_ Haahha! 
  * TOR is just necessary while using PYTHON
  * Use Firefox webdriver and changed the network preferences. See file `TorFirefox.py`.

## Watchdog
  * This file tracks any changes in the directory.
  * Used this to make sure that unzipping of file is done only after file is completely downloaded.
  * check the file `watchdogg.py`
  * Used `tqdm` to view the dowload progress. check `download.py`.

## IN QPython 
  * install Qpython 
  * open terminal 
  * execute `pip.main(['install', 'bs4'])`
  * execute `pip.main(['install', 'PyPDF2'])`
  * I have attached a sample of execution in Qpython. However I have changed the code for setting up conditional cron in Ubuntu.
  * I have added much more libraries untill now( 5th May 2018). The very first commit was focused on Qpython. Now its totally dekstop-mode script( I mean it has librabries than can be installed in Linux systems conveniently)

## RUN
  * change the config file
  * add `to` id `from` id
  * run `python Dainik_e_paper.py` ( this runs both the file `Dainik_e_paper.py` and `hindustan.py` )

## DEPENDENCIES
  * pyvirtualdisplay
  * BeautifulSoup
  * urllib2
  * selenium
  * tqdm
  * math
  * PyPDF2
  * requests
  * smtplib, email
  * wget
  * TorFirefox
  * multiprocessing
  * watchdog

## ERROR and References
  * you might have to turn on "Allow less secure apps for your emailid"
  * SMTPAuthenticationError : Use below link to check enabling access for less secure app on gmail
  * https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
  * I have added useful links that assisted me in some of the files.

## Sample execution video in QPython

   * [Watch the video](https://photos.app.goo.gl/2reXOkKhmu8rMlkx1)

## Email sample 
   * ![image](Email_sample2.jpeg)

