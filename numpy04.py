import numpy as np

# 연습) 1차원으로 변경해 보니다.
arr = [[1,2,3,],[4,5,6]]
a = list(np.array(arr).reshape(6))
b = np.array(arr).reshape(-1,6)
print(b)
print(type(a))
print(type(b))

