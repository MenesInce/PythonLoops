sayi = 0
while sayi <= 100 :
    print(sayi)
    sayi+=1

sayi1 = 100
while sayi1 >= 0 :
    print(sayi1)
    sayi1 -=1

print("*" * 30)

x = 0
while x < 10 :
    print("{} değeri 10'dan küçüktür".format(x))
    x += 1
else :
    print("{} değeri 10'dan küçük değil".format(x))


print("*" * 30)

fak = 1
sayi = 1

while sayi <= 10 :
    fak *= sayi
    print("{}! : {}".format(sayi,fak))
    sayi += 1
    
print("*" * 30)

fak1 = 1
s = 6

while s > 0 :
    fak1 *= s
    s -=1
print(fak1)