#liste=["1","2","5a","10c","11c","12"]
#Liste elemanları içindeki sayısal değerleri yazdıralım
"""
for x in liste:        #Bir for döngüsü oluşturduk.
    try:
        result=int(x)  #Liste elemanı bir integer değer olduğunda yazdırıyoruz
        print(result)
    except ValueError: #Liste elemanı integer olmazsa yazdırmadan devam ediyoruz.
        continue
"""
#kullanıcı q değerini girmedikçe aldığımız her inputun sayı olduğundan emin olunuz .Aksi halde hata mesaji yazdırınız.
"""
x=input("Bir sayı giriniz : ")
q=quit
if not x=="q":                              #Girilen input "q" olmadığında
    try:
        x=int(x)                            #Ve girilen input bir sayı olduğunda
        print(f"Girdiğiniz sayı {x}' dir.") #Sayıyı ekrana yazdırıyoruz
    except ValueError:                      #İnput bir sayı değilse hata mesaji gönderiyoruz.
        print("Yanlış giriş yaptınız.Lütfen bir sayı giriniz ")
else:
    print("Uygulama sonlandırıldı")         #Girilen input "q" olduğunda ise uygulamayı sonlandırıyoruz.
"""
#Girilen parola içinde türkçe karakter varsa hata veren programı yazalım 
"""
import re          #"re" import ettiğimiz build in bir search kütüphanesi(karakter aramak için kullandık)
print("Merhaba parola oluşturma ekranına hoşgeldiniz.Lütfen Türkçe karakter kullanmayınız..")
password=input("Parolanızı giriniz :",)
def checkPassword(psw):              #Şifre kontrolü yapacak bir fonksiyon tanımladık.
    if re.search("İ",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.") #Fonksiyon Türkçe karakterlerle karşıla-
    elif re.search("Ş",psw):                                     #şırsa hata verecek.
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("Ğ",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("ğ",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("Ü",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("ü",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("Ç",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("ç",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("Ö",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("ö",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("ş",psw):
        raise Exception("Parola Türkçe karakter içermemelidir.")
    elif re.search("\s",psw):                                  #Şifrede boşluk bırakılmaması için
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Parola {psw} geçerlidir.")
try:
    checkPassword(password)
except Exception as ex:       #Eğer şifrede bir hata olursa hata mesajı ekrana yazdırılıyor.
    print(ex)
else:
    print("Parola geçerlidir") #Sorun olmazsa ise parola geçerlidir yazdırılıyor.
finally:
    print("Parola oluşturma işlemi sona ermiştir.")
"""
#Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları veriniz
""" 
import math          #factorial fonksiyonunu kullanabilmek için math kütüphanesini import ettik.
def faktöriyel(x):   #faktoriyel işlemini yapacak fonksiyonu tanımladık.
    if x>0:          #Sayı 0'dan büyükse hesaplama işlemi yapılıp ekrana yazdırılıyor.
        result=math.factorial(x)
        print(f"Sonuç : {result}")
    else:           #0'dan küçük bir sayı girilirse ekrana hata mesajı yazdırılıyor.
        raise Exception("O'dan büyük bir sayı giriniz")

try:
    faktöriyel() #Burada fonksiyonun inputuna sayı girerseniz döngüyü çalıştırıyor.
except NameError: #Fonksiyonun inputuna eğer bir sayı girmezseniz de hata mesajı ekrana yazdırılıyor.
    print("Bir sayı girmeniz gerekmektedir.")
    """
#faktöriyel(5)
#faktöriyel(-3)
#faktöriyel(abc) bunları deneyip görebilirsiniz..



    

    

    


