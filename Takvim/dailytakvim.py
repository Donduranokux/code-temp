import datetime

def takvim():
    # Bugünün tarihini al
    bugun = datetime.date.today()
    
    # Ay isimlerini tanımla
    ay_isimleri = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
                   "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
    
    # Ayın gün sayısını hesapla
    gün_sayısı = [31, 28 if bugun.year % 4 != 0 or (bugun.year % 100 == 0 and bugun.year % 400 != 0) else 29,
                   31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Ay ve yıl bilgisini yazdır
    print(f"{ay_isimleri[bugun.month-1]} {bugun.year}")
    print("Pzt Sal Çar Per Cum Cmt Paz")
    
    # İlk günün hangi gün olduğunu hesapla
    ilk_gün = datetime.date(bugun.year, bugun.month, 1).weekday()
    
    # İlk boşlukları ekleyerek başlangıç gününü ayarla
    for i in range(ilk_gün):
        print("   ", end=" ")
    
    # Günleri yazdır
    for gün in range(1, gün_sayısı[bugun.month-1] + 1):
        if bugun.day == gün:
            print(f"\033[1m{gün:2}\033[0m", end=" ")  # Bugünü kalın olarak göster
        else:
            print(f"{gün:2}", end=" ")
        ilk_gün += 1
        if ilk_gün == 7:
            ilk_gün = 0
            print()
    print()

# Takvimi oluştur
takvim()
