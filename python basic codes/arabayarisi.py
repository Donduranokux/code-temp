import time
import random

def yaris():
    mesafe = 100
    oyuncu_pozisyon = 0
    rakip_pozisyon = 0
    
    print("Yarış başlıyor!")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Başla!")
    
    while oyuncu_pozisyon < mesafe and rakip_pozisyon < mesafe:
        # Oyuncunun hızı
        oyuncu_hiz = random.randint(1, 5)
        oyuncu_pozisyon += oyuncu_hiz
        
        # Rakibin hızı
        rakip_hiz = random.randint(1, 5)
        rakip_pozisyon += rakip_hiz
        
        print("\nOyuncunun pozisyonu:", "-" * oyuncu_pozisyon + "🚗")
        print("Rakibin pozisyonu:   ", "-" * rakip_pozisyon + "🚗")
        time.sleep(0.5)
    
    if oyuncu_pozisyon >= mesafe:
        print("\nTebrikler! Oyuncu kazandı!")
    else:
        print("\nMaalesef, rakip kazandı. Bir dahaki sefere daha şanslı olabilirsiniz!")

yaris()
