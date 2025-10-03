## Check if a number is even or odd.##
def check_even_odd(num):
    return "even" if num % 2 == 0 else "odd"
print(check_even_odd(5))

##  Find the maximum and minimum element in a list. ##
def max_min_list(list1):
    maximum = list1[0]
    minimum = list1[0]
    for i in list1:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return minimum, maximum
print(max_min_list([1, 4, 7, -4, 6, 0]))

##  Reverse a string without using slicing  ##
def rev_string(word):
    rev = ""
    for char in word:
        rev = char + rev
    return rev
print(rev_string("python"))

##  Check if a string is a palindrome. ##
def check_palindrome(word):
    return "Palindrome" if word == word[::-1] else "Not a Palindrome"
print(check_palindrome("madam"))

##  Find the factorial of a number (using loop). ##
def fact(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact
print(fact(5))

##  Count the frequency of each character in a string.##
def freq_string(word):
    freq = {}
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(freq_string("madam"))

##  Find the second largest number in a list. ##
def second_largest_num(list1):
    list1.sort()
    return list1[-2]
print(second_largest_num([1, 4, -5, 4, 65, 205, 344]))

##  Count how many vowels and consonants are in a string. ##
def count_vowel_constant(word):
    vowel = "AEIOUaeiou"
    vowel_count = 0
    const_count = 0
    for char in word:
        if char in vowel:
            vowel_count += 1
        else:
            const_count += 1
    return vowel_count, const_count
print(count_vowel_constant("python"))

##  Calculate the sum of digits of a number. ##
def sum_digits(num):
    sum_digits = 0
    while num > 0:
        digit = num % 10
        sum_digits += digit
        num = num // 10
    return sum_digits
print(sum_digits(255))

## Print the multiplication table of a number. ##
def table_of_num(num):
    for i in range(1,11):
        print(num, "X", i , "=", num * i)
table_of_num(5)

##  Find the largest word in a given sentence. ##
def largest_sentence(sentence):
    words = sentence.split()
    largest = ""

    for word in words:
        if len(word) > len(largest):
            largest = word

    print("Largest word:", largest)
    print("Length:", len(largest))
largest_sentence("python developers often use list comprehensions and decorators to write efficient code.")

##  Remove all duplicate elements from a list. ##
def remove_duplicates(list1):
    print(list(set(list1)))
remove_duplicates([1, 5, 9, 56, 2, 1, 56, 2, 9])

##  Sort a list without using Python’s built-in sort ##
def sort_list(list1):
    
    falg = False
    for i in range(0, len(list1)-1):
        for j in range(0, len(list1)-1-i):
            if list1[j] < list1[j+1]:
                falg = True
                list1[j], list1[j+1] = list1[j+1], list1[j]
        if falg == False:
            break
    list1.reverse()  
    print(list1)
sort_list([-4, 78, 23, 67, 12, 678, 0])

## Merge two lists into a single sorted list ##
def merge_lists(list1, list2):
    merged_list = sorted(list1 + list2)
    print(merged_list)
merge_lists([1, 4, 6, 90], [0, 23, 55, 21, 9])

##  Check if a number is a prime number. ##
def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not a Prime")
                break
        else:
            print("Prime")
check_prime(79)

