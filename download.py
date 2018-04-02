import urllib2
import os
import CompressFile
import pdf_merger

def main():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/" + "doc.pdf"
    download_file("http://epaper.jagran.com/epaperimages/25032018/muzaffarpur/24smt-pg1-0.pdf",file_path)
   
    # download_file("https://drive.google.com/file/d/1EqS7SQMGCz-XE5_Th7Lp_VXHZiuI12Vg/view",'hindu28feb.pdf')
    # filestatus = os.path.isfile('2.pdf')
    # if filestatus :

    #     print "file already downloaded"

def download_file(download_url,file_path):
    ## check if file already exists
    filestatus = os.path.isfile(file_path)
    if filestatus :
        print "(((((((((( file already downloaded :)))))))))))"
        return 0
    response = urllib2.urlopen(download_url)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dup_file_path = dir_path + "/" +"comp.pdf"

    ## file written in duplicate file name that is later compressed and file name is changed to file_path
    file = open( dup_file_path , 'w')
    file.write(response.read())
    file.close()
    print("Completed")

    ### compress only valid pdf file
    flag = pdf_merger.check_valid_pdf(dup_file_path)
    if(flag == 0):
        print "Hurray got a valid Pdf.. Now we gonna compress it !! "
        CompressFile.compress( dup_file_path, file_path )
        os.remove(dup_file_path)
    
    print "FLAG = ", flag
    return flag
            
            


if __name__ == "__main__":
    main()