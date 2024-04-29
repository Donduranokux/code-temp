def macera_oyunu():
    print("Hoş geldiniz! Hayal gücünüzü kullanarak bir maceraya başlamaya hazır mısınız?")
    print("Başlangıçta iki yol var: Ormanda keşfe çıkmak için 'orman' veya dağ yolunu seçmek için 'dağ'.")

    secim = input("Yolunuzu seçin: ")

    if secim == "orman":
        print("Ormanda yürüyorsunuz. Bir nehirle karşılaşıyorsunuz. Köprüyü geçmek istiyor musunuz? (evet/hayır)")
        nehir_secim = input("Seçiminizi yapın: ")

        if nehir_secim == "evet":
            print("Köprüyü geçtikten sonra, gizemli bir mağara keşfediyorsunuz. İçeri girmek ister misiniz? (evet/hayır)")
            magara_secim = input("Seçiminizi yapın: ")

            if magara_secim == "evet":
                print("Mağarada hazineyi buldunuz! Kazandınız!")
            else:
                print("Maalesef, mağaraya girmediniz ve hazineyi kaçırdınız. Oyunu kaybettiniz.")
        else:
            print("Nehri geçemediniz ve geri dönmeye karar verdiniz. İyi bir seçim değildi. Oyunu kaybettiniz.")

    elif secim == "dağ":
        print("Dağ yolunu seçtiniz. Yolda kar fırtınası başladı. Ne yapacaksınız?")
        print("a. Yoluna devam etmek")
        print("b. Bir mağaraya sığınmak")

        kar_secim = input("Seçiminizi yapın (a veya b): ")

        if kar_secim == "a":
            print("Yolunuza devam ediyorsunuz. Kar fırtınası giderek şiddetleniyor. Kayboldunuz ve donarak öldünüz. Oyunu kaybettiniz.")
        elif kar_secim == "b":
            print("Mağaraya sığındınız. Sıcak bir ateş yakarak ısınıyorsunuz. Kar fırtınası geçtikten sonra yola devam ediyorsunuz. Kazandınız!")
        else:
            print("Geçersiz seçim. Oyunu kaybettiniz.")
    else:
        print("Geçersiz seçim. Oyunu kaybettiniz.")

if __name__ == "__main__":
    macera_oyunu()
