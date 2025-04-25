test_cases=int(input("Enter the number of test cases : "))
list=[]
for i in range(test_cases):
    a=int(input("Enter the number : "))
    list.append(a)
print(list)

for i in list:
    temp=i
    count=0
    while i>0:
        num=i%10
        i=int(i/10)
        if num!=0:
            if temp%num==0:
                count+=1
    print(count)