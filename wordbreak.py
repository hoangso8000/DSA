def wordbreak(word,dict):
    if len(word)==0: yield []
    else: 
        for i  in range(1, len(word)+1):
            sub=word[:i]
            if not sub in dict: continue
            for others in wordbreak(word[i:],dict):
                yield [sub]+others

def wordbreak2(word,dict):
    dict = set(dict)
    for combo in wordbreak(s, words):
        print(" ".join(combo[:]))
s = "godofwar"
dict=open("/home/viethoang/petproject/data_structures_and_algorithm/google-10000-english/google-10000-english.txt","r").read().split("\n")
words = set(dict)
print(wordbreak2(s,words))

def findMissingNumber(arr,n):
    arr.sort()
    l,h=0,n-1
    mid=0
    while(h>l):
        mid = l + (h - l) // 2
        if(arr[mid]-mid==arr[0]):#check xem day co dung tinh chat cac phan tu cach nhau 1 k
            if(arr[mid+1]-arr[mid]>1):#so sanh phan tu giua voi phan tu truoc no
                return arr[mid]+1
            else:
                l=mid+1#phan tu tiep theo
        else:
            if(arr[mid]-arr[mid-1]>1):
                return arr[mid]-1
            else:
                l=mid-1
                
    return -1
arr=[1,2,3,5,6,7,8]
n=len(arr)
print(findMissingNumber(arr,n))