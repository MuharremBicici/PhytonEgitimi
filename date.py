"""
BU uygulamaları yazarak denemek isterseniz dosya adını datetime.py koymayın.Çünkü öyle koyulursa
program çalışmakta sorun yaşıyor.

"""
from datetime import datetime
"""
result=dir(datetime)
print(result)          #datetime modulu içerisinde kullanabileceğimiz metodları yazdırdık.İnceleyebilirsiniz
"""


now=datetime.today() 
print(now)            #2021-01-12 00:07:47  

result=datetime.ctime(now)
print(result)        #Tue Jan 12 00:07:47 2021

result=datetime.strftime(now,"%Y") #yılı yazdırır :2021
print(result)

result=datetime.strftime(now,"%X") #saati yazdırır 00:10:52
print(result)

result=datetime.strftime(now,"%d") #ayın kaçıncı gümü olduğu yazdırılır : 12
print(result)

result=datetime.strftime(now,"%A") #gün string ifade olarak yazdırılır :Tuesday
print(result)

result=datetime.strftime(now,"%B") #ay string olarak yazdırılır:January
print(result)

result=datetime.strftime(now,"%Y %B %d") #İkinci indekste hangi bilgiyi istersek yazdığımız sırada ekrana gelir
print(result)                            #2021 January 12 



time="13 September 1995 hour 15:30:46"
dogumtarihi=datetime.strptime(time,"%d %B %Y hour %H:%M:%S")
yıl=dogumtarihi.year
print(yıl)            #1995 yazdırır

ay=dogumtarihi.month
print(ay)             #9(september) yazdırır :9

"""
Yukarıda elde ettiğimiz now objesinde kullandığımız bütün metodlar burada da kullanılabilir.
Çünkü String ifade olarak girilen time bilgisini strptime metodunu kullanarak datetime modulune
uygun hale getirdik ve eşleşmeleri yaptık.Artık sistem string değerlerin hangi değere karşılık 
geldiğini algılayabilir.

"""

birthday=datetime(1999,6,6)
print(birthday)

result=datetime.timestamp(birthday) #Burada bilgisayarın doğuşunu 1970.01.01 kabul edip bilgisayarın doğuşundan birthday tarihine kadar olan sürede geçen saniyeyi hesaplıyor.
print(result)   #Saniye cinsinden süre hesaplar


result=datetime.fromtimestamp(result)
print(result)  #Saniye cinsinden geçen zamanı yeniden tarihe çeviriyor.Yani sonuç birthday'i verecek

result=now-birthday
print(result)  #Gün+saat cinsinden yaşı hesaplar


from datetime import timedelta
result=dir(timedelta)          #Timedelta sınıfına ait metodları incelemek isterseniz bakabilirsiniz.
print(result)

result=now+timedelta(days=10)   #Yukarda aldığımız anlık zaman bilgisine gün olarak 10 gün ekledik
print(result)

result=now-timedelta(days=365) #Yukarda aldığımız zaman bilgisinden 365 gün çıkardık.
print(result)