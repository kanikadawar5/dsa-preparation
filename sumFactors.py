# def factorsSum(num):
#     sum = 0
#     i = 1
#     while i*i <= num:
#         if num % i == 0:
#             sum += i
#             if num // i != i:
#                 sum += num // i
#         i += 1
#     return sum


# print(factorsSum(10))
# print(factorsSum(25))

def factorsSum(num):
    sum = 0
    i = 1
    while i*i <= num:
        if num % i != 0:
            i += 1
            continue

        sum += i
        if num // i != i:
            sum += num // i
        
        i += 1
    return sum


print(factorsSum(10))
print(factorsSum(25))
print(factorsSum(100))
