website="htpp://www.MuharremBicici.com"
course="Python Kursu:Baslangıc seviyesinden ileri seviyeye python"

print(len(course)) # Kurs karakter dizisinin kac karakterden olustugu
print(website[7:10]) #www kısmını yazdırdık
print(len(website))  # Website karakter dizisinin kac karakterden olustugu
print(website[26:29])  #com kısmını yazdırdık
print(course[0:15]) #0dan 15. karaktere kadar olan kısmı yazdırıyoruz
print(course[43:57]) # son 15 karakteri yazdırdık.
print(course[::-1]) # tesrten yazdırdık -1 yerine 1 deseydik düz yazardı

name="Muharrem"
surname="Bicici"
age=25
job="Engineer"

print(f"My name is {name} {surname}.I am {str(age)} years old.I am an {job}.")   # printF metodu ile
print("My name is {} {}.I am {} years old.I am an {}".format(name,surname,age,job)) #Format metodu ile


