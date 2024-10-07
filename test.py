import numpy as np

# a = np.array([1,2,3])
# print(a)
# print(type(a))

# A = np.array([[2, 4], [5, -6]])
# B = np.array([[9, -3], [3, 6]])

# # C = A+B
# # print(C)

# C = A.dot(B)
# print(C)

# A = np.array([[1, 1], [2, 1], [3, -3]])
# print(A.transpose())

# A = np.array([[1, 4, 5, 12, 14], 
#     [-5, 8, 9, 0, 17],
#     [-6, 7, 11, 19, 21]])

# print(A[:2, :4]) 

# x = None

# print(x)

# x = None

# if x:
#   print("Do you think None is True?")
# elif x is False:
#   print ("Do you think None is False?")
# else:
#   print("None is not True, or False, None is just None...")

# number = 2
# if number:
#     print(number)

# a = 20
# b = 20

# print('a and b are equal') if a == b else (print('a is greater than b') if a > b else print('b is greater than a'))

# print("Both are equal" if a == b else "a is greater"
#       if a > b else "b is greater")

# print(("a is less", "b is less") [a < b] )


# for x in range(6):
#     print(x)
# else:
#     print("finishes")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)