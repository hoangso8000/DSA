#stack linked list implementation
class Element(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
    def append(self,new_element):
        #this function append an element to the last position of ll  
        #1. run from the head of ll to the tail of ll
        #2. assume the next element "new_element"
        current=self.head
        while current.next !=None:
            current=current.next
        current.next=new_element
    
    def insert_first(self,new_element):
        #this function  insert the element "new_element" to the head of LinkedList
        #1. the first element is changed to the second so we assume it as the next element of "new_element"
        #2. change new_element to head  
        if self.head:
            new_element.next=self.head
        self.head=new_element
    def delete_first(self):
        if self.head:
            self.head=self.head.next    
    def printll(self):
        current=self.head
        while current !=None:
            print(current.value)
            current=current.next
class Stack(object):
    def __init__(self,top=None):
        self.ll=LinkedList(top)
    def push(self, new_element):
        self.ll.insert_first(new_element)
    def pop(self):
        self.ll.delete_fisrt()
    def append(self,new_element):
        self.ll.append(new_element)

# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

stack.ll.printll()
#stack array implementation 
class Stack(object):
    def __init__(self, head=None):
        self.storage = [head]
        
    def push(self, new_element):
        self.storage.append(new_element)
    
    def pop(self):
        self.storage.pop()
    
    def prints(self):
        print(self.storage)

# Start setting up a Stack
stack = Stack(1)
stack.prints()
stack.push(3)
stack.prints()
stack.push(4)
stack.prints()
stack.pop()
stack.prints()