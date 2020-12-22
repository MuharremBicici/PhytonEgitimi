muharrembicici={
    "name":"Muharrem Bicici",  #hesap bilgilerini dictionary olarak oluşturduk
    "hesapNo":"10711453",
    "bakiye":11300,
    "ekHesap":2500
}
mustafasandal={
    "name":"Mustafa Sandal",
    "hesapNo":"14531071",
    "bakiye":5700,
    "ekHesap":1000
}
def paraCekme(hesap,miktar):                #Para çekme fonksiyonunu oluşturduk.1.parametre:hesap bilgisi
    print(f"Merhaba {hesap['name']}")       #2.parametre:yatırılacak tutar
    if (hesap["bakiye"]>=miktar):           #Bakiye yeterliyse ;para çekme işlemi onaylanıyor.
        hesap["bakiye"]-=miktar
        print(f"Sayın{hesap['name']},para cekme talebiniz başarılıdır.")
        bakiyeSorgulama(hesap)
    
    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]    #Bakiye yeterli değilse ek hesap bakiyesine bakıyoruz
        if toplam>=miktar: #Ek hesap bakiyesi ile birlikte miktar karşılanabiliyorsa ek hesap kullanım onayı isteniyor.
            print(f"{hesap['hesapNo']} numaralı hesabınızın bakiyesi yetersizdir.")
            ekhesapSorgulama=int(input("Ek hesap kullanmak için 1'i tuşlayınız : "))#Ek hesap kullanımı onayı
            if(ekhesapSorgulama==1):      #Kullanıcı ek hesap kullanımına onay verirse para çekme işlemi onaylanıyor.
                hesap["ekHesap"]=toplam-miktar  
                hesap["bakiye"]=0 #Hesap bakiyesinin tamamı kullanılmadan ek hesapdan para çekilemez.
                print(f"Sayın {hesap['name']},para cekme talebiniz başarılıdır.")
                bakiyeSorgulama(hesap)
            else:
                print("İşleminiz sonlandırılmıştır.")
        else:
            print("Bakiyeniz yetersizdir..")

def bakiyeSorgulama(hesap): #Bakiye sorgulama fonksiyonunu tanımladık ve bakiye bilgisini yazdırdık.
    print(f" Merhaba sayın {hesap['name']}.{hesap['hesapNo']} numaralı hesabınızın {hesap['bakiye']} TL bakiyesi vardır.Ayrıca {hesap['ekHesap']} TL ek hesap bakiyeniz vardır.")
     
def paraYatirma(hesap,miktar): #Para yatırma fonksiyonunu tanımladık.1.parametre :hesap bilgisi 2.parametre : miktar
    print(f"Merhaba {hesap['name']}")
    hesap["bakiye"]+=miktar #yatırılan tutarı bakiyeye ekledik
    print("Para yatırma işleminiz başarıyla gerçekleştirilmiştir ")
    bakiyeSorgulama(hesap)

### Burada referans türünde bir yapı kullandığımız için fonksiyon içerisinde gerçekleşen değişimler
### hesap bilgilerine yansır.
paraYatirma(muharrembicici,10000)
paraCekme(muharrembicici,22000)
#Bu denemelerde de görebileceğimiz gibi hesabımıza önce 10000 lira yatırdık ve yeni bakiyemiz :21300 tl oldu
#Ardından 22000 lira çektik ve 21300 tl hesaptan,700 tl ise ek hesaptan çekildi.
#Yani bakiyemiz fonksiyonun içerisindeki işlemlere göre güncellendi.