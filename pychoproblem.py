list=[4,3,2,1]
print(list)
swap=0
max=list[0]
for i in range(len(list)):
    if list[i]>max:
        max=list[i]
min=list[0]
for i in range(len(list)):
    if list[i]<min:
        min=list[i]
list[0],min=min,list[0]
list.pop(list.index(max))
list.append(max)
for i in range(1,len(list)-1):
    for j in range (i+1,len(list)-1):
        if(list[i]>list[j]):
            list[i],list[j]=list[j],list[i]
            swap+=1
print("Sorted list is : ",list)
print("Number of swaps is ", swap)