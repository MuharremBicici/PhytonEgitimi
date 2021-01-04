import modul                     #modul.py dosyasında tüm bilgileri ve işlemleri çağırdık.Yani kendi oluşturduğumuz kütüphaneden faydalanıyoruz.
import random                    #Phyton bünyesinde zaten mevcut olan random kütüphanesini çağırdık
kisi=modul.persons["person1"]    #modul.py dosyasındaki kişilerin bilgilerini kullanarak kişileri tanımladık
kisi2=modul.persons["person2"]
kisi3=modul.persons["person3"]
pozisyon= random.choice(modul.positions)  #modul.py dosyasındaki pozisyonlardan rastgele bir tanesini seçtik 
pozisyon2=random.choice(modul.positions)
pozisyon3=random.choice(modul.positions)
print(f"{kisi} kişisi {pozisyon} pozisyonuna atanmıştır") #rastgele seçilen pozisyonlara kişileri atadık.
print(f"{kisi2} kişisi {pozisyon2} pozisyonuna atanmıştır")
print(f"{kisi3} kişisi {pozisyon3} pozisyonuna atanmıştır")



    



