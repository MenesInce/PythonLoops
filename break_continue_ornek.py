sayac = 2

for i in range(0,3) :
    kullanici_Adi = str(input("Kullanıcı Adı : "))
    kullanici_Pswrd = str(input("Şifre : "))

    sistemKA = "Anlaşılır Ekonomi"
    sistemPswrd = "1234567"

    if kullanici_Adi == sistemKA and kullanici_Pswrd == sistemPswrd :
        print("Giriş başarılı.")
        break
    elif (kullanici_Adi != sistemKA or kullanici_Pswrd != sistemPswrd) and sayac != 0 :
        print("Hatalı giriş yaptınız. Kalan hakkınız : {}".format(sayac))
        sayac -= 1
    else : print("Kalan kullanım hakkınız : {} . Kapatılıyor".format(sayac))
    
