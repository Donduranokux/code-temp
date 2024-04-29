import matplotlib.pyplot as plt

def grafik_olustur():
    # Veri setleri
    yillar = [2015, 2016, 2017, 2018, 2019, 2020]
    gelirler = [50000, 55000, 60000, 65000, 70000, 75000]
    giderler = [30000, 32000, 35000, 37000, 40000, 42000]

    # Çizgi grafiği
    plt.figure(figsize=(8, 5))
    plt.plot(yillar, gelirler, marker='o', label='Gelirler')
    plt.plot(yillar, giderler, marker='o', label='Giderler')
    plt.title('Gelirler ve Giderler')
    plt.xlabel('Yıllar')
    plt.ylabel('Miktar (TL)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Bar grafiği
    plt.figure(figsize=(8, 5))
    plt.bar(yillar, gelirler, label='Gelirler', color='skyblue')
    plt.bar(yillar, giderler, label='Giderler', color='salmon', alpha=0.7)
    plt.title('Gelirler ve Giderler')
    plt.xlabel('Yıllar')
    plt.ylabel('Miktar (TL)')
    plt.legend()
    plt.grid(axis='y')
    plt.show()

    # Pasta grafiği
    plt.figure(figsize=(6, 6))
    plt.pie(gelirler, labels=yillar, autopct='%1.1f%%', startangle=140)
    plt.title('Yıllara Göre Gelir Dağılımı')
    plt.show()

if __name__ == "__main__":
    grafik_olustur()
