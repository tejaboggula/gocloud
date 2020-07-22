# for index in range(5):
#     if index == 0:
#         print("first iteration")
#     else:
#         print("next iteration")

def power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(power(10, 3))