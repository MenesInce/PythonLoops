kullanici1 = {
    "ad" : "Ferhat",
    "soyad" : "Ibrik",
    "uzmanlik" : ["Front-End"]
}
kullanici2 = {
    "ad" : "Gokce",
    "soyad" : "Gun",
    "uzmanlik" : ["Tasarim"]
}
kullanici3 = {
    "ad" : "Mesut",
    "soyad" : "Gun",
    "uzmanlik" : ["Front-End"]
}

#* Soru 1 : Ferhat Ibrik kullanıcısının uzmanlık alanını dödür
print(kullanici1.get("uzmanlik"))

#* Soru 2 : Front-End uzmanlığındaki isimleri döndürün
kullanici_listesi = [kullanici1,kullanici2,kullanici3]
for kullanici in kullanici_listesi : 
    if kullanici.get("uzmanlik") == ["Front-End"] :
        print(kullanici.get("ad"))

#* Soru 3 : Mesut kullanicisi Yazılım öğrendi. Bilgilerini güncelle
kullanici3["uzmanlik"].append("Yazilim")
print(kullanici_listesi)

#* Soru 4 : birden fazla uzmanlık alanı olanı döndür
for k1 in kullanici_listesi :
    if len(k1.get("uzmanlik")) > 1 :
        print(kullanici.get("ad"))

#* Soru 5 : zip kullanarak 2 listeyi birleştir ve yaşları 30 dan büyük olanı yaz
kullanici_yaslari_listesi = [22,34,32]

for k2,yas in zip (kullanici_listesi,kullanici_yaslari_listesi) :
    if yas > 30 :
        print(k2)

#* Soru 6 : Asal sayı bul

deger = int(input("Bir sayı girin : "))
x = deger - 1
while x > 1 :
    if deger%x == 0 :
        print("{} sayısı asal değil".format(deger))
        break
    else : 
        x -= 1
else :
    print("{} sayısı asaldır".format(deger))

        

