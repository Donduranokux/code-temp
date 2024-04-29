import time

class Kronometre:
    def __init__(self):
        self.baslangic_zamani = None
        self.bitis_zamani = None

    def basla(self):
        self.baslangic_zamani = time.time()
        print("Kronometre başladı.")

    def dur(self):
        self.bitis_zamani = time.time()
        print("Kronometre durduruldu.")

    def gecen_sure(self):
        if self.baslangic_zamani is None:
            print("Kronometre başlatılmadı.")
            return
        if self.bitis_zamani is None:
            return time.time() - self.baslangic_zamani
        return self.bitis_zamani - self.baslangic_zamani

if __name__ == "__main__":
    kronometre = Kronometre()
    kronometre.basla()
    input("Kronometreyi durdurmak için Enter'a basın.")
    kronometre.dur()
    print("Geçen süre: {:.2f} saniye".format(kronometre.gecen_sure()))
