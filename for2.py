# 1  den 100 e kadar olan tek ve çift sayıları yazdırın

for sayi in range(101) :
    if sayi % 2 == 0 :
        print(f'{sayi} çift sayıdır')
    else : print(f'{sayi} tek sayıdır')

#klavyeden girilen sayı kadar yazdıran döngü

sayi1 = int(input("Bir sayı giriniz"))
for i in range(0,sayi1+1) : print(i)    

s1 = int(input("Bir sayı giriniz"))
yaz = range(0,s1+1)
for i in yaz : 
    print(i)
    
# 1  den 100 e kadar olan sayıların toplamı

s2 = range(0,100)
toplam = 0
for i in s2 :
    toplam += i
print(toplam)