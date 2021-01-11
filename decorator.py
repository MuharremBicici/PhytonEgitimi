import math              #Kütüphanaleri çağırdık
import time

def time_decorator(func):          #Zaman bilgisi için bir time decorator oluşturduk
    def inner(*args,**kwargs):     #Bir inner fonksiyon oluşturarak fonksiyonlara atayabileceğimiz inputları tanımladık
        start=time.time()          #Başlangıç zamanını tanımladık
        time.sleep(1)              #Zamanlamayı görebilmek için 1 saniye beklettik
        func(*args,**kwargs)       #Fonksiyonu çalıştırdık
        finish=time.time()         #Sonlanma zamanını tanımladık
        print("Fonksiyon "+str(finish-start)+"saniyede tamamlandı") #Fonksiyonun ne kadar sürede çalıştığını yazdırdık
    return inner

    
@time_decorator                     #üs alma fonksiyonu için time decoratoru cağırdık
def usalma(a,b):                    #Üs alma fonksiyonunu tanımladık
    return print(math.pow(a,b))

usalma(2,3)                        #örnek

@time_decorator                    #faktoriyel fonksiyonu için time decoratoru çağırdık
def faktoriyel(num):              
    print(math.factorial(num))

faktoriyel(6)                     #örnek,aynı işlemleri toplama ve alan hesaplama fonk.için de yaptık

@time_decorator
def toplama(a,b,c):
    print(a+b+c)

toplama(2,3,5)

@time_decorator
def alan(r):
    pi=3.14
    print("Alan ="+str(pi*r**2))

alan(3)

