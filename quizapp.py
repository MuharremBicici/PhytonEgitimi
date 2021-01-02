#Önce sorular için bir sınıf oluşturacağız.
class Question:
    def __init__(self,text,choices,answer): #Burada sorular için metni,seçenekleri,cevabı içeren bir fonksiyon oluşturduk
         self.text=text 
         self.choices=choices 
         self.answer=answer 
    def checkanswer(self,answer):           #Burada cevabın doğruluğunu kontrol etmek için bir fonksiyon oluşturduk 
        return self.answer==answer
    
#Şimdi quiz sınıfını oluşturacağımız.Quiz klası içerisinde question klasını kullanacağı için question
#sınıfındaki tüm özellikleri kullanabilir.
class Quiz:
    def __init__(self,questions):     #Burada quiz için soruları içeren bir fonksiyon oluşturduk.
        self.questions=questions 
        self.score=0                  #Doğru cevapların sayımı için puanı sıfırdan başlattık
        self.questionIndex=0          #Soruları sıfırıncı indeksten başlattık
    def getQuestion(self):            #Soru almak için oluşturduğumuz fonksiyon
        return self.questions[self.questionIndex]   
    def displayQuestion(self):       #Soruları göstermek için oluşturduğumuz fonksiyon
        question=self.getQuestion()  #Soruyu alıyoruz ve printle yazdırıyoruz
        print(f"Soru {self.questionIndex+1} : {question.text}")
        for q in question.choices:   #For döngüsü ile seçenekleri alt alta yazdırıyoruz
            print("--"+q)            
        answer=input("Cevap : ")     #Cevabı bir string ifade olarak alıyoruz
        self.guess(answer)           #İnput olarak alınan tahmini aşağıda tanımladığımız guess metoduna gönderiyoruz
        self.loadQuestion()          #Aşağıda tanımladığımız soru çağırma metodunu çağırıyoruz
    def guess(self,answer):          #Tanımladığımız tahmin metodu
        question=self.getQuestion()
        if question.checkanswer(answer): #Eğer cevap doğruysa(true) skoru ve sorunun numarasını 1 artırıyoruz
            self.score+=1
        self.questionIndex+=1
    def loadQuestion(self):        #Soru çağırma metodumuz
        if len(self.questions)==self.questionIndex: #soru sayısı gösterilen sorunun numarasına eşit olduğunda skor gösteriliyor yani sorular bitmiş oluyor.
            self.showScore()
        else:
              self.displayProgres()  #Biraz sonra tanımlayacağımız kaçıncı soruda olduğumuzu gösteren metod
              self.displayQuestion()  
    def showScore(self):             #Sonuçları en son yazdıracak olan metod
        print("Score : ",self.score)
    def displayProgres(self):        #Kaçıncı soruda olduğumuzu gösteren metod
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex +1

        if questionNumber > totalQuestion:
            print("Quiz Sona Erdi ")
        else:
            print(f"Question : {questionNumber} of {totalQuestion}. ".center(100,"*"))

q1=Question("En iyi programlama dili hangisidir?",["Phyton","Java","c","HTML"],"Phyton")
q2=Question("En kolay programlama dili hangisidir?",["Phyton","Java","c","HTML"],"Phyton")
q3=Question("En popüler programlama dili hangisidir?",["Phyton","Java","c","HTML"],"Phyton")
questions=[q1,q2,q3]

quiz=Quiz(questions)
question=quiz.loadQuestion()



         