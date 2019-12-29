#first missing positive
#ý tưởng nếu một phần tử nguyên dương của mảng không đúng vị trí: 1 thì phải ở phần từ 0 ................ thì tiến hành đổi chỗ
def firstMissingPos(nums):
    i=0
    while i<len(nums):
        while nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        i+=1
    for i,num in enumerate(nums):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1
# result=firstMissingPos([1,3,56,7,2])
# print(result)
#implement binary search to find peek: ....<a[i-1<a[i]>a[i+1]...
def solve(nums):
    left,right=1,len(nums)
    # print(left,right)
    while left <right:
        mid=(left+right)//2
        # print(mid)
        if nums[mid+1]<nums[mid]:
            right=mid
        else:
            left=mid+1
    return nums[left]

print(solve([1,243,5,4,3,2,1]))
# wordbreak II
class wordBreakTwo():
    def canBreak(self,s,wordDict):
        can_make=[False]*(len(s)+1)
        can_make[0]=True
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if can_make[j] and s[j:i]:
                    can_make[i]=True
                    break 
        return can_make[-1]
    def wordBreak(self,s,wordDict):
        if not self.canBreak(s,wordDict):
            return []
        result_lists=self.break_word(s,0,wordDict,{})
        print(result_lists)
        return [" ".join(result) for result in result_lists]
    def break_word(self,s,left,wordDict,memo):
        if left>=len(s):
            return [[]]
        if left in memo:
            return memo[left]
        results=[]
        for i in range(left+1,len(s)+1):
            prefix=s[left:i]
            suffix_breaks=self.break_word(s,i,wordDict,memo)
            if suffix_breaks and prefix in wordDict:
                for suffix_break in suffix_breaks:
                    results.append([prefix]+suffix_break)
                    
# print(wordBreakTwo().wordBreak("universityofscience",["uni","university","sci","science"]))
#shortestworddistance
def shortestWordDistance(words,word1,word2):
    shortest=len(words)
    i_1,i_2=float("-inf"),float("-inf")
    for i,word in enumerate(words):
        if word==word1:
            i_1=i
            shortest=min(shortest,i_1-i_2)
        if word==word2:
            i_2=i
            shortest=min(shortest,i_2-i_1)
    return shortest
print(shortestWordDistance(["hoang","hi","ha","hi","ha","hi","hi"],"hoang","hi"))
#shortestworddistance
from collections import defaultdict
class wordDistance:
    def __init__(self,words):
        self.word_indices=defaultdict(list)
        for i, word in enumerate(words):
            self.word_indices[word].append(i)
    def shortest(self,word1,word2):
        i1=self.word_indices[word1]
        i2=self.word_indices[word2]
        distance=float("inf")
        p1,p2=0,0
        while p1<len(i1) and p2 < len(i2):
            distance=min(distance,abs(i1[p1]-i2[p2]))
            if i1[p1]<i2[p2]:
                p1+=1 
            else:
                p2+=1 
        return distance
ex_1=wordDistance(["hoang","hi","ha","hi","ha","hi","hi"]).shortest("hoang","hi")
print(ex_1)
#jobschedule 
def printJobScheduling(arr,t):
    n=len(arr)
    #sort all job according to its profit 
    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2]<arr[j+1][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    #keep track free time slots
    result=[False]*t 
    #store result
    job=['-1']*t 
    for i in range(n):
        #find free slots for this job(we start from the last possible slot)
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            #free slot found
            if result[j] is False:
                result[j] =True
                job[j]=arr[i][0]
                break
    print(job)
# Driver COde 
arr = [['a', 2, 100], # Job Array 
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 
  
  
print("Following is maximum profit sequence of jobs") 
printJobScheduling(arr, 1) # Function Call 