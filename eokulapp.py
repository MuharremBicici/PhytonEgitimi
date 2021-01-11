print("E-Okul uygulamasına hoşgeldiniz")

def not_hesapla(satir):         #Öncelikle bir not hesaplama ve puanlama fonksiyonu oluşturuyoruz.
    satir=satir[:-1]            #Satirlari birbirinden ayırmak için
    liste=satir.split(":")      #Satir içerisindeki metni : ifadesinden ayırıyoruz be liste olarak ayırıyoruz
    ogrenciadı=liste[0]         #Listenin 0.indeksinde öğrenci adları var
    notlar=liste[1].split(",")  #1.indekste ise notlar virgülden ayrılmış bir şekilde bulunuyor

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not1+not2+not3)/3
    if ortalama>90:
        harf="AA"
    elif ortalama<=90 and ortalama>80:
        harf="BA"
    elif ortalama<=80 and ortalama>70:
        harf="BB"
    elif ortalama<=70 and ortalama>60:
        harf="CB"
    elif ortalama<=60 and ortalama>50:
        harf="CC"
    elif ortalama<=50 and ortalama>45:
        harf="DC"
    elif ortalama<=45 and ortalama>40:
        harf="DD"
    else:
        harf="FF"
    return ogrenciadı+":"+harf+"\n"

def ortalamaları_oku():   #Notları okumak için tanımladığımız fonksiyon
    with open("Sınav_notları.txt","r",encoding="utf-8")as file: #Sınav notları dosyasını okuma(r) amaçlı açıyoruz."utf-8" ifadesi türkçe karakterler için
        for satir in file:
            print(not_hesapla(satir))  #Not hesapla fonksiyonuna sınav notlarındaki her satırı gönderiyoruz

def not_gir():        #Not girmek için oluşturduğumuz fonksiyon
    adı=input("Öğrenci Adı : ")
    soyadı=input("Öğrenci Soyadı : ")
    not1=input("Birinci Sınav Notu : ")
    not2=input("İkinci Sınav Notu : ")
    not3=input("Üçüncü Sınav Notu : ")
    with open("Sınav_notları.txt","a",encoding="utf-8")as file: #Sınav notları dosyasına bilgileri kayıt ediyoruz.Eğer sınav notları dosyası yoksa dosya oluşturuluyor."a" dosyayabilgi eklemek için(append)
        file.write(adı+" "+soyadı+" "+":"+not1+","+not2+","+not3+"\n")
    
def notları_kaydet():   #Girilen notları kaydetmek için kullandığımız fonksiyon
    with open("Sınav_notları.txt","r",encoding="utf-8")as file: #Önce sınav notları dosyasını okuma amaçlı açıyoruz.
        liste=[]
        for i in file: #For döngüsüyle hesaplanan notları oluşturduğumuz listeye ekliyoruz.
            liste.append(not_hesapla(i))
        with open("Sonuçlar.txt","a",encoding="utf-8")as file2:  #Sonra sonuçlar txt dosyasına notları ekliyoruz("a"(APPEND)).Eğer öyle bir dosya yoksa kod çalıştığı anda dosya oluşacak
            file2.write(i)

while True:
    islem=int(input("1-Notları oku\n2-Not gir\n3-Notları kaydet\n4-Çıkış\n")) #İşlem menüsünü oluşturduk \n alt satıra doğru menüyü yazdırmak için

    if islem==1:                 #Kullanıcın isteğine göre fonksiyonlar çağrılıyor.
        ortalamaları_oku()
    elif islem==2:
        not_gir()
    elif islem==3:
        notları_kaydet()
    else:
        print("Çıkış başarılıdır.")
        break

#Deneme yapmak isterseniz notları girdikten sonra kaydetmeyi unutmayın çünkü kaydetmezseniz silinir.