#Girilen iki sayıdan hangisi büyük
'''
x=input(" Bir sayı giriniz" , )
y=input(" İkinci sayıyı giriniz ", )
result= (x>y)
print(result)
'''
#Kullanıcının girdiği iki vize(%30+%30) ve bir final notunun(%40) ortalamasını alıp sonuc notunu hesapla
#eger sonuc 50den yuksekse gecti degilse kaldı yazdır
'''
vize1=input(" Birinci vize notunuzu giriniz ",  )

vize2=input(" İkinci vize notunuzu giriniz ", )
final=input(" Final notunuzu giriniz ", )

ortalama=((int(vize1)*0.3)+(int(vize2)*0.3)+(int(final)*0.4))
print(" Ortalamanız = ",(ortalama))

if(ortalama>=50):
    print(" Gectiniz ")
elif(ortalama<50):
    print(" Kaldınız ")
'''
#Girilen bir sayının tek mi cift mi oldugunu yazdıralım
'''
sayi=input(" Bir sayı giriniz ", )
result=int(sayi)%2
if(result==0):
 print(" Girdiginiz sayı cifttir ")
elif(result!=0):
 print(" Girdiginiz sayı tektir")
'''
#Girilen bir sayının negatif,pozitif oldugunu yazdır
'''
sayi=input(" Bir sayı giriniz ", )
sayi=int(sayi)
if(sayi>0):
    print(" Girdiginiz sayı pozitifdir")
elif(sayi<0):
    print(" Girdiginiz sayı negatifdir")
elif(sayi==0):
    print(" Girdiginiz sayı sıfırdır")
'''
#Parola ve email bilgisi isteyip dogrulugunu kontrol edelim
'''
password="123456"
email="mbicici@gmail.com"

mail=input(" Mail adresinizi giriniz ", )
result=(mail==email)
print(result)
if(result==True):
    sifre=input(" Sifre giriniz ", )
    result=(sifre==password)
    print(result)
print(" Giris Basarılı ")
'''