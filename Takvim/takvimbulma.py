def takvim(yil, ay):
    # Ay isimlerini tanımla
    ay_isimleri = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
                   "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
    
    # Ayın gün sayısını hesapla
    gün_sayısı = [31, 28 if yil % 4 != 0 or (yil % 100 == 0 and yil % 400 != 0) else 29,
                   31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Ay ve yıl bilgisini yazdır
    print(f"{ay_isimleri[ay-1]} {yil}")
    print("Pzt Sal Çar Per Cum Cmt Paz")
    
    # İlk günün hangi gün olduğunu hesapla
    ilk_gün = (1 + sum(gün_sayısı[:ay-1]) + (yil-1)*365 + ((yil-1)//4) - ((yil-1)//100) + ((yil-1)//400)) % 7
    
    # İlk boşlukları ekleyerek başlangıç gününü ayarla
    for i in range(ilk_gün):
        print("   ", end=" ")
    
    # Günleri yazdır
    gün_sayacı = 0
    for gün in range(1, gün_sayısı[ay-1] + 1):
        if gün_sayacı == 7:
            gün_sayacı = 0
            print()
        print(f"{gün:2}", end=" ")
        gün_sayacı += 1
    print()

# Kullanıcıdan yıl ve ay bilgisini al
yil = int(input("Yılı giriniz: "))
ay = int(input("Ayı giriniz (1-12): "))

# Takvimi oluştur
takvim(yil, ay)
