
'''
this file made me understand the flow of watchdogg.py
But the problem with this is that it doen't tracks the file change as frequent as watchdogg.py.
So this was not used.
'''

import sys
import time
# import xmltodict
# import magicdate
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler


# from .models import Media

#http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html
#https://pythonhosted.org/watchdog/
class MyHandler(FileSystemEventHandler):
	patterns=["*.pdf"]
	print "--- HANDLER"

	

	def process(self, event):
		"""
		event.event_type
		    'modified' | 'created' | 'moved' | 'deleted'
		event.is_directory
		    True | False
		event.src_path
		    path/to/observed/file """
		print " --------IN pROCESS"
		# print event.src_path[-5:], type(event.src_path)
		# if(event.src_path[-4:]== ".zip."):
		# 	print "=====HURRAY STR matched====="

		# 	with open('/home/gugli/Documents/script_py/Dainik_Jagron/checkDownStatus.txt','w') as outFile:
		# 		outFile.write("DONE")
		# with open(event.src_path, 'r') as xml_source:
		#     xml_string = xml_source.read()
		#     parsed = xmltodict.parse(xml_string)
		#     element = parsed.get('Pulsar', {}).get('OnAir', {}).get('media')
		#     if not element:
		#         return

		#     media = Media(
		#         title=element.get('title1'),
		#         description=element.get('title3'),
		#         media_id=element.get('media_id1'),
		#         hour=magicdate(element.get('hour')),
		#         length=element.get('title4')
		#     )
		#     media.save()

	def on_modified(self, event):
		print " ------- ON MODIFIED"
		print event.src_path
		self.process(event)

	def on_created(self, event):
		print " ------- ON CREATED"
		print event.src_path
		self.process(event)
	# 	with open('/home/gugli/Documents/script_py/Dainik_Jagron/checkDownStatus.txt','w') as outFile:
	# 			outFile.write("CREATED")

	# 	self.process(event)


if __name__ == '__main__':
	args = sys.argv[1:]
	observer = Observer()
	DIRECTORY_TO_WATCH = "/home/gugli/Documents/script_py/Dainik_Jagron"
	#observer.schedule(MyHandler(), path=args[0] if args else '.')
	""" You can set the named-argument "recursive" to True for observer.schedule.
	 if you want to watch for files in subfolders."""

	observer.schedule(MyHandler(), path=DIRECTORY_TO_WATCH)
	print " ----------------- "
	observer.start()

	try:
		while True:
			print "==========",observer.isAlive()
			
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()