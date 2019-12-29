def linearSearch(data,value):
    index=0
    step=0
    while index<len(data) and data[index]<value:
        index+=1
        step+=1
    if index>len(data) and data[index]!=value:
        return -1,step
    return index, step
def Binary_search(data,value):
    if value >data[-1] or value<data[0]:
        return -1,1
    low=0 
    high=len(data)-1
    step=0
    while low<=high:
        mid=(low+high)//2
        if data[mid]==value:
            return mid,step
        elif data[mid]<value:
            low=mid+1
        else:
            high=mid-1 
        step+=2
    return -1,step