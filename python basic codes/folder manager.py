def menu_goster():
    print("Dosya İşlemleri")
    print("1. Dosya Oluştur")
    print("2. Dosya Oku")
    print("3. Dosyaya Yaz")
    print("4. Dosya Düzenle")
    print("5. Çıkış")

def dosya_olustur():
    dosya_adi = input("Oluşturulacak dosyanın adını girin: ")
    try:
        with open(dosya_adi, 'x'):
            print(f"{dosya_adi} adlı dosya oluşturuldu.")
    except FileExistsError:
        print(f"{dosya_adi} adlı dosya zaten var.")

def dosya_oku():
    dosya_adi = input("Okunacak dosyanın adını girin: ")
    try:
        with open(dosya_adi, 'r') as dosya:
            icerik = dosya.read()
            print(f"{dosya_adi} dosyasının içeriği:\n{icerik}")
    except FileNotFoundError:
        print(f"{dosya_adi} adlı dosya bulunamadı.")

def dosyaya_yaz():
    dosya_adi = input("Yazılacak dosyanın adını girin: ")
    icerik = input("Dosyaya yazılacak metni girin: ")
    with open(dosya_adi, 'w') as dosya:
        dosya.write(icerik)
    print(f"{dosya_adi} dosyasına yazıldı.")

def dosya_duzenle():
    dosya_adi = input("Düzenlenecek dosyanın adını girin: ")
    try:
        with open(dosya_adi, 'r+') as dosya:
            icerik = dosya.read()
            print(f"{dosya_adi} dosyasının mevcut içeriği:\n{icerik}")
            yeni_icerik = input("Yeni içeriği girin: ")
            dosya.seek(0)
            dosya.truncate()
            dosya.write(yeni_icerik)
            print(f"{dosya_adi} dosyası düzenlendi.")
    except FileNotFoundError:
        print(f"{dosya_adi} adlı dosya bulunamadı.")

while True:
    menu_goster()
    secim = input("Yapmak istediğiniz işlemi seçin (1-5): ")

    if secim == '1':
        dosya_olustur()
    elif secim == '2':
        dosya_oku()
    elif secim == '3':
        dosyaya_yaz()
    elif secim == '4':
        dosya_duzenle()
    elif secim == '5':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir seçim yapın.")
