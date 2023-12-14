
yorum_birakanlar = ["İsmail Aydemir","Uygar Aydın","Naz Yağcıoğlu","Ferhat İbrik","Ulaş Acil"]
moderatör = "Naz Yağcıoğlu"
kullanici_sayisi = 0
moderator_sayisi = 0

for kullanici in yorum_birakanlar :

    ad = kullanici.split()[0]
    soyad = kullanici.split()[1]
    if kullanici == moderatör :
        moderator_sayisi += 1
        print(f'----{moderator_sayisi}. Moderatörün----  \nAdı    : {ad} \nSoyadı : {soyad} ')
    else : 
        kullanici_sayisi += 1
        print(f'----{kullanici_sayisi}.Kullanıcının----  \nAdı    : {ad} \nSoyadı : {soyad} ')




tup1 = (1,3,5,7)
for sayi in tup1 :
    print(sayi)

print("*" * 30)



liste = [[1,2],[3,4],[5,6],['a','b']]

for x,y in liste :
    print(x)

print("*" * 30)

liste1 = [[1,2],[3,4],[5,6]]

for x,y in liste1 :
    print(f'{x} * {y} : {x * y}')

print("*" * 30)


kullanici1 = {
    "ad" : "Naz",
    "soyad" : "Yağcıoğlu"
}
print(kullanici1.items())

for k , v in kullanici1.items() :
    print(f'Key   : {k} \nValue : {v}')