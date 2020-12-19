#Sayılar listesindeki hangi sayılar 3'ün katı?
"""
sayilar=[1,3,5,9,12,19,21]
for sayi in sayilar:
   if(sayi%3==0) :
      print(sayi) # islemi sırayla listedeki tüm sayılara uygular.3.9.12.21 cıktısı verecektir.
"""
#Sayılar listesindeki sayıların toplamını hesaplayalım
"""
sayilar=[1,3,5,9,12,19,21]
toplam=0
for sayi in sayilar:
    toplam += sayi                 # "+=" ifadesi koyulan sayıları toplayarak ilerliyor
        print("Toplam : ",toplam)  # Sayılar toplana toplana ilerler.Cıktılardaki Son toplam tüm sayıların toplamıdır
"""
#Listedeki ürünlerin fiyatları toplamı?
#En fazla 5000 lira olan ürünler?
urunler=[
   {"name":"samsung s6","price":"3000"},
   {"name":"samsung s7","price":"4000"},
   {"name":"samsung s8","price":"5000"},
   {"name":"samsung s9","price":"6000"},
   {"name":"samsung s10","price":"7000"}
]
"""
toplam = 0
for urun in urunler:
   fiyat = int(urun['price'])
   toplam += fiyat
print('toplam ürün fiyatı: ', toplam)

for urun in urunler:
    fiyat=int(urun["price"])
    if fiyat<=5000:
        print(urun["name"])    
"""