list1 =  [10, -3, 23, 45, 700, -300]
falg = False
for i in range(0, len(list1)-1):
    for j in range(0, len(list1)-1-i):
        if list1[j] > list1[j+1]:
            falg = True
            list1[j], list1[j+1] = list1[j+1], list1[j]
    if falg == False:
        break
    
    print(list1)
    
    
list1 = [10, -3, 23, 45, 700,5, 5, -300]
searc_element = 5
flag = False
for i in range(len(list1)):
    if list1[i] == searc_element:
        flag = True
        print(i)
if flag == False:
    print("not found")
    
    
# Assignment:
# Can you wrtie bubble sort for decending order

list1 = [56, -43, 67, -2, 902, -55, 77]
falg = False
for i in range(0, len(list1)-1):
    for j in range(0, len(list1)-1-i):
        if list1[j] < list1[j+1]:
            falg = True
            list1[j], list1[j+1] = list1[j+1], list1[j]
    if falg == False:
        break
    
    print(list1)
    
    
##Use bubble sort to sort strings based on their lengths. That is strings with highest length should go to last##

str_list = ["python","web-development", "HTML","CSS","DJango"]
for i in range(0,len(str_list)-1):
    for j in range(0,len(str_list)-1-i):
        if len(str_list[j]) > len(str_list[j+1]):
            str_list[j], str_list[j+1] = str_list[j+1], str_list[j]
        
    print(str_list)
    
    
### Can you sort nested lists based on the first element of each nested list.

nested_list = [[1, 56], [5,79], [3,86], [13,42], [7,5]]


for i in range(0, len(nested_list)-1):
    for j in range(0, len(nested_list)-1-i):
        if nested_list[j][0] > nested_list[j+1][0]:
            nested_list[j][0], nested_list[j+1][0] = nested_list[j+1][0], nested_list[j][0]
            
    print(nested_list)