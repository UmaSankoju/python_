# def check_pos_neg_zero(n):
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return 0
# num_input=int(input("enter a number:"))    
# num=check_pos_neg_zero(num_input)   
# print(num) 

#(((ternary operator)))
# def even_odd(n):
#     result="even" if n%2==0 else "odd"
#     return result
# n_input=int(input("enter a number:"))
# print(even_odd(n_input))

# def elgibilty(n):
#     result="elgible" if n>=18 else "not elgible"
#     return result
# n_input=int(input("enter your age:"))
# print(elgibilty(n_input))

# def greatest(n1,n2):
#     result= n1  if n1>n2 else "both are equal" if n1==n2 else n2
#     return result
# n1_input=int(input("enter first num:"))
# n2_input=int(input("enter second num:"))
# result=greatest(n1_input,n2_input)
# print(result,"is greatest")


# operator=input("enter a operator(+,-,*,/)")
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# if operator=="+":
#   print("addition",a+b)
# elif operator=="-":
#    print("substraction",a-b) 
# elif operator=="*":
#     print("multiplicatin",a*b)
# else:
#     if b>0:
#         print("division",a/b)
#     else:
#         print("division not possible") 
        
        
# def simple_calculator(operator,a,b):
#     if operator=="+" or operator=="add":
#        print("addition",a+b)
#     elif operator=="-"or operator=="sub" :
#        print("substraction",a-b) 
#     elif operator=="*" or operator=="multi":
#        print("multiplicatin",a*b)
#     elif operator=="/" or operator=="div":
#       a/b if b>0 else "division not possible"
    
# operator=input("enter a operator(+,-,*,/,add,sub,multi,div)")
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))   
# print(simple_calculator(operator,a,b))                       



# def simple_calculator(operator,a,b):
#     if operator in ["+","add","ADD"]:
#        print("addition",a+b)
#     elif operator in["-","sub","SUB"] :
#        print("substraction",a-b) 
#     elif operator in ["*" ,"multi","MULTI"]:
#        print("multiplicatin",a*b)
#     elif operator in ["/" ,"div","DIV"]:
#       print(a/b) if b>0 else print("division not possible")
    
# operator=input("enter a operator(+,-,*,/,add,sub,multi,div, ADD,MULTI,SUB,DIV)")
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))   
# print(simple_calculator(operator,a,b))              

# def simple_calculator(operator,a,b):
#     if operator=="+" or operator=="add":
#        print("addition",a+b)
#     elif operator=="-"or operator=="sub" :
#        print("substraction",a-b) 
#     elif operator=="*" or operator=="multi":
#        print("multiplicatin",a*b)
#     elif operator=="/" or operator=="div":
#       a/b if b>0 else "division not possible"
    
# operator=input("enter a operator(+,-,*,/,add,sub,multi,div)").lower()
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))   
# simple_calculator(operator,a,b)   

# def check_leap(year): 
#   if year<0:
#       return "invalid year" 

#   return "leap year" if (year % 400==0) or (year % 4 ==0 and year%100!=0) else "not a leap year"

# print(check_leap(2015))  

# def tri_angle(a,b,c):
#     return "given sides form a triangle" if a+b>c and a+c>b and b+c>a  else "doesn't form triangle"    
# def check_type_triangle(a,b,c):
#     if a==b==c:
#         return "equilaterel triangle"
#     elif a==b!=c or a==c!=b or b==c!=a:
#         return "isolateral triangle"
#     else:
#         return "scalace"
# def angle_type(a,b,c):
#     if (a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==b**2+a**2):
#         return "right angle triangle"
#     elif (a**2>b**2+c**2) or (b**2>a**2+c**2) or (c**2>b**2+a**2) :
#         return "obtuse angle triangle" 
#     elif  (a**2<b**2+c**2) or (b**2<a**2+c**2) or (c**2<b**2+a**2):
#         return "acute angled triangle" 

# a=int(input("enter a side:")) 
# b=int(input("enter a side:")) 
# c=int(input("enter a side:")) 
# if tri_angle(a,b,c):
#     print("given sides:",a,b,c)
#     print(a,b,c,"form a triangle")
#     print("type of triangle:",check_type_triangle(a,b,c))
#     print("angle type of triangle:",tri_angle(a,b,c))
# else:
#     print(a,b,c,"does not form a triangle")

    

# def check_v_c_neither(char):
    
#     if len(char)!=1:
#         return "invalid input"
#     if char in "AEIOU":
#         return "vowel"
#     else:
#         return "consonant"
# input_char=str(input("enter a character:")).upper()    
# print(check_v_c_neither(input_char))    
        
    
