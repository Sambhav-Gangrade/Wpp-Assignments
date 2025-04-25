def checksquare(a,b):
    list=[]
    for i in range (a,b+1):
        list.append(i)
    sqrlist=[]
    for i in range(1,int(b**0.5)+1):
        sqrlist.append(i**2)
    for i in range (len(sqrlist)):
        if sqrlist[i] in list:
            print(sqrlist[i],end=" ")
a=int(input("Enter a starting point : "))
b=int(input("Enter an ending point : "))
checksquare(a,b)