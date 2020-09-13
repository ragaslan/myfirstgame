import random
import time
def oyunbaslat():
    print("****** SAYI BULMA OYUNU Version-0 ******")
    print("Oyun Ayarları...")
    time.sleep(1)
    while True:
        ustsinir = input("Zorlugunu Seciniz kolay(k)/orta(o)/zor(z) :")
        if ustsinir == "k":
            sayi = "50"
            print("sayınız 0 ile 50 arasından seçilecek")
            break
        elif ustsinir == "o":
            sayi = "250"
            print("sayınız 0 ile 250 arasından seçilecek")
            break
        elif ustsinir == "z":
            sayi = "1000"
            print("sayınız 0 ile 1000 arasından seçilecek")
            break
        else:
            print("hatalı yazım")

    oyunsayisi = random.randrange(0, int(sayi))
    time.sleep(1)
    print("Oyun Ayarları Bitti Hadi Başlayalım !")
    i = 0
    while True:
        oyuncusayi = int(input("hadi sayıyı bul"))

        if oyuncusayi < oyunsayisi:
            print("Sayımız " + str(oyuncusayi) + " 'dan büyük")
            i+=1
        elif oyuncusayi > oyunsayisi:
            print("Sayımız " + str(oyuncusayi) + " 'dan küçük")
            i += 1
        elif oyuncusayi == oyunsayisi:
            print("K-A-Z-A-N-D-I-N")
            print(str(i+1) + ". seferde bildin")
            time.sleep(1)

            break
    while True:
        karar = input("Tekrar Oynamak İstermisin E/H")
        if karar == "E":
            print("oyun başlıyorr..")
            time.sleep(1)
            oyunbaslat()
            break
        elif karar == "H":
            print("Tekrar Bekleriz Oyundan Çıkılıyor..")
            time.sleep(1)
            exit()

        else:
            print("Hatalı Cevap")






oyunbaslat()
