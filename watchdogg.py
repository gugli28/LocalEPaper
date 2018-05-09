'''
this file tracks the changes in the directory entioned.
It runs untill the zip file is downloaded.

'''

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import re
import os
"""
http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html
https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory
this code is working but dont know how to make use of it the script """
class Watcher:
    # DIRECTORY_TO_WATCH = "/path/to/my/directory"
    DIRECTORY_TO_WATCH = os.getcwd()
    def __init__(self):
        self.observer = Observer()
        print "   ---------INIT------------"

    def run(self):
        print "   ----------RUN--------------"
        event_handler = Handler()

        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            print "    ---------TRY-----------"
            # while True:
            #     time.sleep(5)
            '''run this until the zip file is not downloaded 
                the txt file is updated as "Created" when there is some activity in the given Directory
                it is updated as "DONE" whe the zip file completely downloads
            '''
            fileObject = open(os.getcwd()+"/checkDownStatus.txt" ,"r")
            status = fileObject.read()
            while( status != "DONE"):
                fileObject = open(os.getcwd()+"/checkDownStatus.txt","r")
                status = fileObject.read()
                print "     ----Watching any changes----" , status, status != "DONE"
                time.sleep(5)
            fileObject.close()
            self.observer.stop()


        except Exception as e:
            print e
            print '    -----EXCEPT-----------'
            self.observer.stop()
            print "Error"

        print "    ------JOIN -----------"
        self.observer.join()



class Handler(FileSystemEventHandler):
# class Handler(FileSystemEventHandler):
#     patterns=[r"*.zip.*"]
    print "   ----------Handler-------------"
    @staticmethod
    def on_any_event(event):
        # print "   ----------on_any_event--------------"
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            # print re.match('.*zip',event.src_path) 
            if( re.match('.*zip',event.src_path)):

                print "=====================ZIP CREATED===================="
                print "Received created event - %s." % event.src_path
                with open(os.getcwd()+"/checkDownStatus.txt"+'checkDownStatus.txt','w') as outFile:
                    outFile.write("CREATED")


        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            if(event.src_path[-4:]== ".zip"):
                print "=====================ZIP MODIFIED===================="
                print "Received modified event - %s." % event.src_path
                print event.src_path[-4:], type(event.src_path[-4:]), event.src_path[-4:]== "zip."
                print "=====HURRAY STR matched====="
                with open(os.getcwd()+"/checkDownStatus.txt",'w') as outFile:
                    outFile.write("DONE")


if __name__ == '__main__':
    w = Watcher()
    w.run()
   
