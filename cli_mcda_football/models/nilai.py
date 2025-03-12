from peewee import *
import Mahasiswa, Kriteria

class Nilai(Model):
    mahasiswa = Mahasiswa
    cr = Kriteria()
    
    # mhs: Mahasiswa

    def perhitungan(self):
        return self.mhs.getNama()
