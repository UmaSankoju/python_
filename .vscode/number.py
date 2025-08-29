##Printing even digits in given number##
n=int(input("enter a number:"))
temp=n
even_digits=[]
digit_count=0
while temp>0:
    digit_count+=1
    digit=temp%10
    temp=temp//10
    if digit_count%2==0:
        even_digits.append(digit)
print("even digits in given numbers are",even_digits)
##printing prime numbers in given number##        
temp1=n
prime_numbers=[]
while temp1>0:
    digit=temp1%10
    temp1=temp1//10
    if digit>1:
         for i in range(2,digit):
             if digit%i==0:
                 break 
         else:
             prime_numbers.append(digit)     
print("prime numbers in given number are:",prime_numbers) 

##checking a number is Perfect Or Not ##
num=int(input("enter a number:"))
temp=num
sum_num=0
factors=[]
for i in range(1,num):
    if num%i==0:
        factors.append(i)
for j in factors:
    sum_num+=j
if sum_num==temp:
    print(temp,"is perfect number")
      
##Perfect Numbers in range##
perfect_numbers=[]
for digit in range(1,100):
    sum_digit=0
    factors=[]
    for i in range(1,digit):
        if digit%i==0:
            factors.append(i)
    for j in factors:
        sum_digit+=j
    if sum_digit==digit:
         perfect_numbers.append(digit)
print("perfect numbers between 1 to 100:",perfect_numbers)  

##palindrome##
palindrome=[]
for n in range(11,1000):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10  
        rev=rev*10+digit 
        temp=temp//10
        if rev==n:
            palindrome.append(n)         
                
print("palindrome numbers between 11 t0 1000:",palindrome)    

