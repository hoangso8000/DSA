# #prob1_2sum
class week1:
    def twoSum(nums,target):
        num_to_index={}
        for i,num in enumerate(nums):
            if target-num in num_to_index:
                return[num_to_index[target-num],i]
        num_to_index[num]=i
        return [] 
# print(week1().twoSum([1,2,3,4,5,6],4))
#prob2 delete all duplicate ele in linkedlist
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def deleteAllDuplicate(self,head):
        while node and node.next:
            if node.val==node.next.val:
                node.next=node.next.next
            else:
                node=node.next
        return head
#prop3 Roman to Integer
# def romanToInt(s):
# 	doubles={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
# 	singles={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
# 	integer=0
# 	i=0
#     while i<4:
#         if i<len(s) and s[i:i+2] in doubles:
#             integer+=doubles[s[i:i+2]]
#             i+=2
#         else:
#             integer+=singles[s[i]]
#             i+=1  
#     return integer
#prob4 Integer to Roman
def intToRoman(num):
    mapping=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    roman=[]
    for i,numeral in mapping:
        while num>i:
            num-=i
            roman.append(numeral)
    return "".join(roman)
print(intToRoman(1823))
#prob5 detectCapitalUse
def detectCapitalUse(word):
    if len(word)<=1:
        return True
    first=word[0]<='Z'
    second=word[1]<='Z'
    if not first and second:
        return False
    for c in word[2:]:
        if(c<='Z')!=second:
            return False
    return True
print(detectCapitalUse('VietHoang'))
#Remove LinkedlistElement
class listNode(object):
    def __init__(self,x):
        self.val=x 
        self.next=None
class Solution(object):
    def removeElement(self,head,val):
        dummy=prev=listNode(None)
        dummy.next=head
        while head:
            if head.val==val:
                prev.next,head.next,head=head
            else:
                prev,head=head,head.next 
        return dummy.next
    
ele_first=listNode(1)
ele_sec=listNode(2)