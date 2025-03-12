from peewee import *

# 1 player punya banyak nilai
class Mahasiswa(Model):
    nama = TextField()
    
    def getNama(self):
        return self.nama
