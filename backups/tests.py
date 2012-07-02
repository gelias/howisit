from django.test import TestCase
from backups.models import Backup

class BackupTest(TestCase):

    def test_should_create_backup_file_instance(self):
    	path = '/temp'
		file_name = 'bckp*.zip'
		self.backup = Backup(path, file_name)
        self.assertIsNotNone(self.backup)

    def test_should_check_file_existing(self):
    	path = '/temp'
		file_name = 'bckp*.zip'
		self.backup = Backup(path, file_name)
        self.assertTrue(self.backup.itsHere)

