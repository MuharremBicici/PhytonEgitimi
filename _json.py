import json
import os
class User:
    def __init__(self,username,password,email): #Önce bir user sınıfı oluşturduk.İnput olarak isim,şifre ve mail bilgisi tanımladık.
        self.username=username
        self.password=password
        self.email=email
        
class userRepository:     #Kullanıcı işlemlerini tanımlamak için bir userrepository sınıfı oluşturduk.
    def __init__(self):
        self.users=[]            #Kullanıcıları kaydedeceğimiz bir liste oluşturduk
        self.isLoggedIn=False    #Kullanıcı giriş yaptı mı bilgisini başlangıç olarak false değer belirledik.
        self.currentUser={}      #Giriş yapan aktif kullanıcıyı görüntülemek için bir dict yapısı tanımladık.
        self.loadUsers()         #Kullanıcı yükleme adındaki aşağıda tanımladığımız fonksiyonu  çağırdık
    
    def loadUsers(self):         #Kullanıcı yükleme fonksiyonu
        if os.path.exists("users.json"):   #Eğer users.json adında(kullanıcıları kaydettiğimiz dosya) varsa
            with open("users.json","r",encoding="utf-8")as file: #Okumak amacıyla dosyayı açıyoruz.
                users=json.load(file)    #File içindeki bilgileri load metoduyla aldık ve users listesine yazdık
                for user in users:       
                    user=json.loads(user) #Dosyada json stringi olarak kayıtlı bilgiyi bir python objesine dönüştürdük.
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(users) #json yapısıyla tanımladıktan sonra dosyaya kaydediyoruz
            print(self.users)
    
    def register(self,user: User):
        self.users.append(user)        #Kullanıcıyı users listesin ekledik
        self.savetoFile()              #Dosyaya kaydet fonksiyonunu çağırdık
        print("Kullanıcı oluşturuldu")
    def login(self,username,password): #Giriş fonksiyonunu tanımladık
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedIn=True   #Parametreler doğru olup giriş yapıldığında isloggenin True değer alıyoe.
                self.currentUser=user #Giriş yapıldığı için kullanıcı giriş yapan user oluyor.
                print("Giriş başarılı")
                break
    def Logout(self): #Çıkış
        self.isLoggedIn=False  #isloggedin e False çevirerek çıkış yapıyoruz.
        self.currentUser={}    
        print("Çıkış başarılı")
    def identity(self):    #Eğer giriş yapıldıysa giriş yapan userin ismi ekrana yazdırılıyor.
        if self.isLoggedIn:
            print(f"Username : {self.currentUser.username}")
        else:
            print("Giriş yapılmadı.")

        
    def savetoFile(self):  #Kaydetme fonksiyonu
        list=[]            #Boş bir liste tanımladık
        for user in self.users: 
            list.append(json.dumps(user.__dict__)) #Dictionary yapısındaki user bilgilerini json stringine çevirip listeye ekledik.
        with open("users.json","w")as file: #users.json dosyasını yazma amacıyla açarak listeyi kaydettik
            json.dump(list,file)


repository=userRepository()

while True: #Kullanıcı menüsünü aşağıda tanımladık.Yukarda tanımladığımız fonksiyon ve sınıfları çağırarak menüyü oluşturduk.
    print("Menü".center(50,"*"))
    secim=input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçim : ")
    if secim=="5":
        break
    else:
        if secim=="1":
            username=input("Username : ")
            password=input("Password : ")
            email =input("eMail : ")
            
            user=User(username=username,password=password,email=email)
            repository.register(user)
        elif secim=="2":
            if repository.isLoggedIn:
                print("Zaten giriş yapıldı")
            else:
                username=input("username : ")
                password=input("password : ")
                repository.login(username,password)
        elif secim=="3":
            repository.Logout()
        elif secim=="4":
            repository.identity()
        else:
            print("Yanlış seçim")
        
            

