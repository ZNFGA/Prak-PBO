class Hewan:
    def __init__(self, nama, jeniskelamin):
        self.nama = nama
        self.jeniskelamin = jeniskelamin

    def bersuara(self):
        pass

    def makan(self):
        pass

    def minum(self):
        pass


class Anjing(Hewan):
    def __init__(self, nama, jeniskelamin):
        super().__init__(nama, jeniskelamin)

    def bersuara(self):
        print(f"Anjing {self.nama} bersuara: Guk Guk !")

    def makan(self):
        print(f"Anjing {self.nama} sedang makan: Tulang")

    def minum(self):
        print(f"Anjing {self.nama} sedang minum: Susu")


class Kucing(Hewan):
    def __init__(self, nama, jeniskelamin):
        super().__init__(nama, jeniskelamin)

    def bersuara(self):
        print(f"Kucing {self.nama} bersuara: Meong !")

    def makan(self):
        print(f"Kucing {self.nama} sedang makan: Ikan")

    def minum(self):
        print(f"Kucing {self.nama} sedang minum: Susu")


hewan1 = Anjing('Anto', 'Betina')
hewan2 = Kucing('Ayu', 'Jantan')

hewan1.bersuara()
hewan2.bersuara()
print()

hewan1.makan()
hewan2.makan()
print()

hewan1.minum()
hewan2.minum()
