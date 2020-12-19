#dairenin alanını ve cevresini hesaplama pi=3,14 r=kullanıcıdan istenecek

r=input("yaricap: ")
pi=3.14
r=float(r)  #string alınan degeri floata cevirip islem yaptik

print(type(r))

daireninalanı=pi*r*r
dairenincevresi=2*pi*r

daireninalanı=int(daireninalanı)
dairenincevresi=int(dairenincevresi) #float olan degeri int e cevirdik tamsayı olarak yazdırdık

print(daireninalanı)
print(dairenincevresi)