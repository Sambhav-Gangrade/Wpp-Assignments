def utotree(cycle):
    height=1
    for i in range (1,cycle+1):
        if i%2!=0:
            height*=2
        else:
            height+=1
    print("The height of the tree after",cycle,"growth cycles is",height)
list=[]
test=int(input("Enter the number of test cases : "))
for i in range (test):
    a=int(input(f"Enter the number of growth cycles for test case {i+1}: "))
    list.append(a)
print("---------------OUTPUT---------------")
for cycle in list:
    utotree(cycle)
