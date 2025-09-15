##Add a Number##
def add_a_num(a):
    li1=[]
    li1=li+[a]
    print(li1)
li=[1,2,3,4,5]
add_a_num(7)

##To find element##
def find_elemnet(input_list,input_index):
    if  input_index < -len(input_list) or input_index >= len(input_list):
        
       return "invalid index" 
    else:
        return input_list[input_index]


# index=int(input("enter a number:"))
list1=[1,2,3,4,5,-6,10,-45]

print(find_elemnet(list1,2))


##Find sum , max and min of the list##

def find_sum_list(li):
    if len(li) == 0:
        return "invalid list"
    else:
        maximum=li[0]
        minimum=li[0]
        sum_of_list = 0
        for i in li:
            sum_of_list += i
            if i > maximum:
                maximum  =i
            if i < minimum:
                minimum = i
            
        return f" sum of elements in list {sum_of_list} \n maximum element in list {maximum}\n least element in list  {minimum}"

li = [1,3,6,9,0,-4,-4.5] 
print(find_sum_list(li))

##Reverese a list##

def reverse_list(li):
    li.reverse()
    return li
li=[5,7,0,10,9]
print(reverse_list(li))

def reverse_list1(li):
    li=li[::-1]
    return li
li=[5,7,0,10,9]
print(reverse_list1(li))

def reverse_list2(li):
    li1 = []
    for i in li:
        li1 = [i] + li1
        # li1.insert(0,i)  ( ## inbuilt method ) ( we approach this insert method when the answer have to be value based )
    return li1
    
li = [5,7,0,10,9]
print(reverse_list2(li))

def reverse_list3(li):
    li1 = []
    for ind in range(len(li)-1,-1,-1): ## ( we approach this method when the answer have to be value and index values )
      li1 = li1 + [li[ind]]
    return li1

li = [5,7,0,10,9]
print(reverse_list3(li))  
   
## Efficient approach ## ( In Place Reverse )  ( Without Using New List)

def reverse_list4(li):
    low = 0
    high = len(li)-1
    while low < high:
        li[low], li[high] = li[high], li[low]
        low += 1
        high -= 1
    return li
li = [5,7,0,10,9]
print(reverse_list4(li))

def reverse_half_list(li):
    low = 0
    high = (len(li)-1) // 2
    while low < high:
        li[low], li[high] = li[high], li[low]
        low += 1
        high -= 1
    return li
li = [5,7,0,10,9]
print(reverse_half_list(li))

def reverse_half_list1(li):
    low = (len(li)-1) // 2
    high = len(li)-1
    while low < high:
        li[low], li[high] = li[high], li[low]
        low += 1
        high -= 1
    return li
li = [5,7,0,10,9]
print(reverse_half_list1(li))


### Asaignment ###

## Strig Reverse ##
def string_reverse1(word):
    return word[::-1]

print(string_reverse1("python"))

def string_reverse2(word):
    reverse="".join(reversed())
    return reverse

print(string_reverse1("python"))

def string_reverse3(word):
    rev_word=""
    for i in word:
        rev_word = i + rev_word
    return rev_word

print(string_reverse3("python"))

def string_reverse4(word):
    rev_word = ""
    for ind in range(len(word)-1,-1,-1): 
      rev_word = rev_word + word[ind]
    return rev_word

print(string_reverse4("python"))

def string_reverse5(word):
    low = 0
    high = len(word)-1
    while low < high:
        word[low], word[high] = word[high], word[low]
        low += 1
        high -= 1
    return word

print(string_reverse5("python"))

## this code gives an error 

#( string is immutable so item assaignement is not possible )



    
##Sum of digits of each number in the given list. Output should be in list format ##
##[123,345,61,3,45]
def sum_elements_list(li):
    new_list = []
    for i in li:
        sum_i = 0
        while i > 0:
            digit = i % 10
            sum_i += digit
            i = i // 10
        new_list.append(sum_i)
    return new_list

li=[123,345,61,3,45]
print(sum_elements_list(li))

#Find max digit in the given number##
def max_digit(num):
    maximum = 0
    while num > 0:
        digit = num % 10
        if maximum < digit:
            maximum = digit
        elif maximum > digit:
            maximum = maximum
        num = num // 10
    return f"maximum digit is : {maximum}"
print(max_digit(152))


##Find max digit for every number in the given list##

def max_num_list(li):
    for i in li:
        j = i
        new_li = []
        while i > 0:
            digit = i % 10
            new_li.append(digit)
            i = i // 10
        new_li.sort()  
        print(j," :",new_li[-1])  


li=[123,345,61,3,45]
max_num_list(li)

def max_num_list(li):
    for i in li:
        j = i
        maximum = 0
        while i > 0:
            digit = i % 10
            if maximum < digit:
                maximum = digit
            elif maximum > digit:
                maximum = maximum
            
            i = i // 10
        print(j,":",maximum, end=" ,")


li=[123,345,61,3,45]
max_num_list(li)
        



