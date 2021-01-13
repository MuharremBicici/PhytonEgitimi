import os
"""
result=dir(os)
print(result)                          #os kütüphanesinde kullanabileceğimiz metdoları inceleyebilirsiniz.

"""

result=os.name
print(result)                          #işletim sistemi yazdırılır windows için :nt

result=os.getcwd()
print(result)                          #Şu an etkin olarak çalıştığımız dosyanın hangi dizinde olduğunu gösterir

os.mkdir("newdirectory")               #Etkin dizinde yeni bir dosya oluşturur.
os.rename("newdirectory","yeniklasor") #Dosya ismini değiştirme,
os.removedirs("yeniklasor")            #Dosyayı siler
os.listdir()                           #Mevcut dizindeki dosyaları listeler
os.listdir("C:\\")                     #C dosyasındaki klasorleri listeler


for dosya in os.listdir("C:\\Users\MUHARREM BİÇİCİ\Desktop\python_education"):
    if dosya.startswith("D"):
        print(dosya)                  #Python education dosyası içerisinde D ile başlayan dosyaları yazdırdık


#os.stat("dosyaismi")                  #İnput olarak ismi verilen dosyanın özellikleri(boyutu,kayıt tarihi vs. listelenir)
"""
stat metodunu daha iyi öğrenmek için bir örnek yapacağız burada dikkat edilmesi gerekn birşey var.
Burada örneğin dosyanın oluşturulma zamanını ekrana getirdiğimizde karşımıza saniye cinsinden yüksek bir
sayı gelecektir.Bunu datetime moduluyle tarih bilgisine çevireceğiz.

"""
#***stat metdou****
import datetime
result=os.stat("Fonksiyonlar")
print(result)                        #Burada fonksiyonlar dosyası ile ilgili bilgiler ekrana yazdırılır.

result1=datetime.datetime.fromtimestamp(result.st_ctime)
#dosya bilgilerinden gelen oluşturulma zamanı bilgisi(st_ctime(sayısal bir değer gelir)) datetime.fromtimestamp metodu kullanılarak tarih bilgisine çeviriliyor.
print(result1)

result2=datetime.datetime.fromtimestamp(result.st_atime)   #Dosyaya Son erişilme tarihi
print(result2)


result3=datetime.datetime.fromtimestamp(result.st_mtime)   #Dosyanın son değiştirilme tarihi
print(result3)

#os.system("notepad.exe") #içine ismi yazılan dosya çalışır

#path metodu
result=os.path.abspath("date.py")  #Dosyanın tam konumunu verir
print(result)

result=os.path.dirname(result)     #input olarak tam konumu verilen dosyanın yolunu verir
print(result)

result=os.path.exists("date.py")   #Çalışılan dizinde input olarak adı verilen dosya var mı? True ya da False sonuç verir
print(result)

