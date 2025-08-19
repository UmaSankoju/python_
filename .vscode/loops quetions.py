#scope

# n=1
# while n<100:
#     if n%2==0:
#         print(n)
#     n+=1

# n=5
# sum_of_n=0
# for i in range(1,6):
#     sum_of_n+=i
# print(sum_of_n)

# n=1
# sum_of_n=0
# while n<56:
#     sum_of_n+=n
#     n+=1
# print(sum_of_n) 

# n=55
# sum_of_n=0
# while n>0:
#     sum_of_n+=n
#     n-=1
# print(sum_of_n)  

# while True:
#     n=int(input("enter a number:"))
#     sum_digit=0
#     if n>0:
#         while n>0:
#             digit=n%10
#             sum_digit+=digit
#             n=n//10
#         print(sum_digit)
#     else:
#         print("you hitten single digit \n loop stops")
#         break  

# while True:
#     n=float(input("enter a number:"))
#     if n<=0:
#         print("negative number entered:")
#         break

# password=str(input("enter a number:"))
# actual_password="r765776908"
# while password!=actual_password:
#     print("you entered wrong password\ntry again")
#     password=str(input("enter a number:"))
# if password==actual_password:
#     print("login successful")

# n=1
# while n<51:
#     if n%2==0:
#         print(n)
#     n+=1    

# n=5768
# sum_n=0
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     sum_n+=digit
#     n=n//10
# print(rev)    
# print(sum_n)  

### we use print(prime), when loop is over..we should give print prime in last### 

# n=int(input("enter a number"))
# for i in range(2,n):
#     if n%i==0:
#         print(n,"is not prime")
#         break
# else:
#     print(n,"is prime")        

# n=int(input("enter a number"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count>1:
#     print(n,"is prime") 
# else: 
#     print(n,"is not prime")   

# def check_prime(in_num):
#     if in_num<=1:
#         return "not a prime"
#     for i in range(2,in_num):
#         if in_num%i==0:
#             return "not a prime"
#     return "prime"    
            
# print(check_prime(5))  

# n = int(input("Enter a number: "))

# flag = True

# if n <= 1:
#     flag = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             flag = False
#             break

# if flag:
#     print(n, "is prime")
# else:
#     print(n, "is not prime")

# for n in range(2, 101):  # start from 2 because 1 is not prime
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=" ")


# num=int(input("enter a number"))
# print("prime numbers between 2 to",num)
# for n in range(2,num):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         print(n, end=",")
