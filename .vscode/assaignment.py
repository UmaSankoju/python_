# # 
# a=str(input("ente a string:"))
# vowels="aeiouAEIOU"
# a_1_vowels=''
# a_2_vowels=''
# if len(a)%2==0:
#     a_1=a[0:len(a)//(2)]
#     # a_1_vowels=""
#     a_2=a[len(a)//(2):]
#     # a_2_vowels=""
#     # vowels="aeiouAEIOU"
#     for ch in a_1:
#         for ch in vowels:
#             a_1_vowels+=ch
            
#     for ch in a_2:
#         for ch in vowels:
#             a_2_vowels+=ch
            
            
        
#     print("vowels in first half",a_1_vowels)
#     print("vowels in second half",a_2_vowels)
# else:
#     print("your strin is inavalid")


# n=int(input("enter a number:"))
# print("prime numbers between 2 and",n)
# for num in range (2,n):
#     for i in range(2,num):
#        if num%i==0:
#          break
#     else:
#       print(num,end=",")
      
# n = int(input("Enter a number: "))
# print("Prime numbers between 2 and", n)

# for num in range(2, n):
#     for i in range(2, num):
#         if num % i == 0:  # check divisibility of num
#             break
#     else:  # executes if the loop is not broken
#         print(num, end=" ")


# n = int(input("Enter start number: "))
# for num in range(1,n+1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")

# n = int(input("Enter a number: "))
# for num in range(1, n+1):
#     if num > 1:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")

# n=int(input("enter a number:"))

# for num in range(1, n + 1):
#     if num > 1:
#         flag = True
#         for i in range(2, num):
#             if num % i == 0:
#                 flag = False
#                 break
#         if flag:
#             print(num, end=" ")
# print("\n")
