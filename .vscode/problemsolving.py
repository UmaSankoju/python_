
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