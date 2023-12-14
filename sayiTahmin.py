sayi = 25
hak = 5

while hak > 0 :
    tahmin = int(input("Pozitif bir tam sayı giriniz : "))
    if tahmin <= 0 :
        print("Girdiğiniz sayı pozitif bir tam sayı değildir..")
        continue
      
    if sayi == tahmin :
        print("Doğru tahmin ettiniz tebrikler..!!")
        break
    elif tahmin > sayi :
        print("Yukarı, kalan hakkınız {}".format(hak))
        hak -= 1
    else : 
         print("Aşağı, kalan hakkınız {}".format(hak))
         hak -= 1

    if hak == 0 :
        print("Hakkınız kalmadı. Doğru sayı {} olacaktı".format(sayi))

         
