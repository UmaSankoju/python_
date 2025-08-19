# def average(*a):
#     average=sum(a)/2
#     print("average of given numbers:",average)
# average(2,4,9,5,7,5)    

# types of argumrnts
#  position arguments
#  keyword arguments
#  default arguments
#  arbitary argumrnts(*)
#  keyword arbitary arguments(**)

#arbitary argumrnts(tuple type)

# def sum_of(*b):
#     temp=0
#     for i in b:
#         temp=temp+i
#     print(temp)    
# sum_of(4,6) 
# sum_of(55,8,2,6,0)  

#keyword arbitary arguments(dict type)

# def connect_to_db(**kargs):
#     print(kargs)    
# connect_to_db(db_host="localhose:3300",port="3546", password="9094")    
 
#return
#functions with statements
# we use return to re use the result given
# return statement ones executed, it will be end of function 

# def add(a,b):
#     return a+b
# result=add(5,7)  
# print(result*5)  

# def even_odd(a):
#     if a%2==0:
#         return "it is even"
#     else:
#         return "it is odd"
# result=print(even_odd(5))   

# def simple_calculater(a,b):
#     print(a+b,a*b,a/b)
# simple_calculater(25,5)  
 
# def simple_calculater(a,b):
#      return a+b,a*b,a/b
# print(simple_calculater(25,5)) (((#result will be tiple format)))
 
 
 ##Functions Scope##
 
 