##Sum of digits##
n=8765
sum_n=0
while n>0:
    digit=n%10
    sum_n+=digit
    n=n//10
print(sum_n)     

##count the no.of digits in number##
n=67665
count=0
while n>0:
    count+=1
    digit=n%10
    n=n//10
print(count)    

##check palindrome## 
n=int(input("enter a number:"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("palindrome") 
else:
    print("not a palindrome")       

##perfect number##
n=int(input("enter a number:"))
sum_fact=0
for i in range(1,n):
    if n%i==0:
        sum_fact+=i
if sum_fact==n:
    print("perfect number") 
else:
    print("not a perfect number")  

##perfect square##
n=int(input("enter a number:"))  
if n%(n**(0.5))==0:
    print(n,"is perfect square") 
else:
    print(n,"is not perfect square")         


##sunny Number##
n=int(input("enter a number:"))  
if (n+1)%((n+1)**(0.5))==0:
    print(n,"is sunny number") 
else:
    print(n,"is not sunny number")



##harshad Number Check##
n=int(input("enter a number:"))
temp=n
sum_n=0
while n>0:
    digit=n%10
    sum_n+=digit
    n=n//10
if temp%sum_n==0:
    print(temp,"is harshad number")    
else:
    print(temp,"is not harshad number")


##neon number##
n=int(input("enter a number:"))
m=n**2
sum_m=0
while m>0:
    digit=m%10
    sum_m+=digit
    m=m//10
if n==sum_m:
    print(n,"neon number")  
else:
    print(n,"not a neon number") 

##Automarphic Number##
n=int(input("enter a number:"))  
temp=n
m=n**2
count=0
while n>0:
    count+=1
    n=n//10
last_digits=m%(10**count)
    
if temp==last_digits:
    print("automarphic") 
else:
    print("not automarphic")
##composite numbers## 
n=int(input("enter a number:"))
for i in range(2,n):
    if n%i==0:
        print(n,"is composite number")
        break
else:
    print(n,"is not a composite number")
    
##spy number##
n=int(input("enter a number:"))
multi_n=1
sum_n=0
while n>0:
    digit=n%10
    sum_n+=digit
    multi_n*=digit
    n=n//10
if sum_n==multi_n:
    print(n,"is spy number") 
else:
    print(n,"is not spy number")      
