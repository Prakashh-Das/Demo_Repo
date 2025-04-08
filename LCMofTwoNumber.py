num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# def multiple(num):
#     multiples = []
#     for i in range(1, 11):
#         multiples.append(num * i)
#     return multiples


# multi1 = multiple(num1)
# multi2 = multiple(num2)


# common_multi = multi1[-1]

# for i in multi1:
#     for j in multi2:
#         if i == j and i < common_multi:
#             common_multi = i


greater = max(num1, num2)

common_multi = 0

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        common_multi = greater
        break
    greater += 1
    
print(f"The least common multiple of {num1} and {num2} is {common_multi}")




a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


    
    
    
