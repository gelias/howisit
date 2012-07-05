from django.db import models

import os

class Backup:

	def setUp(self):
		file = None
		try:
			file = open('/temp/bckp.zip', 'w')
		except Exception, e:
			print 'Fudeu'
		finally:
			print file.name
			file.close
		

	def __init__(self, path, file_pattern):
	  self.path = path
	  self.file_pattern = file_pattern

	def how_is_it(self):
		filepath = '%s/%s' % (self.path,self.file_pattern)
		print filepath
		print os.path.isfile(filepath)
		return os.path.isfile(filepath)