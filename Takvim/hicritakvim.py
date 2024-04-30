import datetime

def hicri_takvim():
    # Bugünün tarihini al
    bugun = datetime.date.today()
    
    # Hicri ay isimlerini tanımla
    hicri_ay_isimleri = ["Muharrem", "Safer", "Rebiülevvel", "Rebiülahir",
                         "Cemaziyelevvel", "Cemaziyelahir", "Recep", "Şaban",
                         "Ramazan", "Şevval", "Zilkade", "Zilhicce"]
    
    # Hicri tarih hesaplamak için sabitleri tanımla
    gregoryan_yili = bugun.year
    gregoryan_ayi = bugun.month
    gregoryan_gunu = bugun.day

    tarih = bugun.toordinal() - datetime.date(gregoryan_yili, 1, 1).toordinal() + 1
    hicri_yili = gregoryan_yili - 622 if gregoryan_ayi < 10 or (gregoryan_ayi == 10 and gregoryan_gunu < 21) else gregoryan_yili - 621
    toplam_gun = 0
    for i in range(1, 13):
        toplam_gun += 29 if i <= 6 else 30
        if i % 2 == 0 and i != 12:
            toplam_gun += 1
    toplam_gun += (hicri_yili - 1) * 354 + (hicri_yili - 1) // 33 * 8 + ((hicri_yili - 1) % 32 + 3) // 8 + tarih
    
    # Hicri tarihi yazdır
    print(f"{hicri_ay_isimleri[int((toplam_gun - 1) // 29.530588853 + 2) % 12 - 1]} {hicri_yili}")
    print("Pzt Sal Çar Per Cum Cmt Paz")
    
    # İlk günün hangi gün olduğunu hesapla
    ilk_gün = datetime.date(bugun.year, bugun.month, 1).weekday()
    
    # İlk boşlukları ekleyerek başlangıç gününü ayarla
    for i in range(ilk_gün):
        print("   ", end=" ")
    
    # Günleri yazdır
    gün_sayısı = 30 if int((toplam_gun - 1) // 29.530588853 + 2) % 12 in [1, 5, 7, 10] else 29
    for gün in range(1, gün_sayısı + 1):
        if bugun.day == gün:
            print(f"\033[1m{gün:2}\033[0m", end=" ")  # Bugünü kalın olarak göster
        else:
            print(f"{gün:2}", end=" ")
        ilk_gün += 1
        if ilk_gün == 7:
            ilk_gün = 0
            print()
    print()

# Hicri takvimi oluştur
hicri_takvim()
