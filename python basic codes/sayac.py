import time

def geri_sayim(saniye):
    while saniye > 0:
        print(saniye)
        time.sleep(1)
        saniye -= 1
    print("Geri sayım tamamlandı!")

if __name__ == "__main__":
    try:
        saniye = int(input("Kaç saniye geri sayım yapmak istiyorsunuz?: "))
        geri_sayim(saniye)
    except ValueError:
        print("Geçersiz giriş! Bir tam sayı giriniz.")
