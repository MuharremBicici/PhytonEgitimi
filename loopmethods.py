#Rastgele seçilen bir sayıyı bylmaya çalıştığımız bir oyun tasarlayalım
"""
import random                    #Rastgele bir sayı elde etmek içim random kütüphanesini çağırıyoruz
sayı=random.randint(1,100)       #rastgele bir integer çağırıyoruz
can=int(input("Kaç tahmin hakkınız olsun istersiniz? : ", ))    #Tahmin haklarımız
puan=100
while can>0 :
    can-=1
    puan-=10
    tahmin=int(input(" 1-100 arasında bir sayı giriniz : "))
    if tahmin==sayı:
        print("Tebrikler sayıyı buldunuz.")
        print("Puanınız :" ,puan)
        break
    elif tahmin<sayı :
        print("Daha büyük bir sayı giriniz")
        if can==0:
            print("Haklarınız bitmiştir")
    elif tahmin>sayı:
        print("Daha küçük bir sayı giriniz")
        if can==0:
            print("Haklarınız bitmiştir")
    
 """
 #Girilen bir sayının asal sayı olup olmadığını gösteren program
"""
sayi=int(input(" Bir sayı giriniz : "))
asalmi=True 

if sayi==1:
    asalmi=False
for i in range(2,sayi):   #2den sayıya kadar olan sayılar için
    if sayi%i==0:         #Girilen sayı diğer sayılara bolunuyosa asal değil
        asalmi=False
        break
if asalmi:
    print("sayi asal sayıdır")
else:
    print("Sayı asal sayı değildir")
"""
    
        

    
