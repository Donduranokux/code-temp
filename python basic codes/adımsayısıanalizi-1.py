def veri_analizi():
    adim_verisi = [
        {"tarih": "2024-04-01", "adim": 8000},
        {"tarih": "2024-04-02", "adim": 10000},
        {"tarih": "2024-04-03", "adim": 6000},
        {"tarih": "2024-04-04", "adim": 7500},
        {"tarih": "2024-04-05", "adim": 9000},
        {"tarih": "2024-04-06", "adim": 11000},
        {"tarih": "2024-04-07", "adim": 8500},
    ]

    # Toplam adım sayısı
    toplam_adim = sum(veri["adim"] for veri in adim_verisi)
    print("Toplam adım sayısı:", toplam_adim)

    # Ortalama günlük adım sayısı
    ortalama_adim = toplam_adim / len(adim_verisi)
    print("Ortalama günlük adım sayısı:", ortalama_adim)

    # En yüksek ve en düşük adım sayısı
    en_yuksek_adim = max(veri["adim"] for veri in adim_verisi)
    en_dusuk_adim = min(veri["adim"] for veri in adim_verisi)
    print("En yüksek günlük adım sayısı:", en_yuksek_adim)
    print("En düşük günlük adım sayısı:", en_dusuk_adim)

    # En çok adım atılan tarih
    en_cok_adim_tarihi = max(adim_verisi, key=lambda x: x["adim"])["tarih"]
    print("En çok adım atılan tarih:", en_cok_adim_tarihi)

    # En az adım atılan tarih
    en_az_adim_tarihi = min(adim_verisi, key=lambda x: x["adim"])["tarih"]
    print("En az adım atılan tarih:", en_az_adim_tarihi)

if __name__ == "__main__":
    veri_analizi()
