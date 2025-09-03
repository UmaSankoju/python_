# a=0
# b=1
# for i in range(5):
#     for n in range(1):
#       for j in range(i+1):
#          print(a,end="  ")
#          a,b=b,a+b
#       print()    

# a=0
# b=1
# for n in range(1):
#     for i in range(5):
#         for j in range(i+1):
#             print(a,end=" ")
#             a,b=b,a+b
#         print()    

# for n in range(10):
# for i in range(5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    

# s="abcde"
# n=len(s)
# for i in range(n):
#     for j in range(i,n):        
#         for k in range(i,j+1):   
#             print(s[k], end=" ")
#         print()
#     print()    

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