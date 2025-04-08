user_input = int(input("Enter a number: "))

def factorial(num):
    if num == 0:            
        return 1
    else:
        return num * factorial(num - 1)
    
print(f"The factorial of {user_input} is {factorial(user_input)}")




    