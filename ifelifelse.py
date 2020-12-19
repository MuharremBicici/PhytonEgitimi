#Kullanıcıdan isim yaş ve eğitim bilgileri isteyipehliyet alabilme durumunu kontrol ediniz.
#Yas 18den küçük olmamalı eğitim en az lise olmalı
'''
print(" Ehliyet durumu sorgulama ekranına hosgeldiniz ")
isim=input(" İsminiz = " ,  )
yas=input(" Yaşınız = " ,   )
egitimdurumu=input(" Egitim seviyeniz =  " ,  )
yas=int(yas)
if(yas>=18)and((egitimdurumu=="lisans")or(egitimdurumu=="lise")or(egitimdurumu=="önlisans")or(egitimdurumu=="yükseklisans")):
    print("Tebrikler {}.Ehliyet alma yetkinliğiniz bulunmaktadır".format(isim))
else:
    print("Sayın {},Ehliyet alma yeterliliğine sahip değilsiniz".format(isim))
'''
#Bir öğrencinin iki yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre aşagıdaki tabloyla kıyaslayarak
#not durumunu yazdıralım
#0-24 : 1
#25-44 : 2
#45-54 : 2
#55-69 : 3
#70-84 : 4
#85-100 : 5
'''
print("Not durumu sorgulama ekranına hoşgeldiniz")
yazılı1=input(" Birinci yazılınızı giriniz : ",  )
yazılı2=input(" İkinci yazılınızı giriniz : ",  )
sozlu=input(" Sozlu notunuzu giriniz : ",  )
yazılı1=int(yazılı1)
yazılı2=int(yazılı2)
sozlu=int(sozlu)
ortalama=(yazılı1+yazılı2+sozlu)/3
if ortalama<25:
    print( " Notunuz : 0 " )
elif (ortalama>=25)and(ortalama<45):
    print(" Notunuz : 1 ")
elif (ortalama>=45)and(ortalama<55):
    print(" Notunuz : 2 ")
elif(ortalama>=55)and(ortalama<70):
    print(" Notunuz : 3 ")
elif(ortalama>=70)and(ortalama<85):
    print(" Notunuz : 4 ")
else:
    print(" Notunuz : 5")
'''
#Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki nilgilere göre hesaplayınız.
#1.bakım : 1 yıl
#2.bakım : 2 yıl
#3.bakım : 3 yıl
'''
gun=input("Aracınız trafıge kac gun once cıktı : " ,  )
gun=int(gun)
if gun<=365:
    print(" Aracınız 1.bakım yılındadır ")
elif(gun>365)and(gun<=730):
    print(" Aracınız 2.bakım yılındadır ")
elif(gun>730)and(gun<=1095):
    print(" Aracınız 3.bakım yılındadır ")
else:
    print("Aracınız servis bakım sürecini doldurmuştur. ")
''' 