import numpy as np

# 연습.) 0-5 까지의 정수가 들어있는 2행 3열을 만드세요. 3가지 방법을 제시 하시오
a = [0,1,2,3,4,5]
b = np.array(a)
c = b.reshape(2,3)
print(c)

aa = np.arange(6)
bb = aa.reshape(2,3)
print(bb)

aaa = [[0,1,2],[3,4,5]]
ccc = np.array(aaa)
print(ccc)

arr = np.arange(6).reshape(2,3)
print(arr)

arr4 = np.arange(6).reshape(2,-1)
print(arr4)

arr2 = np.arange(6).reshape(-1,3)
print(arr2)

# a = np.arange(7)
# b = a.shape(2,3)     # 차원을 변경하려면 데이터차수가 맞아야 한다.
# print(a)
# print(b)

# a = np.arange(6)
# b = a.reshape(2,3) # 차수를 변경한다. (차원을 변경한다 1차원 2차원... 배열)
# print(a)
# print(b)
#
# print(a.shape)  # 차원을 확인
# print(b.shape)