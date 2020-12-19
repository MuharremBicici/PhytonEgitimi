#  1.ögrenci icin
print("Merhaba,kayıt ekranına hosgeldiniz")  #3 öğrencicic bilgilerini alıp users listesine kaydettik
okulnumarası1=input(" okul numaranız ", )
adı1=input(" adınız ", )
soyadı1=input(" soyadınız ", )
mailadresi1=input(" mail adresiniz ", )
print("Kayıt islemi tamamlanmıstır")
#2.öğrenci icin
print("Merhaba,kayıt ekranına hosgeldiniz")
okulnumarası2=input(" okul numaranız ", )
adı2=input(" adınız ", )
soyadı2=input(" soyadınız ", )
mailadresi2=input(" mail adresiniz ", )
print("Kayıt islemi tamamlanmıstır")
#3.öğrenci icin
print("Merhaba,kayıt ekranına hosgeldiniz")
okulnumarası3=input(" okul numaranız ", )
adı3=input(" adınız ", )
soyadı3=input(" soyadınız ", )
mailadresi3=input(" mail adresiniz ", )
print("Kayıt islemi tamamlanmıstır")

#liste 

users={
    "okulnumarası1":{
     "adı": adı1,
     "soyadı": soyadı1,
     "mailadresi": mailadresi1
}
   ,"okulnumarası2":{
       "adı": adı2,
       "soyadı": soyadı2,
       "mailadresi": mailadresi2
   }     
    ,"okulnumarası3":{
        "adı": adı3,
        "soyadı": soyadı3,
        "mailadresi":mailadresi3
    }    
}

okulno=input(" okul numaranızı giriniz ", ) #Kullanıcının girdiği okul numarasına sahip öğrencinin
                                            #bilgilerini yazdırdık
if okulno==okulnumarası1 :
 print(users ["okulnumarası1"])

elif okulno==okulnumarası2 :
 print(users ["okulnumarası2"])

elif okulno==okulnumarası3:
 print(users ["okulnumarası3"])

else:
    print("kayıt bulunamadı")


