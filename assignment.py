x,y,z=2,5,107
numbers=1,5,7,10,6

#Kullanıcıdan aldığımız iki sayıyı çarpıp sonuctan x+y+z toplamını çıkaracagız.
'''
a=input(" Bir sayı giriniz  ",   )
b=input(" İkinci sayıyı giriniz ",   )

carpim=int(a)*int(b)
print("carpim",carpim)
toplam=x+y+z
print("toplam",toplam)
sonuc=carpim-toplam
print(sonuc)
#y'nin x'e kalansız bölümü icin;

sonuc=y//x
print(sonuc)

#x+y+z'nin mod(3)'unu hesaplayalım

toplam=x+y+z
mod=toplam%3
print(mod)

#y'nin x.kuvveti nedir

sonuc=y**x
print(sonuc()
'''
#listeleri birbirine esitleyelim ve numbers listesindeki indeks daha fazla oldugu icin 
#y'yi bir dizi olaraka tanımlayalım.

x,y,z=2,5,107
numbers=1,5,7,10,6

x,*y,z=numbers
sonuc=z**3   #listeler esitlendiginde : x=1 y=5,7,10 z=6 degerini aldı
print(sonuc)
print(y)
#y degerlerinin toplamı
toplam=y[0]+y[1]+y[2]
print(" y degerleri toplamı = ", toplam)