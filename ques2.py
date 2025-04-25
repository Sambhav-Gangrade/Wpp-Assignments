import random
list=[]
for i in range (0,100):
    list.append(random.randint(0,1))

print(list)
max=0
count=0
for i in range(len(list)):
    if list[i]==1:
            count=0
            continue
    if list[i]==0:
        count+=1
        if (max<count):
            max=count
        
        

print("The maximum number of zeros appearing together in the following list is",max)