from abc import ABC, abstractmethod


def pasien_decorator(cls):
   
    print(f"Class {cls.__name__} didekorasi!")
    return cls


class Pasien(ABC):
   

    def __init__(self, nama, no_rm, gejala):
      
        self.nama = nama
        self.no_rm = no_rm
        self.gejala = gejala
        print(f"Pasien {self.nama} ({self.no_rm}) telah dibuat!")

    def __del__(self):
        
        print(f"Pasien {self.nama} ({self.no_rm}) telah dihapus!")

    @abstractmethod
    def bersabar(self):
        
        pass


@pasien_decorator
class PasienUmum(Pasien):
   
    def __init__(self, nama, no_rm, gejala, no_antrian):
        
        super().__init__(nama, no_rm, gejala)
        self.no_antrian = no_antrian

    def bersabar(self):
       
        print(f"{self.nama} ({self.no_rm}) bersabar menunggu antrian nomor {self.no_antrian}")


@pasien_decorator
class PasienDarurat(Pasien):
   

    def __init__(self, nama, no_rm, gejala):
       
        super().__init__(nama, no_rm, gejala)

    def bersabar(self):
       
        print(f"{self.nama} ({self.no_rm}) tidak perlu bersabar karena kasus darurat")


# Contoh penggunaan
pasien_umum = PasienUmum("Zakhi algifari", "2634782834", "Kecelakaan", 10)
pasien_darurat = PasienDarurat("Lucky", "987654321", "Sakit jiwa")

pasien_umum.bersabar()
pasien_darurat.bersabar()
