class Queue:
    def __init__(self,head=None):
        self.storage=[head]
    def enqueue(self,new_element):
        self.storage.append(new_element)
    def peek(self):
        return self.storage[0]
    def dequeue(self):
        return self.storage.pop(0)
    def printq(self):
        print(self.storage)
#Setup
q=Queue(1)
q.enqueue(2)
q.enqueue(3)

q.printq()
print(q.peek())
q.printq()

print(q.dequeue())
q.printq()
print(q.dequeue())
q.printq()
print(q.peek())
q.printq()
#Queue LinkedList Implementation
class Element(object):
    def __init__(self,value):
        self.value=value
        self.next=None 
class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
        self.tail=head
    def insert_last(self,new_element):
        #this function add element "new_element" to the tail of LinkedList
        # concatenate current tail with new_element
        # change tail to new_element
        if self.tail:
            self.tail.next=new_element
        self.tail=new_element
        
    def delete_first(self):
        if self.head:
            self.head=self.head.next
    def printll(self):
        current=self.head
        while current !=None:
            print(current.value)
            current=current.next
class Queue(object):
    def __init__(self,top=None):
        self.ll=LinkedList(top)
    def enqueue(self,new_element):
        self.ll.insert_last(new_element)
    def dequeue(self):
        self.ll.delete_first()
    def printq(self):
        self.ll.printll()

# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
q = Queue(e1)
q.enqueue(e3)
q.enqueue(e4)

q.printq()
q.dequeue()
q.printq()