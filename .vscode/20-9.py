list1 = [202, 89, 112, 88]
result_list = []
for i in list1:
    duplicate_list = []
    flag = False
    while i > 0:
        digit = i % 10
        if digit in duplicate_list:
            flag = True
            break
        else:
           duplicate_list.append(digit)
        i = i // 10  
    result_list.append(flag)
    
print(result_list)


## Sum Of all Numbers In a Matrix ##

list2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
sum_elements = 0
for i in list2:
    for j in i:
        sum_elements += j
        
print(sum_elements)