def isSubset(arr1,arr2):
    i=0
    j=0
    arr1.sort()
    arr2.sort()
    if len(arr2)>len(arr1):
        return 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]==arr2[j]:
            i+=1
            j+=1
        elif arr1[i]>arr2[j]:
            return 0
    return False if j<len(arr2) else True
# print(isSubset([1,2,3,4],[1,2])   


def largestSquare(M):
    R=len(M)
    C=len(M[0])
    S=[[0 for k in range(C)]for l in range(R)]
    for i in range(1,R):
        for j in range(1,C):
            if M[i][j]==1:
                S[i][j]=min(S[i][j-1],S[i-1][j-1],S[i-1][j])+1
            else:
                S[i][j]=0
    max_of_s=S[0][0]
    max_i=0
    max_j=0
    for i in range(R):
        for j in range(C):
            if(max_of_s<S[i][j]):
                max_of_s=S[i][j]
                max_i=i
                max_j=j
    print("Maximum size sub-matrix is: ") 
    for i in range(max_i, max_i - max_of_s, -1): 
        for j in range(max_j, max_j - max_of_s, -1): 
            print (M[i][j], end = " ") 
        print("")
        
M = [[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0]] 
# largestSquare(M)

class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
def isIdentical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return(root1.data==root2.data 
        and isIdentical(root1.left,root2.left)
        and isIdentical(root1.right,root2.right))
def isSubTree(T,S):
    if S is None:
        return True
    if T is None:
        return False
    if(isIdentical(T,S)):
        return True
    return isSubTree(T.left,S) or isSubTree(T.right,S)
T=Node(26)
T.left=Node(20)
T.left.left=Node(10)
T.left.left.right=Node(5)
T.right=Node(20)
S=Node(20)
S.left=Node(10)
S.left.right=Node(5)
# print(isSubTree(T,S))
def printLogestIncSubArr( arr, n) : 
  
    # 'max' to store the length of longest 
    # increasing subarray 
    # 'len' to store the lengths of longest 
    # increasing subarray at diiferent  
    # instants of time 
    m = 1
    l = 1
    maxIndex = 0
       
    # traverse the array from the 2nd element 
    for i in range(1, n) : 
  
        # if current element if greater than previous 
        # element, then this element helps in building 
        # up the previous increasing subarray  
        # encountered so far 
        if (arr[i] > arr[i-1]) : 
            l =l + 1
        else : 
  
            # check if 'max' length is less than the length 
            # of the current increasing subarray. If true,  
            # then update 'max' 
            if (m < l)  : 
                m = l      
                maxIndex = i - m     
            l = 1    
          
          
    # comparing the length of the last 
    # increasing subarray with 'max' 
    if (m < l) : 
        m = l 
        maxIndex = n - m 
      
    # Print the elements of longest 
    # increasing contiguous subarray.  
    for i in range(maxIndex, (m+maxIndex)) : 
        print(arr[i] , end=" ") 
    print(l,m,maxIndex)
# Driver program to test above 
arr = [5, 6, 3, 5, 7, 8, 9, 1, 2] 
n = len(arr) 
# printLogestIncSubArr(arr, n) 

