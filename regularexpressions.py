import re
"""
result=dir(re)          #re sınıfında kullanabileceğimiz metodları öğrenmek için inceleyebilirsiniz
print(result)
"""
mesaj="Python Course : Online course for 40 hours"

#re.findall()
"""
result=re.findall("Python",mesaj)  #Mesajın içinde Python ifadesini arar varsa yazdırır.
print(result)
"""
#re.split()
"""
result=re.split(" ",mesaj)         #Mesaj her boşluk ifadesinden ayrılır
print(result) 
"""
#re.sub()
"""
result=re.sub(" ","-",mesaj)       #Mesajdaki her boşluk ifadesi yerine - koyar
print(result)
"""
#re.search()
"""
result=re.search("Python",mesaj)   #Mesajdaki ilk "python" ifadesini ve bulunduğu yeri(span:) ekrana yazdırır
print(result)
result1=result.span()               #Mesajın içindeki ilk "python" ifadesinin konumunu yazdırır
print(result1)
result2=result.start()             #Mesajın içindeki ilk Python ifadesinin başladığı indeksin numarasını yazdırır
print(result2)
result3=result.end()               #Mesajın içindeki İlk Python ifadesinin bittiği indeksin numarasını yazdırır
print(result3)
result4=result.group()             #Mesajın içinde aradığımız ifadeyi ekrana yazdırır
print(result4)
"""
#[]
"""
result=re.findall("[abc]",mesaj)  #mesajın içinde a,b,veya c aradık.
print(result)
result=re.findall("[a-e]",mesaj)  #mesajın için a,b,c,d,e aradık
print(result)
result=re.findall("[1-5]",mesaj)  #mesajın içinde 1,2,3,4,5 aradık
print(result)
result=re.findall("[0-39]",mesaj) #mesajın içinde DİKKAT :0,1,2,3,9 aradık. 0dan 39a kadar sayı aramadık
print(result)
result=re.findall("[^abc]",mesaj) #mesajın içinde a,b,c olmayan bütün elemanları aradık
print(result)
"""
#. Herhangi bir karakteri belirtir
"""
result=re.findall("...",mesaj)    #Bütün 3 karakterli ifadeleri boşluklar dahil yazdırır.(Bir nevi mesajı 3 karakterlik dizelere bölerek yazdırır)
print(result)
"""
#^ Belirtilen karakterle başlıyormu
"""
result=re.findall("^a",mesaj)     #mesaj a ile başlıyormu True ise bir liste için a yazdırır
print(result)
"""
#$ Belirtilen karakterle biitiyormu
"""
result=re.findall("hours$",mesaj) #mesaj hoursla bitiyormu True ise bir liste içinde hours yazdırır.
print(result)
"""
#* Bir karakterin sıfır yada daha fazla sayıda olup olmadığını kontrol etmemizi sağlar
"""
result=re.findall("th*o",mesaj)  #t ve o arasında h var mı 
print(result)
"""
#+ Bir karakterin en az bir tane olup olmadığını kontrol eder
"""
result=re.findall("hour+s",mesaj) #hou ile s arasında en az bir tane r olan ifade varmı
print(result)
"""
#? Bir karakterin sıfır ya da bir kez olup olmadığını kontrol eder
"""
result=re.findall("hour?s",mesaj) #hou ile s arasında 0 veya 1 kez r ifadesi varmı(hous olur,hours olur,hourrs olmaz)
print(result)
"""
#{} Karakter sayısını kontrol eder
"""
result=re.findall("a{2}",mesaj)  #içinde aa ifadesi geçen bir ifade varmı
print(result)
result=re.findall("[0-9]{2}",mesaj) #iki basamaklı sayı varmı
print(result)
"""
#/ or işareti a yada b varmı: a/b
#() gruplamak için kullanılır
"""
(a,b,c)xz : axz,bxz,cxz gibi ifadeler varmı
"""
#\Özel karakterleri aramamızı sağlar mesela : \$a(dolar işaretinden sonra a gelen bir bölüm varmı)
#\A Belirtilen karakter mesajın başında mı mesela : \APython mesaj pythonla başlıyorsa true
#\Z Belirtilen karakter mesajın sonunda mı mesela : \A.com mesaj .com'la bitiyorsa true
#\b Belirtilen karakter Kelimenin başında mı mesela :
"""
\bthe  --- kelime the ile başlıyormu(baslıyorsa o kelimeyi yazdırır)
the\b  ---kelime the ile bitiyormu(bitiyorsa yazdırır)
"""
#\D ==[^0-9] ikiside aynı anlama gelir,rakam olmayan ifadeleri arar
#\d rakamları arar ==[0-9]
#\s boslukları arar
#\w alfabetik karakterler,rakamlar veya altcizgi gibi ifadeleri arar




