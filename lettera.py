class Letter:
    def __init__(self,letterFrom,letterTo):
        self._letterFrom = letterFrom 
        self._letterTo   = letterTo
        self._line        = ""

    def addLine(self,line):
        self.line += "\n" + line
       
        
        

    def getText (self):
       return f" Dear { self._letterTo} : \n"+ self.line + f" \n\nSincerely, \n\n {self._letterFrom}"
    

missiva = Letter("Mary", "john")
missiva.addLine (" I am sorry we must part")
missiva.addLine (" I wish you all the best")



print(missiva.getText())

     