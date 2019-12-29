import time
import os
import sys
sys.setrecursionlimit(1500)
from random import randint
arr=[randint(0,100) for p in range (0,10000)]
def bubbleSort(arr):
    n=len(arr)
    start=time.time()
    for i in range(n,-1,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    end=time.time()
    return arr, end-start

def selection_sort(arr):
    start=time.time()
    n=len(arr)
    for i in range(0,n-1):
        minimum=i
        for j in range(i+1,n):
            if arr[j]<arr[minimum]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]
    end=time.time()
    return arr, end-start

def insertion_sort(arr):
    start=time.time()
    n=len(arr)
    for i in range(0,n):
        temp=arr[i]
        j=i
        while j>0 and temp<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=temp
    end=time.time()
    return arr,end-start

sort_in, insetion_sort_time=insertion_sort(arr)

def merge_sort(arr):
    start=time.time()
    divide(arr,0,len(arr))
    end=time.time()
    return arr, end-start
def divide(arr,start,end):
    if start<end-1:
        mid=(start+end)//2
        divide(arr,start,mid)
        divide(arr,mid,end)
        merge(arr,start,mid,end)
def merge(arr,start,mid,end):
    L=arr[start:mid]
    print(L)
    R=arr[mid:end]
    print(R)
    L.append(1000)
    R.append(1000)
    i=j=0
    for k in range(start,end):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
print(merge_sort([1,2,6,4,5,9,8]))

def quick_sort(arr):
    start=time.time()
    qsort(arr,0,len(arr))
    end=time.time()
    return arr, end-start
def partition(arr,start,end):
    i=start+1
    piv=arr[start]
    for j in range(start+1,end):
        if arr[j]<piv:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[start],arr[i-1]=arr[i-1],arr[start]
    return i-1
def rand_partition(arr,start,end):
    rand = randint(start, end-1)
    arr[rand], arr[start] = arr[start], arr[rand]
    return partition(arr, start, end)
def qsort(arr,start,end):
    if start<end:
        piv_pos=rand_partition(arr,start,end)
        qsort(arr,start,piv_pos)
        qsort(arr,piv_pos+1,end)
print(quick_sort([3,4,5,1,4,6,1,2]))