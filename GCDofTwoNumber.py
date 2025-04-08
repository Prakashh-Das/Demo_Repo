num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

divisors1 = divisor(num1)
divisors2 = divisor(num2)   

common_divisors = 0

for i in divisors1:
    for j in divisors2:
        if i == j:
            common_divisors = i
            if i > common_divisors:
                common_divisors = i
            
print(f"The greatest common divisor of {num1} and {num2} is {common_divisors}")