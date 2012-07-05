from django.test import TestCase
from backups.models import Backup
import os

class TestBackup(TestCase):
    
    def setUp(self):
        print "setup ..."
        try:
            f = open('/temp/bckp.zip', 'w')
            f.close
        except Exception, e:
            raise e

    def test_should_create_backup_file_instance(self):
        path = "/temp"
        file_pattern = ""
        backup = Backup(path,file_pattern)
        self.assertIsNotNone(backup)

    def test_should_check_file_existing(self):
        path = "/temp"
        file_pattern = "bckp.zip"
        backup = Backup(path,file_pattern)
        self.assertTrue(backup.how_is_it())

