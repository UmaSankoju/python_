class Calculater():
    def add(self,a,b):
        print("addition of",a,"and",b,"is",a+b)
    def sub(self,a,b):
        print("substraction of",a,"and",b,"is",b-a) 
    def multi(self,a,b):
        print("multiplication of",a,"and",b,"is",a*b)   
    def div(self,a,b):
        if a!=0:
          print("division of" ,a,"and",b, "is",a/b) 
        else:
            print("division not possible")   
        
    def display(self):
        print("Calculator Colour:", self.colour)
        print("Price:", self.price)
        print("Discount:", self.discount, "%")
  
        
minicalc1=Calculater() 
minicalc2=Calculater() 
minicalc3=Calculater() 
minicalc4=Calculater()
minicalc5=Calculater()
# print("arithemetic")
# minicalc1.add(25,5)    
# minicalc1.sub(25,5)    
# minicalc1.multi(25,5)    
# minicalc1.div(25,5)  

minicalc1.colour = "Black"
minicalc1.price = 500
minicalc1.discount = 10  

minicalc2.colour = "white"
minicalc2.price = 450
minicalc2.discount = 15  

minicalc3.colour = "red"
minicalc3.price = 550
minicalc3.discount = 12  

minicalc4.colour = "voilet"
minicalc4.price = 500
minicalc4.discount = 20  

minicalc5.colour = "peech"
minicalc5.price = 500
minicalc5.discount = 25  


print("arithemetic operations on minicalc1")
minicalc1.add(25,5)    
minicalc1.sub(25,5)    
minicalc1.multi(25,5)    
minicalc1.div(25,5)
minicalc1.display()

print("arithemetic operations on minicalc2")
minicalc1.add(55,5)    
minicalc1.sub(55,5)    
minicalc1.multi(55,5)    
minicalc1.div(55,5)
minicalc2.display()

print("arithemetic operations on minicalc3")
minicalc1.add(35,5)    
minicalc1.sub(35,5)    
minicalc1.multi(35,5)    
minicalc1.div(35,5)
minicalc3.display()

print("arithemetic operations on minicalc4")
minicalc1.add(45,5)    
minicalc1.sub(45,5)    
minicalc1.multi(45,5)    
minicalc1.div(45,5)
minicalc4.display()

print("arithemetic operations on minicalc5")
minicalc1.add(75,5)    
minicalc1.sub(75,5)    
minicalc1.multi(75,5)    
minicalc1.div(75,5)
minicalc5.display()