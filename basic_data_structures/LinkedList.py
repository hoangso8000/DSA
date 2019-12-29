class Element(object):
    def __init__(self,value):
        self.value = value
        self.next=None

class LinkedList(object):
    def __init__(self,head=None ):
        self.head=head
    def append(self,new_element):
        # add new_Element to the tail of linkedList
        # 1. attach head of LinkedList to current 
        # 2. if head of ll is not None, go to the last element of linkedList then attach next to that element with new_Element
        # 3. if head of ll is None then attach head of ll with new_Element
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=new_element
        else:
            self.head=new_element
    def get_position(self,position):
        #this func return the element with the positon "position" in linkedList. Supposed the first position is "1". Return None if position is not in linkedList
        #1.attach postion 1
        #2.current element is head of linked
        #3.if position <1 which means linkedList not exist -> return None 
        #4. while "currrent" is not None and the current position <= position "position" then if counter==position then return element at counter or else attach current with the next element and then increase counter +1
        counter=1
        current=self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    def insert(self, new_element, position):
        # '''
        # Nếu position là 3 thì new_element sẽ được insert
        # giữa vị 2 và 3 cũ, nghĩa là thành element 3 mới, element 3 cũ 
        # sẽ thành element 4.
        
        # 1. Gắn vị trí là 1
        # 2. Element hiện tại là head
        # 3. Nếu vị trí cần chèn >1 thì sẽ chạy current đến 
        # element position-1
        # 4. Gắn element next của new_element là element cũ tại position,
        # gắn element next của element tại position-1 là new_element
        # 5. Nếu position muốn insert là vị trí đầu tiên thì chỉ việc 
        # gắn element next của new_element là head rồi gắn lại head là
        # new_element
        # '''
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    def delete(self,value):
        #this func  will te first element with the value equal to the expected delete value
        #1.attach the current element "head", before head there is no element then you should assume previous None
        #2.While next element is not None, find the first value with "value"
        #3.If finding the element with value="value" then we consider 2 cases:
        #case 1: previous is not None which means we find the element is not head so we assume element next of previous with the value=next of current.
        #case 2: curent is head so just assume head with the element "next" of current
        current=self.head
        previous=None
        while current.value !=value and current.next:
            previous=current
            current=current.next
        if current.value==value:
            if previous:
                previous.next=current.next
            else:
                self.head=current.next
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# # Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
