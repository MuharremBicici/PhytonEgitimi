names=["ali","Yağmur","Hakan","Deniz"]
years=[1982,1986,1995,1996]

#1
names.append("Cenk") #listeye cenk'i de ekledik.
print(names)
#2
names.insert(0,"sena") #listenin 0. indeksine yani başına senayı ekledik
print(names)
#3
names.remove("Deniz") #Deniz'i listeden çıkardık
print(names)
#4
names=["Ali","Yağmur","Hakan","Deniz"]
index=names.index("Deniz") #Deniz kaçıncı indekste?
print(index)
#5
result=names.__contains__("Ali") #Listede "Ali" var mı?
print(result)
#6
names.reverse() #Listteyi ters çevirdik
print(names)
#7
names.sort() #Orjinal listenin sıralamalarını değistirdik
print(names)
#8
years.sort()
print(years)
#9
str="chevrolet dacia"
str=str.split()     #String ifadeyi boşluktan ayırarak iki endeksi olan bir listeye çevirdik
print(str)
#10
result=max(years) #en büyük yılı yazdırdık
print(result)
result=min(years) #en küçük listeyi yazdırdık
print(result)
#11
print(years.count(1998)) #listede kaç tane "1998" ifadesi var?
#12
years.clear() #listenin içindekileri sildik
print(years)
#13
bir=input("Bir marka giriniz  ",  )
iki=input("farklı bir marka giriniz  ",  )
üc=input("farklı bir marka giriniz  ",  )
list=[bir]+[iki]+[üc]  #Kullanıcıdan aldığımız ifadeleri liste içinde yazdırdık
print(list)
