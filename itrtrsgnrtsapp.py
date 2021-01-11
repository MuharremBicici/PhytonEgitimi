#Iterators
"""
#Phytonda gezinilebilen(iterable) nesne olarak kullanılabilen bir nesneye iterable obje denir.Bu temel olarak
nesnedeli dizinin gezilebileceğini ilerlenebileceğini gösterir.Python iteratorleri sayılabilecek değer içeren
bir objedir.Bir objedeki değerler iterator kullanılarak aktarılabilir.Örnekle daha iyi anlayalım :

isimler=["Muharrem","Ali","Mustafa"]
iterator=iter(isimler)  
print(next(iterator))    #Çıktı Muharrem
print(next(iterator))    #Çıktı Ali
print(next(iterator))    #Çıktı Mustafa 
"""

liste=[1,2,3,4,5]
iterator=iter(liste)  #liste iterable bir nesnedir.Yani listeler için bu yöntem tanımlıdır
while True:
    try:
        element=next(iterator)   #Listedeki her eleman next metoduyla tek tek yazdırılacak
        print(element)
    except StopIteration:        #Listedeki elemanların tamamı yazdırıldığında StopIteration hatası verecek ve burada yazdurma duracak
        break


#Generators
"""
Generatorler Phytonda iterable objeler oluşturmak için kullanılan objelerdir ve bellekte yer tutmazlar
Yani burada aldığımız değerleri bir listeye kaydetip yer kaplamak zorunda değiliz.Yield metodu kullanılarak
değerler anlık olarak üretilirler ve kayıt altında tutulmazlar.Şimdi generator kullanmadan bir kare alma 
fonksiyonu tanımlayalım


def kareleri_al():                #Burada sonuçlar bir listeye ekleniyor yani bellekte yer tutuyor
    sonuclar=[]
    for i in range(1,6):
        sonuclar.append(i**2)
print(kareleri_al)

#Bunun yerine bir generator kullanırsak:
def karelerini_al():            #Burada yield metoduyla değerler anlık olarak üretilir ve kaydedilmez
    for i in range(1,6):        #Farkettiğiniz gibi değerleri kaydeden bir liste yok
        yield i**2
generator=karelerini_al()
print(generator)

"""
generator=(i**3 for i in range(5)) #0dan 5 e kadar olan sayıları tek tek for döngüsüne sokup küpünü alıyoruz
for i in generator:
    print(i)                       #Sonra sonuçları ekrana yazdırıyoruz


#Örnek
class myNumbers:                        #myNumbers isimli bir sınıf tanımladık
    def __init__(self,start,stop):      #init metoduyla bir fonksiyon tanımladık ve input olarak başlangıç ve bitiş sayılarını verdik
        self.start=start
        self.stop=stop
    def __iter__(self):                 #iter metoduyla her birini çağırıyoruz
        return self
    def __next__(self):                 #next metoduyla bir sonraki objeye geçecek fonksiyonu tanımladık
        if self.start<=self.stop:       
            x=self.start                #Başlangıç sayısından bitiş sayısına kadar 1er 1er artarak objeleri çağırıyoruz
            self.start+=1       
            return x
        else:                           
            raise StopIteration

list=myNumbers(10,20)                  #Burada bir örnek yaptık
for i in list:
    print(i)
