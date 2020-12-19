#1
arabalar="bmw mercedes opel mazda".split() #Her boşluğun indexleri birbirinden ayırdığını belirttik.
print(arabalar)
#2
print(len(arabalar)) #indexs sayısını yazdırdıl
#3
print(arabalar[0]) #0. vce 3. indeksi yazdırdık
print(arabalar[3]) 
#4
arabalar="bmw mercedes opel mazda"
arabalar=arabalar.replace("mazda","toyota") #Mazdanın yerine listeye toyotayı ekledik
print(arabalar)
#5
arabalar="bmw mercedes opel mazda".split() #"mercedes" arabalar listesinde varmı?
isFound="mercedes"in arabalar
print(isFound)
#6
print(arabalar[-2]) #listenin sonundaki indeksi (-1) sondan bir önceki indeksini ise(-2) ile çağırabiliriz
#7
print(arabalar[0:3]) #0. indeksten 3.indekse kadar olanları yazdırdık
#8
arabalar="bmw mercedes opel mazda".split()
arabalar=arabalar[0:2]
result=arabalar+["toyota","renault"] #arabalar listesinin ilk iki indeksini alıp sonlarına toyota ve
print(result)                        #renault markalarını ekleyerek yeni bir liste oluşturduk.
#9
result=arabalar+["audi","nissan"] #arabalar listesine audi ve nissanı ekledik.
print(result)
#10
arabalar=arabalar[0:3]
print(arabalar)
#11
arabalar="bmw mercedes opel mazda".split()
print(arabalar[::-1])                         #listeyi tersten yazdırdık
#12
studentA="Muharrem,1995,(80,70,90)"
studentB="Kazım,1999,(80,80,70)"
studentC="Ayse,1968,(90,90,90)"
result=[studentA] +[ studentB] +[ studentC] #3 kişinin bilgilerini bir listede topladık
print(result)
print(result[2])