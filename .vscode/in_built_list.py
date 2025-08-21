li=[24,56,78,90,55]
print("append")
li.append(57)
li.append([5,7])
print("Edge cases:\nAdds a single element at the end.\nworks with any object (number, string, list, dict, even None).\nNo major errors unless memory runs out.")
print("extend")
li1=[24,56,78,90,55]
li1.extend([57,75])
print(li1)
print("Edge cases:\nAdds each element of iterable to the end.\nworks with any iterable (list, tuple, string, set).\nRaises TypeError if argument is not iterable.")
print("insert")
li2=[24,56,78,90,55]
li2.insert(4,57)
print(li2)
print("Remove")
li3=[24,56,78,90,55]
li3.remove(78)
print(li3)
print("Removes the first occurrence of x.\nIf multiple exist, only first is removed.\nRaises ValueError if element not found.")
print("pop")
li4=[24,56,78,90,55]
li4.pop(2)
print(li4)
print("Removes and returns element at index i.\nDefault removes last element if index not given.\nRaises IndexError if list is empty or index is out of range.")
print("Clear")
li5=[24,56,78,90,55]
li5.clear()
print(li5)
print("Count")
li6=[24,56,78,90,55]
print(li6.count(55))
print("Returns how many times x appears.\nAlways works, even if x not in list.\nNo error cases ()")
print("Reverse")
li7=[24,56,78,90,55]
li7.reverse()
print(li7)
print("Max")
li8=[24,56,78,90,55]
print(max(li8))
print("Min")
li9=[24,56,78,90,55]
print(min(li9))
print("Sum")
li10=[24,56,78,90,55]
print(sum(li10))