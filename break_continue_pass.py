harfler = ['a','b','c','d','e'] * 100
for index,harf in enumerate(harfler) :
    if harf == 'c' :
        print("{} harfi {}.indexte ".format(harf,index))
        break

for sayi in range(1,6) :
    if sayi %2 == 0 :
        continue
    print(sayi)

 
for sayi1 in range(1,6) :
    if sayi1 %2 == 0 :
        pass
    else :
        print(sayi)    