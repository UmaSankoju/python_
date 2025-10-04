## Find all pairs in a list that sum up to a target value. ##
def find_pairs(list1, target):
    for i in range(len(list1)):
        for j in range( i + 1, len(list1)):
            if list1[i] + list1[j] == target:
                return list1[i], list1[j]

print(find_pairs([1, 5, 7, 9, 0, 3, 4], 10))

##  Implement a program to rotate a list by k positions. ##
def rotate_list(list1, k):
    k = k % len(list1)
    return list1[-k:] + list1[:-k]
print(rotate_list([1, 3, 6, 8, 3, 7], 4))

## Find the missing number in a list of consecutive integers. ##
def missing_number(list1):
    list1.sort()
    low = list1[0]
    high = list1[-1]
    for i in range(low, high):
        if i not in list1:
            print(i, end = " ")
missing_number([1, 6, 8, 2, 4, 20])

##  Check if two strings are anagrams. ##
def check_anagram(word1, word2):
    if len(word1) == len(word2):
        freq1 = {}
        freq2 = {}
        for char in word1:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1
        for char in word2:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1
        if freq2 == freq1:
            print("anagrams")
        else:
            print("not an anagram")
check_anagram("earth", "heart")

##  Count the number of words in a sentence. ##
def count_words(sentence):
    words = sentence.split()
    count = 0
    for i in words:
        count += 1
    return count
print(count_words(" Count the number of words in a sentence."))

## Remove all duplicate words from a sentence ##
def remove_duplicates(sentence):
    words = sentence.split()
    result = []
    for i in words:
        if i not in result:
           result.append(i) 
    return " ".join(result)
print(remove_duplicates("The cat chased the mouse because the cat was hungry."))

##  Given a dictionary, invert it (keys become values). ##
def inverted_dict(dict):
    inverted_dict = {}
    for key, value in dict.items():
        inverted_dict[value] = key
    return inverted_dict

dict = {
    'John': 'Math',
    'Alice': 'Science',
    'Bob': 'English',
    'Eve': 'Math' }

print(inverted_dict(dict))

##  Find the intersection of two lists. ##
def intersect_lists(list1, list2):
   intersect_list = []
   for i in list1:
       for j in list2:
           if i == j and i not in intersect_list:
               intersect_list.append(i) 
   return intersect_list
list1 = [1, 7, 8, 9, 23, 5]
list2 = [2, 4, 7, 10, 5]
print(intersect_lists(list1, list2))

##  Print the transpose of a matrix. ##
def transpose_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    return matrix
matrix = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(transpose_matrix(matrix))

## Implement bubble sort.##
def bubble_sort(list1):
    falg = False
    for i in range(0, len(list1)-1):
        for j in range(0, len(list1)-1-i):
            if list1[j] < list1[j+1]:
                falg = True
                list1[j], list1[j+1] = list1[j+1], list1[j]
        if falg == False:
            break
        
        print(list1)
    
list1 = [5, -88, 67, -25, 10, 55, 7]
bubble_sort(list1)
    
##  Find the first non-repeating character in a string.##
def first_non_repeating_char(word):
    for char in word:
        if word.count(char) == 1:
            print(char)
            break
            
first_non_repeating_char("hewihwi")

##  Find the longest word in a sentence. ##
def longest_word(sentence):
    words = sentence.split()
    result = []
    for word in words:
        result.append(word)
    longest = result[0]
    for i in range(len(result)):
        if len(result[i]) > len(longest):
            longest = result[i]
    print(longest)
longest_word("programming in python is fun")

##  Find the second smallest number in a list. ##
def second_small_num(list1):
    falg = False
    for i in range(0, len(list1)-1):
        for j in range(0, len(list1)-1-i):
            if list1[j] < list1[j+1]:
                falg = True
                list1[j], list1[j+1] = list1[j+1], list1[j]
        if falg == False:
            break
    return list1[-2]
print(second_small_num([1, 6, 8, 2, 4, 20]))

##  Implement a program to check if a number is an Armstrong number.##
def check_armstrong(num):
    flag = False
    temp = num
    sum_num = 0
    n = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum_num += digit ** n
        temp = temp // 10
    if sum_num == num:
        flag = True
    return flag
print(check_armstrong(153))