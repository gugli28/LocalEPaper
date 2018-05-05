import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

"""
http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html
https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory
this code is working but dont know how to make use of it the script """
class Watcher:
    # DIRECTORY_TO_WATCH = "/path/to/my/directory"
    DIRECTORY_TO_WATCH = "/home/gugli/Documents/script_py/Dainik_Jagron"
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
            while True:
                time.sleep(5)
        except:
            print '    -----EXCEPT-----------'
            self.observer.stop()
            print "Error"

        print "    ------JOIN -----------"
        self.observer.join()



class Handler(FileSystemEventHandler):
    print "   ----------Handler-------------"
    @staticmethod
    def on_any_event(event):
        # print "   ----------on_any_event--------------"
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print "Received created event - %s." % event.src_path


            with open('/home/gugli/Documents/script_py/Dainik_Jagron/checkDownStatus.txt','w') as outFile:
                outFile.write("CREATED")


        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print "Received modified event - %s." % event.src_path

            print event.src_path[-4:], type(event.src_path[-4:]), event.src_path[-4:]== "zip."
            if(event.src_path[-4:]== ".zip"):
                print "=====HURRAY STR matched====="
                with open('/home/gugli/Documents/script_py/Dainik_Jagron/checkDownStatus.txt','w') as outFile:
                    outFile.write("DONE")


if __name__ == '__main__':
    w = Watcher()
    w.run()