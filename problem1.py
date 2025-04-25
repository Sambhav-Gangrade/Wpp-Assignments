
user_input = input("Enter a string: ")
list = list(user_input)

for temp in range(len(list)):
    if temp % 2 != 0:
        list[temp] = list[temp].upper() 

print("Processed string:", str(list))
