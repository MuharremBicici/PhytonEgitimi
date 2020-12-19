website="http://www.MuharremBicici.com"
course="Python Kursu:Bastan sona python programlama"

#1
phrase=" Hello World " #String ifadenin sağındaki ve solundaki boşlukları atar
print(phrase.strip())
#2
print(website.find("MuharremBicici")) #website adında "MuharremBicici" ifadesinin hangi indekslere
print(website[11:25])                 #karşılık geldiğini bulduk
#3
print(course.lower())            #course ifadesinin tamamını küçük harflerle yazdırdık
#4
print(website.count("i"))     #website ifadesinde kaç tane "i" var?
#5
isFound=website.startswith("www") #website www ile başlıyor mu?
print(isFound)
isFound=website.endswith("com") #website com ile bitiyormu
print(isFound)
#6
isFound=website.find(".com") #".com" ifadesi websitesi içerisinde yer alıyormu?
print(isFound)
#7
alpha=course.isalpha() #course içerisindeki string ifade alfabetik sıralı mı?
print(alpha)
#8
message="Contents"
message=message.center(50,"*") #Mesajı 50 karakterin tam merkezine yazdırdık ve mesajın sağındaki ve 
print(message)                 #solundaki boşlukları "*" ile doldurduk
#9
course=course.replace(" ","-") #Boşlukların yerine - koyarak yazdırdık
print(course)
#10
message="Hello World"
message=message.replace("World","There") #Mesajdaki world ifadesi yerine there yazdırdık
print(message)
#11
course=course.split() #course ifadesini boşluklardan ayırarak yazdırdık
print(course)