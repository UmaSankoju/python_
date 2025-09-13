##Add a Number##
def add_a_num(a):
    li1=[]
    li1=li+[a]
    print(li1)
li=[1,2,3,4,5]
add_a_num(7)

# #Add a numbrt in particuler index##
# def add_a_num(n,li):
#     li1=[]
#     for i in range(len(li)):
#         if i==n:
#             li1=li+[-32]
#         else:
#             li1=li+[li[i]]
#     print(li1)
# li=[1,2,3,4,5,9,10,-45]
# add_a_num(5,li)

def find_elemnet(input_list,input_index):
    if  input_index < -len(input_list) or input_index >= len(input_list):
        
       return "invalid index" 
    else:
        return input_list[input_index]


index=int(input("enter a number:"))
list1=[1,2,3,4,5,-6,10,-45]

print(find_elemnet(list1,index))

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
    
