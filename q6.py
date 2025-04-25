a=int(input("Enter a number : "))
print("the reverse of this number is",end=" ")
while a>0:
    num=a%10
    a=int(a/10)
    print(num,end="")
