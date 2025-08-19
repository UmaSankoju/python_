
n=int(input("enter a number:"))
temp=n
sum=0
digits=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**digits
    n=n//10
print(sum)


if sum==temp:
    print("armstrong number")
else:
    print(temp,"is not armstron number")  
    
###USING FUNCTIONS###    
    
def check_armstrong_number(n):
    temp=n
    sum=0
    digits=len(str(n)) 
    while n>0:
        digit=n%10
        sum+=digit**digits
        n=n//10 
    
    return "armstrong number" if sum==temp else "it is not an armstrong number"

      
n=int(input("enter a number:")) 
print(check_armstrong_number(n))