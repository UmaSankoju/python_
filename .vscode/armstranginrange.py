def check_armstrong(n):
    temp=n
    sum=0
    count=0
    while n>0:
        digit=n%10
        n=n//10
        count+=1
    n=temp
    while n>0:
        digit=n%10
        sum+=digit**count
        n=n//10
    return sum==temp
    
 
for num in range(100,2000):
    if check_armstrong(num):
         print( num,"armstrong number")
    else:
        continue
