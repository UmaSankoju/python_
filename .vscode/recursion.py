##  Assignment ##

##Print first n natural numbers using recursion.##
def natural_num(n):
    if n == 0:
        return
    print(n)
    natural_num(n-1)
natural_num(10)
    
##N natural numbers using recursion in reverse order##
def natural_num_rev(n):
    if n == 0:
        return
    natural_num(n-1)
    print(n)
natural_num_rev(10)

##First n even numbers using recursion##
def even_num(n):
    if n == 0:
        return
    # if n % 2 == 0:
    #    print(n)
    even_num(n-1)
    if n % 2 == 0:
       print(n)
print(even_num(10))

## Exponent ##
def exp(m,n):
    if n == 0:
        return 1
    return m * exp(m, n-1)
print(exp(5,2))

##Reverse a list##
list1 = [1, 2, 3, 4, 5]
def rev_list(list1):
    if len(list1) == 0:
        return
    print(list1[-1])
    rev_list(list1[: -1])
# list1 = [1, 2, 3, 4, 5]
rev_list(list1)

## Fibonacci ##
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))

## Palindrome ##

def check_palindrome(str1):
    if len(str1) <= 1:
        return True
    return str1[0] == str1[-1] and check_palindrome(str1[1 : -1])
print(check_palindrome("MALAYLAM"))

## ASSAIGNEMENT ##

## MAX ELEMENT IN A LIST ##
def max_element(list1):
    if len(list1) == 1:
        return list1[0]
    
    max_list = max_element(list1[1:])
    return list1[0] if list1[0] > max_list else max_list

print(max_element(list1))

## Binary search ##
def binary_search(list2, target):
    if target not in list2:
        return "Not Found"
    mid = len(list2)//2 
    if list2[mid] == target:
        return mid
    elif list2[mid] > target:
        return binary_search(list2[ : mid+1], target)
    elif list2[mid] < target:
        return binary_search(list2[mid :], target)
    
list2 = [2, 45, 78, 37, 20, 1, 99]
list2 = sorted(list2)
print(binary_search(list2, -1))