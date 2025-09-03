#Print Numbers from 1 to n##
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i,end=" ")

#Print Numbers from m to n##
m=int(input("enter lower range:"))
n=int(input("enter upper range:"))
for i in range(m,n+1):
    print(i,end=" ")

#Print Numbers from n to 1 in Reverse##
n=int(input("enter a number:"))
for i in range(n,0,-1):
    print(i,end=" ")

# Print Numbers from n to m in Reverse##
m=int(input("enter lower range:"))
n=int(input("enter upper range:"))
for i in range(n,m-1,-1):
    print(i,end=" ")

#Sum of n Natural Numbers##
n=int(input("enter a number:"))
sum_n=0
for i in range(n+1):
    sum_n+=i
print(sum_n)   


n=int(input("enter a number:")) 
if n>2:
 for i in range(2,n):
    if n%i==0:
        print(n,"is not prime")
        break
 else:
    print(n,"is prime")
else:
    print(n,"is not prime")
    

def is_prime(n):
    if n<2:
        return False
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    return False 
n=int(input("enetr a number:"))
print(is_prime(n))


 
            
#Factorial of a Number##
n=int(input("enter a number:"))
fact=1
while n>0:
    fact*=n
    n=n-1
print(fact) 

#Sum of m to n Numbers##
m=int(input("enter lower boundary: "))
n=int(input("enter upper boundary: "))
sum_m_t0_n=0
for i in range(m,n+1):
    sum_m_t0_n+=i
print(sum_m_t0_n)    



#Product of m to n Numbers##
m=int(input("enter lower boundary: "))
n=int(input("enter upper boundary: "))
product_m_t0_n=1
for i in range(m,n+1):
    product_m_t0_n*=i
print(product_m_t0_n)  

#Print Factors of a Number##
n=int(input("enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)

#Count of Factors##
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count) 
       

#printing addition of first largest and seconed largest##
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>=b>=c or b>=a>=c:
    print (a+b)
elif a>=c>=b or c>=a>=b: 
    print(a+c)
elif b>=c>=a or c>=b>=a:
    print(b+c)
            
#Prime Number Check##            
n=int(input("enter a number:")) 
if n>2:
 for i in range(2,n):
    if n%i==0:
        print(n,"is not prime")
        break
 else:
    print(n,"is prime")
else:
    print(n,"is not prime")


#Even Numbers from m to n##
m=int(input("enter lower boundary: "))
n=int(input("enter upper boundary: "))
for i in range(m,n+1):
    if i%2==0:
        print(i,end=" ")

#Odd Numbers from m to n##
m=int(input("enter lower boundary: "))
n=int(input("enter upper boundary: "))
for i in range(m,n+1):
    if i%2!=0:
        print(i,end=" ")

#Count of Even and Odd Numbers##
m=int(input("enter lower boundary: "))
n=int(input("enter upper boundary: "))
even_count=0
odd_count=0
for i in range(m,n+1):
    if i%2==0:
        even_count+=1
        
    else:
        odd_count+=1
        
print("even count:",even_count) 
print("odd count",odd_count)  

#Reverse a String##
string="uma maheshwari"
rev=" "
for char in string:
    rev=char+rev
print(rev)    

#Check for Palindrome String##
string="uma"
rev=""
for char in string:
    rev=char+rev
if rev==string:
    print(string,"is palindrome")
else:
    print("not a palindrome")    

#Sum of Digits##  
n=int(input("enter a number:"))
sum_digits=0
while n>0:
    digit=n%10
    sum_digits+=digit
    n=n//10
print(sum_digits) 

#Product of Digits##
n=int(input("enter a number:"))
product_digits=1
while n>0:
    digit=n%10
    product_digits*=digit
    n=n//10
print(product_digits)   

#Armstrong Number Check##
n=int(input("enter a number:"))
temp=n
count=len(str(n))
check_arm=0
while n>0:
    digit=n%10
    check_arm+=digit**count
    n=n//10
if temp==check_arm:
    print(temp,"is armstrong")    
else:
    print(temp,"not an armstrong") 

#Reverse a Number ##  
n=int(input("enter a number:"))
rev=0
while n>0:
  digit=n%10
  rev=rev*10+digit
  n=n//10
print(rev)  
  

# Palindrome Number Check##
n=int(input("enter a number:"))
temp=n
rev=0
while n>0:
  digit=n%10
  rev=rev*10+digit
  n=n//10
if temp==rev:
    print(temp,"is palindrome")  
else:
    print(temp,"is not palindrome")    
  

#Count Vowels in String##
string="uma maheshwari"
vowels="aeiouAEIOU"
count=0
for i in string:
    if i in vowels:
        count+=1
print(count)  
 
# Count Consonants in String##
string="uma maheshwari"
vowels="aeiouAEIOU"
vowel_count=0
cons_count=0
for char in string:
    if ("a"<=char<="z") or ("A"<=char<="Z"):
        if char in vowels:
            vowel_count+=1
        else:
            cons_count+=1 
print("vowel count",vowel_count) 
print("consonant count",cons_count)              

#perfect number##
n=int(input("enter a number:"))
sum_divisiors=0
for i in range(1,n):
    if n%i==0:
        sum_divisiors+=i
if sum_divisiors==n:
    print("perfect number")
else:
    print("not a perfect number")

#neon number##   
n=int(input("enter a number:"))         
m=n**2
sum_m=0
while m>0:
    digit=m%10
    sum_m+=digit
    m=m//10
if n==sum_m:
    print("neon number")
else:
    print("not a neon number")  


#Strong number check | Krishnamurthy number##  
n=int(input("enter a number:"))
temp=n
sum_fact=0
while n>0:
    digit=n%10
    fact=1
    while digit>0:
        fact*=digit
        digit-=1
    sum_fact+=fact
    n=n//10
if temp==sum_fact:
    print("strong number")    
else:
    print("not a strong number")    

#harshad Number Check##
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

#Fibonacci Series##
n=int(input("enter a number"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

# neon number in range##   
for n in range(1,1000):      
    m=n**2
    sum_m=0
    while m>0:
        digit=m%10
        sum_m+=digit
        m=m//10
    if sum_m==n:
      print(n,end=" ")



      
      
