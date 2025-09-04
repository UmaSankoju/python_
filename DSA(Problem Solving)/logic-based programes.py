##Prime and Armstrong Logic Questions###

#Print All Prime Numbers from m to n##
m=10
n=30
for i in range(10,30):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i, end=" ") 

#Count of All Prime Numbers from m to n##
m=1
n=10
count=0
for i in range(m,n):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1 
print(count) 

#Print All Armstrong Numbers in a Range##
m=1
n=500
for num in range(1,500):
    temp=num
    temp1=num
    rev=0
    count=0
    while temp>0:
        count+=1
        temp=temp//10
    while temp1>0:
        digit=temp1%10
        rev+=digit**count 
        temp1=temp1//10
    if rev==num:
        print(num, end=" ")       
        
        


  
            
            
s="uma sankoju"
rev=" "
for i in s:
    rev=i+rev
print(rev)    

s="abc"
r1=""
r2=""
r3=""
r4=""
r1=s[0]+s[1]+s[2]
r2=s[1]+s[2]+s[0] 
r3=s[2]+s[0]+s[1]  
r4=s[0]+s[2] +s[1]
print(r1)
print(r2)
print(r3)
print(r4)

##circuler prime number##
def is_prime(num):
    if num>2:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True    
        
    else:
        return False
def is_circular_prime(n):
    s=str(n)
    for j in range(len(s)):
        word=int(s[j:]+s[:j]) 
        if not is_prime(word):
            return False
    else:
        return True  
    
n=int(input("enter a number:")) 
if is_circular_prime(n):
    print(n,"is circular prime")  
       
else:
    print(n,"is not circular prime")
