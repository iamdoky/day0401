import numpy as np
a = [1,3,5,7,9]
b = [0,2,6,8,8]

# Vector Operation
arr1 = np.array(a)
arr2 = np.array(b)
c = arr1 + arr2
print(c)

s = arr1 > arr2
print(s)

k = arr1 ** 2   # 제곱을 한다.
m = arr1 > 5    # booleand
print(k)
print(m)

d = arr1 + 1    # 브로드캐스팅
print(d)

# a = [1,3,5,7,9]
# b = [2,4,6,8,10]
# c = a + b
# print(c)  결과 : [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]