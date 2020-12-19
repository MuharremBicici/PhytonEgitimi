#Sayılar listesini while ile ekrana yazdırın
"""
sayilar=[1,3,5,7,9,12,15,21]
i=0
while i<7:
    i+=1
    print(sayilar[i])
    
print("Liste bitti")
"""
#Baslangıc ve bitis degerlerini kullanıcıdan alarak aradaki tüm tek sayıları yazdıralım
"""
baslangic=input(" Baslangic degeri : ")
bitis=input(" Bitis degeri :  ")
bas=int(baslangic)
bit=int(bitis)
while bas<bit:
    bas+=1
    print(bas)
"""
#1 ile 100 arasındaki sayıları azalan bir şekilde yazdır
"""
i=100
while i>1:
    i-=1
    print(i)
"""
#Kullanıcıdan alınacak 5 sayıyı ekranda sıralı bir şekilde yazdıralım
numbers=[]
"""
i=0
while i<5:
    sayı=int(input("sayı : "))
    numbers.append(sayı) #sayıları listeye ekledik
    i+=1
    numbers.sort() #listedeki sayıları sıraladık
    print(numbers)
"""
#Kullanıcıdan alacağımız sınırsız ürün bilgisini ürünler listesi içinde saklayalım
# ürün sayısını kullanıcıya soracagız
# dictionary yapısı name,prize seklinde olacak
# ürün ekleme işlemi bittiğinde while ile ekrana yazdıracagız
"""
urunsayısı=int(input("ürün sayısı : ", ))
urunler=[]
i=0
while i<urunsayısı :
    urun=input("Name :  ,Fiyat : ")
    i+=1
    urunler.append(urun)
    print(urunler)
"""

     