import numpy as np

# 브로드캐스팅 / 배열의 숫자만큼 연산을 한다.
arr = [1,2,3,4,5,6]
a = np.array(arr)
b = a+1
print(b)

# 불가
# a = [1,2,3,4,5,6]
# b =a+1
# print(b)