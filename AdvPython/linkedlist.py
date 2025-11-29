class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(5)
n2 = Node(3)
head.next = n2

def display_li(head):
    if head == None:
        return
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next
display_li(head)

def add_new_node_start(head, new_node_data):
    new_node = Node(new_node_data)
    new_node.next = head
    return new_node   # return new head
head = add_new_node_start(head, 7)
display_li(head)

def delete_node(head, del_data):
    temp = head
    prev = None
    while temp != None:
        if temp.data == del_data:
            prev.next = temp.next
            return
        
        prev = temp
        temp = temp.next  
        
delete_node(head, 3) 
display_li(head)


# print(sys.getrefcount(a))