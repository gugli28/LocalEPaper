import urllib2
import os

def main():
    # download_file("http://epaper.jagran.com/epaperimages/30012018/muzaffarpur/29smt-pg1-0.pdf","document.pdf")
    download_file("http://epaper.jagran.com/epaperimages/01022018/muzaffarpur/0bgh-pg2-0.pdf","document.pdf")
    filestatus = os.path.isfile('2.pdf')
    if filestatus :

        print "file already downloaded"

def download_file(download_url,file_path):
    response = urllib2.urlopen(download_url)
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # file_path = dir_path +"/"+filename
    # file = open("/home/gugli/Documents/script_py/document.pdf" , 'w')
    filestatus = os.path.isfile(file_path)
    if filestatus :
        print "file already downloaded :)))))))))))"
        return
    file = open( file_path , 'w')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()