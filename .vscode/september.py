list1 = [10, 20, 30, 10, 10]
dict1 ={}
for i in list1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)
print("unique elements:")
for key, value in dict1.items():
    if value == 1:
        print(key,)
    
    
list2 = ["red", "green", "purple", "red", "black","green", "red"]
dict2 = {}
for i in list2:
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i] += 1
for key, value in dict2.items():
    if value % 2 == 0:
        print("using this", key, "you can sustained")


num1 = 34571
list1 = []
while num1 > 0:
    digit = num1 % 10
    list1.append(digit)
    num1 = num1 // 10
    
for i in range(min(list1), max(list1)+1):
    if i  not in list1:
        print(i)
        

list3 = [[1, 2, 3], [-3, 4, 5, 6], [42, 33]]
sum = 0
for i in list3:
    for j in i:
        sum += j
        
    print(sum)
    
list4 = [20, 15, 26, 2, 98, 6]
list5 = sorted(list4)
list6 = []
for i in list4:
    for j in  range(len(list5)):
        if i == list5[j]:
            list6.append(j+1)
            break
print(list6)

##In-Built
list7 = []
for i in list4:
    list7.append(list5.index(i)+1)
            
print(list7)

### Nested lists ###
## Replacing All Elements With Zer0 ##

list1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
for i in range(len(list1)) :
    for j in range(len(list1)):
        list1[i][j] = 0      
print(list1)
## Sum Of Elements in Each list In Nested list ##
list2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
list3 = []
for i in range(len(list2)):
    sum_n = 0
    for j in list2[i]:
        sum_n += j
    list3.append(sum_n)
print(list3)
## Replacing Daigonal Elements With Zero ##
list4 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
for i in range(len(list4)):
    for j in range(len(list4)):
       if i == j:
           list4[i][j] = 0
print(list4)
## Replacing Reverse Diagonal Elements with zero ##
list5 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
for i in range(len(list5)):
      list5[i][len(list5)-1-i] = 0
print(list5)

## Replacing all Diagonal Elements with Zero ##

list6 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
n = len(list6)
for i in range(n):
    list6[i][n-1-i] = 0
    for j in range(n):
        if i == j:
            list6[i][j] = 0
print(list6)


list7 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
n = len(list7)
for i in range(n):
    list7[i][n-1-i] = 0
    list7[i][i] = 0
print(list7)


