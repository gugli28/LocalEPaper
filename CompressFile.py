import os
import compressOnline

# https://askubuntu.com/questions/113544/how-can-i-reduce-the-file-size-of-a-scanned-pdf-file

def main():
    # download_file("http://epaper.jagran.com/epaperimages/30012018/muzaffarpur/29smt-pg1-0.pdf","document.pdf")
    
    filestatus = os.path.isfile('aa1.pdf')
    if filestatus :

        print "file already downloaded"
    # compress('aa1.pdf','o.pdf') 
    # compressOnline.compress('25032018.pdf','co.pdf')
    # dir_path = os.path.dirname(os.path.realpath(__file__))

    # print dir_path
    i =0
    while i<1:
        print i
        i = i+1
        
    byte= os.stat('25032018.pdf').st_size
    print byte #29743629
    compress('2.pdf','out2.pdf')
    percent  = 15
    # print "Compressed by",(percent), '%'
def compress( input_file_path, out_file_path):

    # os.system("ps2pdf -dPDFSETTINGS=/ebook %s %s" % (input_file_path, out_file_path))
    temp = out_file_path
    temp1 = input_file_path
    i = 0
    while i<10 :
        # print i
        # print input_file_path, out_file_path
        os.system("gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=%s %s "% ( out_file_path ,input_file_path))
        # byte_out= os.stat(out_file_path).st_size
        # byte_in = os.stat(input_file_path).st_size
        # print byte_out, " ", byte_in - byte_out

        # temp = out_file_path
        input_file_path = out_file_path
        out_file_path = str(i) + 'o.pdf'

        filestatus = os.path.isfile(str(i-2) + 'o.pdf')
        if filestatus :
            os.remove(str(i-2) + 'o.pdf')
            # print "file del", str(i-2) + 'o.pdf' 

        i = i +1

    input_file_path = str(i-2) + 'o.pdf'
    out_file_path = temp
    os.system("gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=%s %s "% ( out_file_path ,input_file_path))
    os.remove(input_file_path)

    byte_out= os.stat(out_file_path).st_size
    byte_in = os.stat(temp1).st_size
    percent = ((byte_in - byte_out)*100)/byte_in

    # print byte
    # compressOnline.compress(input_file_path,out_file_path)
    print "-------Compressed by %s" %(percent),'%'

if __name__ == "__main__":
    main()