class YemekTarifleri:
    def __init__(self):
        self.tarifler = {
            "Lahmacun": [
                "Hamur yoğrulur.",
                "İç malzemesi hazırlanır ve hamurun üzerine sürülür.",
                "Fırında pişirilir."
            ],
            "Pide": [
                "Hamur yoğrulur ve şekil verilir.",
                "İç malzemesi yerleştirilir.",
                "Fırında pişirilir."
            ],
            "Döner": [
                "Kıyma ve et karıştırılır.",
                "Baharatlar eklenir ve yoğrulur.",
                "Dinlendirilir ve şişe takılır.",
                "Odun ateşinde pişirilir."
            ],
            "Künefe": [
                "Tel kadayıf tuzsuz tereyağı ile kavrulur.",
                "Peynir iç malzemesi hazırlanır.",
                "Kadayıfın alt katı serilir, peynir konur, üstü kapatılır.",
                "Tatlı fırında pişirilir ve şerbet dökülür."
            ],
            "Mücver": [
                "Kabak rendelenir ve suyu sıkılır.",
                "Rendelenmiş kabak, rendelenmiş soğan, ince doğranmış maydanoz, yumurta, un, tuz ve karabiber karıştırılır.",
                "Karışım kızgın yağda kızartılır."
            ],
            "Yaprak Sarma": [
                "Salça, pirinç, doğranmış soğan, maydanoz, nane ve baharatlar karıştırılır.",
                "Başta yapraklar olmak üzere sarılacak malzemeler hazırlanır.",
                "Hazırlanan karışım sarılır ve tencereye yerleştirilir.",
                "Üzerine su ve limon suyu eklenir, pişirilir."
            ],
            "İskender Döner": [
                "Döner etleri ızgarada pişirilir.",
                "Pişen etler ekmek dilimlerinin üzerine yerleştirilir.",
                "Üzerine tereyağı ve domates sosu dökülür, yoğurt ile servis edilir."
            ]
        }

    def tarif_goster(self, yemek_adi):
        if yemek_adi in self.tarifler:
            print(f"{yemek_adi} Tarifi:")
            print("\n".join(self.tarifler[yemek_adi]))
        else:
            print(f"{yemek_adi} için tarif bulunamadı.")


yemek_tarifleri = YemekTarifleri()

# Yemek listesini göster
print("Yemekler:")
for yemek_adi in yemek_tarifleri.tarifler.keys():
    print("- " + yemek_adi)

# Kullanıcıdan yemek adını alın ve tarifi gösterin
while True:
    yemek_adi = input("Yemek adını girin (Çıkmak için 'q' ya basın): ").strip()
    if yemek_adi.lower() == 'q':
        break
    yemek_tarifleri.tarif_goster(yemek_adi)
