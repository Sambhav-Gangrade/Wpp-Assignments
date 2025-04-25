def checkfibo(num):
    list=[0,1]
    for i in range (1,100):
        if (list[i-1]+list[i])<=num:
            list.append(list[i-1]+list[i])
        else:
            break
    print(list)
    if num in list:
        print(f"{num} IsFibo")
    else:
        print(f"{num} IsNotFibo")
num=int(input("Enter a number of choice : "))

checkfibo(num)
