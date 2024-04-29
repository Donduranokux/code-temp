import random

def tahmin_oyunu():
    print("***** Sayı Tahmin Oyununa Hoş Geldiniz *****")
    print("Bilgisayar rastgele bir sayı seçti. Bu sayıyı tahmin etmeye çalışın!")

    tahmin_edilecek_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        try:
            tahmin = int(input("Tahmininiz: "))
            tahmin_sayisi += 1

            if tahmin < tahmin_edilecek_sayi:
                print("Daha büyük bir sayı girin.")
            elif tahmin > tahmin_edilecek_sayi:
                print("Daha küçük bir sayı girin.")
            else:
                print(f"Tebrikler! {tahmin_edilecek_sayi} sayısını doğru tahmin ettiniz!")
                print(f"Tahmin sayınız: {tahmin_sayisi}")
                break
        except ValueError:
            print("Geçersiz giriş! Bir sayı girin.")

if __name__ == "__main__":
    tahmin_oyunu()
