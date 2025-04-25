def min_operations_to_palindrome(s):
    operations = 0
    n = len(s)
    for i in range(n // 2):
        left_char = s[i]
        right_char = s[n - i - 1]
        operations += abs(ord(left_char) - ord(right_char))
    return operations
T = int(input())
for _ in range(T):
    s = input("Enter a number : ") 
    print(min_operations_to_palindrome(s))  
