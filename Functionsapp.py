#Gönderilen kelimeyi belirtilen kez ekranda gösteren fonksiyon
#1.yöntem
"""
def yazdir(a):              #Kelimeyi yazdıran bir fonksiyon tanımladık
    count=int(input("Kaç kez tekrar etsin : ")) #Kaç kez yazdıracağımızı kullanıcıdan aldık
    i=0
    while i<count: #while döngüsünü kullanarak yazdırdık
        i+=1
        print(a)
yazdir("input") #fonksiyonun içine yazacağımız string ifade input olarak aldığımız sayıda tekrar edecek 
"""
#2.yöntem
"""
def yazdir(a,b):    #fonksiyonu içinde iki ane input ifadeyle tanımladık.1.input:yazdıracağımız kelime
    i=0             #2.input : tekrar sayısı
    while i<b :     #while döngüsünü girilen tekrar sayısı kadar çevirerek kelimeyi ekrana yazdırdık
        i+=1
        print(a)
yazdir("anne",3)   
"""
#Kendine gönderilen sınırsız sayıda bir parametreyi listeye çeviren fonksiyon
"""
def makelist(*params):                          #Girdiğimiz parametreleri listenin içine yazdıran bir 
    print(params)                               #fonksiyon tanımladık.
makelist(10,20,30,"item",50,"python,",35,58,59) #"*" ifadesi parametreleri listeleme için kullanılır
                                                #"**" ifadesi ise dictionary yapısı için kullanılır
"""
#Gönderilen iki sayı arasındaki tüm asal sayıları bulan fonksiyon
"""
def asal(a,b):
    for sayi in range(a,b+1): #a sayısı ile b sayısının arasındaki tüm sayılar için işlem yapıyoruz
        if sayi>1:  
            for i in range(2,sayi): #2den sayiya kada rolan tüm sayılar için
                if (sayi%i==0):     #sayının aralıktaki herhangi bir sayıya modu 0'a eşitse(bölünüyorsa)
                    break           #işlemi sonlandırıyoruz
            else:       #sayinin aralıktaki herhangi bir sayıya modu 0a eşit olmuyorsa sayıyı yazdırıyoruz.
                print(sayi)
asal(3,23)
"""
#Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde yazdıran program
"""
def tambolen(a):          #input olarak bir a sayısı giriliyor
    tambolenler=[]        #a sayısını tam bolen sayıları bu listeye ekleyeceğiz
    for sayi in range(2,a+1): #2 ile a sayısı DAHİL(a+1 yazmamızın sebebi) arasındaki tüm sayılar için
        if(a%sayi==0):       #a"nın bu sayılardan modu 0"a eşit olanları(tam bolenlerini)
            tambolenler.append(sayi)  #tambolenler listesine ekledik
    return tambolenler       #listeye geri göndürdük

print(tambolen(17)) #tambolen fonksiyonunu calıstırıp cıktıları ekrana yazdırdık 
"""

