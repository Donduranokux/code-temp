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
    for gün in range(1, gün_sayısı[ay-1] + 1):
        print(f"{gün:2}", end=" ")
        ilk_gün += 1
        if ilk_gün == 7:
            ilk_gün = 0
            print()
    print()

# Takvimi oluştur
takvim(2024, 4)
