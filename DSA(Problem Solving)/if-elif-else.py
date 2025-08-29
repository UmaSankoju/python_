#check even or odd##
n=int(input("enter a number:"))
if n%2==0:
    print(n,"even number")
else:
    print(n,"odd number")    

#.Divisible by 5 but Not by 10##
n=int(input("enter a number:"))
if n%5==0 and n%10!=0:
    print("satisfy")
else:
    print("it doesn't satisfy")   

# Biggest Among Two Numbers##
a=int(input("enter first number:"))
b=int(input("enter seconed number:"))
if a>b:
    print(a,"is bigger")
elif b>a:
    print(b,"is bigger")
elif a==b:
    print(a,b,"are equal")    

#Smallest Among Two Numbers##
a=int(input("enter first number:"))
b=int(input("enter seconed number:"))
if a<b:
    print(a,"is smaller")
elif b<a:
    print(b,"is smaller")
elif a==b:
    print(a,b,"are equal")

#Divisible by 2, 3, and 6##
n=int(input("enter a number:"))   
if (n%6==0):
    print("satisfy")
else:
    print("it doesn't satisy")    

#voting elgibility##
dob=int(input("enter your birth year:"))
current_year=2025
age=current_year-dob
if age>=18:
    print("you are elgible to vote")
else:
    print("you are not elgible to vote\n you have to wait",18-age,"year(s)")    

#Student Pass/Fail Based on All Subjects >= 35##
maths=int(input("enter your maths marks:"))
physics=int(input("enter your physics marks:"))
chemistry=int(input("enter your chemistry marks:"))
if maths>=35 and physics>=35 and chemistry>=35:
    print("pass")
else:
    print("fail")    

#Student Pass if Passed Any One Subject (>= 35)##
maths=int(input("enter your maths marks:"))
physics=int(input("enter your physics marks:"))
chemistry=int(input("enter your chemistry marks:"))
if maths>=35 or physics>=35 or chemistry>=35:
    print("pass")
else:
    print("fail")  
  
#Student Pass if Passed Any Two Subjects##
maths=int(input("enter your maths marks:"))
physics=int(input("enter your physics marks:"))
chemistry=int(input("enter your chemistry marks:"))
if (maths>=35 and physics>=35) or (physics>=35 and chemistry>=35) or (chemistry>=35 and maths>=35):
    print("pass")
else:
    print("fail")    

#Biggest Among Three Numbers##
a=int(input("eneter a number:"))
b=int(input("eneter a number:"))
c=int(input("eneter a number:"))
if a>b and a>c:
    print(a,"is bigger")
elif b>a and b>c:
    print(b,"is bigger") 
elif c>a and c>b:
    print(c,"is bigger")   

#Smallest Among Three Numbers##
a=int(input("eneter a number:"))
b=int(input("eneter a number:"))
c=int(input("eneter a number:"))
if a<b and a<c:
    print(a,"is smaller")
elif b<a and b<c:
    print(b,"is smaller") 
elif c<a and c<b:
    print(c,"is smaller") 

#Perfect Square or Not##
n=int(input("enter a number:"))
if n%(n**0.5)==0:
    print("perfect square")
else:
    print("not a perfect square")  

#Cars Required for Members (Max 5 per car)##  
people=int(input("eneter total number of people:"))
if people%5==0:
    print("required cars",people//5)
elif people%5!=0:
    print("reqiured cars",(people//5)+1)
    
#Second Biggest Among Three Numbers##
a=int(input("eneter a number:"))
b=int(input("eneter a number:"))
c=int(input("eneter a number:"))
if a>b>c or c>b>a:
    print(b,"is second biggest")
elif b>a>c or c>a>b:
    print(a,"is second biggest")
elif a>c>b or b>c>a:
    print(c,"is second bigger") 

#leap year##
year=int(input("enter a year:")) 
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")    


    
      