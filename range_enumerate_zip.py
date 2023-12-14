
#? Range
print(list(range(10)))

print([*range(10)])

print([*range(2,7,2)])

print("-" *30)
for sayi in range(10) :
    print(sayi)

print("-" *30)

#? Enumerate -> indeks ve eleman -> (0 ,a) gibi

harfler = ['a','b','c','d']
for harf in enumerate(harfler) :
    print(harf)

print("-" *30)

harfler1 = ['a','b','c','d']
for index , harf1 in enumerate(harfler) :
    #print(index + 1,harf1)
    print("{}. Sayı : {} ".format(index + 1, harf1))

print("-" *30)

#? zip -> uzunlukları eşit olan iterb özellikteki yapıları ilişkilendirir

ulkeler = ["TR","FR","DE"]
siralamalar = range(1,4)
for ulke in zip(ulkeler,siralamalar) :
    print(ulke)


