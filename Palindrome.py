user_input = input("Enter a number: ")

rev_str = ''

for char in user_input:
    rev_str = char + rev_str
    
if user_input == rev_str:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    
# rev_str = ''
# index = len(user_input) - 1

# while index >= 0:
#     rev_str += user_input[index]
#     index -= 1

# if user_input == rev_str:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")