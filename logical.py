#Girilen bir sayının 0-100 ile arasında olup olmadığını doğrulayınız
'''
sayı=input(" Bir sayı giriniz", )
sayı=int(sayı)
result=(sayı>0)and(sayı<100)
print(result)
'''
#Girilen bir sayının pozitif çift sayı olup olmadıgını dogrulayınız
'''
sayı=input(" Bir sayı giriniz ",  )
sayı=int(sayı)
result=(sayı>0)and(sayı%2==0)
print(result)
'''
#Email ve parola bilgileriyle giriş kontrolü yapınız
'''
email="mbicici@gmail.com"
password="123456"
mail=input(" Mail adresinizi giriniz ",  )
sifre=input(" Sifrenizi giriniz ",   )
result=(mail==email)and(sifre==password)
print(result)
'''
#Girilen 3 sayıyı büyüklük olarak karsılastırınız.
'''
sayı1=input(" Birinci sayıyı giriniz ", )
sayı2=input(" İkinci sayıyı giriniz ", )
sayı3=input(" Ucuncu sayıyı giriniz ", )
if((sayı1>sayı2)and(sayı2>sayı3)):
 print("sıralama ={}>{}>{}".format(sayı1,sayı2,sayı3))
elif((sayı1>sayı2)and(sayı3>sayı2))and(sayı1>sayı3):
 print("sıralama ={}>{}>{}".format(sayı1,sayı3,sayı2))
elif((sayı1>sayı2)and(sayı3>sayı2))and(sayı3>sayı1):
 print("sıralama ={}>{}>{}".format(sayı3,sayı1,sayı2))
elif((sayı3>sayı2)and(sayı3>sayı1))and(sayı2>sayı1):
 print("sıralama ={}>{}>{}".format(sayı3,sayı2,sayı1))
elif((sayı2>sayı3)and(sayı2>sayı1))and(sayı3>sayı1):
 print("sıralama ={}>{}>{}".format(sayı2,sayı3,sayı1))
elif((sayı2>sayı3)and(sayı2>sayı1))and(sayı1>sayı3):
 print("sıralama ={}>{}>{}".format(sayı2,sayı1,sayı3))
'''
#Kullanıcıdan iki vize(%60) bir final notu alıp ortalama hesaplayınız
 #ortalama>=50 ise gecti
 #ortalama>=50 olsa bile final notu en az 50 almalı
 #final>80 ortalamanın önemi olmadan gecti
'''
vize1=input(" Birinci vize notunuz = ",  )
vize2=input(" İkinci vize notunuz = ",  )
final=input(" Final notunuz = ", )
vize1=int(vize1)
vize2=int(vize2)
final=int(final)
ortalama=(vize1*0.3)+(vize2*0.3)+(final*0.4)
print("ortalama = ",ortalama)
if(((ortalama>=50) and (final>=50))or(final>=80)):
    print(" Tebrikler,dersi gectiniz... " )
else:
    print(" Dersi gecemediniz.. " )
'''
#Kullanıcın ad boy kilo bilgilerini alarak boy kilo endeksini hesaplayalım
#formul=kilo/boy uzunluk karesi
#Asagıdaki durumlara göre kisi hangi gruba girmektedir
#0-18.4 zayıf 18.5-24.9 normal 25-29.9 fazla kilolu 30-34.9 obezite
'''
isim=input(" Adınız : " , )
boy=input(" Boyunuz : " , )
kilo=input(" Kilonuz : " , )
boy=float(boy)
kilo=float(kilo)
boykiloendeksi=kilo/(boy**2)
print(" Adınız = {},Endeksiniz = {} ".format(isim,boykiloendeksi))
if(boykiloendeksi<18.5):
    print("Endeksiniz zayıf sınıfıyla eslesmistir.")
elif((boykiloendeksi>=18.5)and(boykiloendeksi<25)):
    print("Endeksiniz normal sınıfla eslesmektedir.")
elif((boykiloendeksi>=25)and(boykiloendeksi<30)):
    print("Endeksiniz fazla kilolu sınıfıyla eslesmektedir")
elif(boykiloendeksi>=30):
    print("Endeksiniz obezite sınıfıyla eslesmektedir")
'''


