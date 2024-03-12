# Find a number that is divisible by maximum array elements and that element should also exist in the array

# def find_number_divisible_max_elements(arr):
#     max_element = max(arr)
#     for i in range(max_element, 0, -1):
#         count = 0
#         for j in arr:
#             if j % i == 0:
#                 count += 1
#         if count == len(arr):
#             return i
#     return -1

# time complexity: O(n * m), where n is the length of the array
#  and m is the maximum element in the array
# solution with reduced complexity is as under

def find_number_divisible_max_elements(arr):
    max_element = max(arr)
    for i in range(max_element, 0, -1):
        if all(j % i == 0 for j in arr):
            return i
    return -1

p = [[3, 4, 6, 8], [1, 2, 3, 4, 5], [2, 4, 8, 16]]
# print (p)