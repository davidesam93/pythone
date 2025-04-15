""" Realizzate una classe, Student, che rappresenti uno studente.In questo esercizio, uno studente ha un nome e un punteggio totale (score) .
Definite nella classe:
un costruttore appropriato e i metodi GetName () restituisce anche il cognome , addQuiz(score), getTotalScore () e getAverageScore().
 Per realizzare l'ultimo dei metodi richiesti, che calcola il punteggio medio per i questionari compilati dallo studente, è necessario memorizzare anche il numero
   di questionari compilati  """

class student():
    def __init__ (self,nome,cognome):
     self._nome    = nome
     self._cognome = cognome
     self._totScore   = 0.0
     self._n0fQuiz = 0

    def GetName(self) :
        return f" {self._nome}, {self._cognome}"

    def AddQuiz(self,score) :
       self._totScore += score
       self._n0fQuiz += 1

    def getTotalScore(self) :
       return self._totScore
    
    def getAverageScore(self):
       return self._totScore / self._n0fQuiz
    

eleonora = student("Eleonora","Moroni")
davide   = student ("Davide", "Sambughi")

davide.AddQuiz(19)
davide.AddQuiz(17)
davide.AddQuiz(18)

print(davide.getAverageScore())

       
       

    

