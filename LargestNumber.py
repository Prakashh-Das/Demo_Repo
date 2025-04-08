
user_input = list(map(int, input("Enter a number: ").split()))
max_num = user_input[0]
# for i in user_input:
#     for j in user_input:
#         if i != j:
#             if i > j and j > max_num:
#                 max_num = i

for i in user_input[1:]:
    if i > max_num:
        max_num = i
                
print(f"The largest number is {max_num}")