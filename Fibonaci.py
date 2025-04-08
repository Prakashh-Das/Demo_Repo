
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_sequence(n):
    flag = True
    num1 = 0
    num2 = 1
    print(num1, num2, end=" ")
    while flag:
        num3 = num1 + num2
        if num3 >= n:
            flag = False
            break
        print(num3, end=" ")
        num1, num2 = num2, num3
        
    
    

    
if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    
    # for i in range(1, user_input+1):
    #     print(fibonacci(i), end=" ")
    
    fibonacci_sequence(user_input)
    
    print("\nFibonacci sequence generated successfully.")