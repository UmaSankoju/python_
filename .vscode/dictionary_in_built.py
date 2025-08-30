employee = {
    "id": 21131,
    "name": "nick",
    "department": "IT",
    "salary": 55000,
    "company":"xyz"
}

#To find number of items in dictionary#
print(len(employee))

#Returns dictionary as string#
print(str(employee))

#to check type#
print(type(employee))

#To Access keys#
print(employee.keys())

#To Access values#
print(employee.values())

#To Access key-value#
print(employee.items())

#Add or update keys##
employee.update({"domain": "Software Development"})
print(employee)

##default value##
print(employee.setdefault("age", 27))  
print(employee)  

##removing key##
print(employee.pop("age"))
print(employee)

##removing last inserted pair##
print(employee.popitem())
print(employee)

##deleting all keys in dictionary##
employee.clear()
print(employee)

##copying the dict##
employee = {
    "id": 21131,
    "name": "nick",
    "department": "IT",
    "salary": 55000,
    "company":"xyz"
}

employe=employee.copy()
print(employe)
