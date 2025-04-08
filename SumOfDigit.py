user_input = int(input("Enter a number: "))

def sum_of_digit(n):
    sum = 0
    while n > 0:     
        sum += n % 10
        n //= 10
    return sum

print(f"Sum of digits of {user_input} is {sum_of_digit(user_input)}")