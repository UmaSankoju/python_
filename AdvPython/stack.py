#stack = last in first out & first in last out

# push , pop, peek(), size, is_empty()


class Stack:
    def __init__(self):
        self.inner_list = []
        print("stack is created")
    
    def push(self, elem):
        self.inner_list.append(elem)  
        
        
    def size(self):
        return len(self.inner_list)
    
    def is_empty(self):
        return len(self.inner_list) == 0   
    
    def peek(self):
        if self.is_empty():
            raise Exception("No elements in the stack")
        last_ind = len(self.inner_list) - 1
        return self.inner_list[last_ind]
    
    def pop(self):
        if self.is_empty():
            raise Exception("No elements in the stack")
        return self.inner_list.pop()