#feet into inches   12
#feet into yards    0.3
#feet into miles    0.0001893939
#feet into millimeters  304.8
#feet into centimeters  30.48
#feet into meters   0.3048
#feet into kilometers   0.0003048
conversion_list=[12,0.3,0.0001893939,304.8,30.48,0.3048,0.0003048]
conversionvalue_list=["inches","yards","miles","millimeters","centimeters","meters","kilometers"]
print("Enter 1 to convert feet into inches")
print("Enter 2 to convert feet into yards")
print("Enter 3 to convert feet into miles")
print("Enter 4 to convert feet into millimeters")
print("Enter 5 to convert feet into centimeters")
print("Enter 6 to convert feet into meters")
print("Enter 7 to convert feet into kilometers")
value=float(input("Enter a value in feet : "))
a=int(input("Enter a number between 1 to 7 : "))
print("The conversion of feet into",conversionvalue_list[a-1],"is",value*conversion_list[a-1],conversionvalue_list[a-1])