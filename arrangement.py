unit=[]
for i in range(0,24):
    unit.append(0)
num=int(input("number of arangement"))
start=[]
end=[]
for i in range(0,num):
    a=int(input("Start of"+str(i)+ ":"))
    b=int(input("End of"+str(i)+ ":"))
    for i in range(a,b+1):
        unit[i]=unit[i]+1
print(max(unit))