from sklearn import svm, metrics
import random, re
# csv 파일 가공
csv = []
with open('iris.csv','r',encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        fn = lambda n: float(n) if re.match('^[0-9\.]+$',n) else n
        cols = list(map(fn,cols))
        csv.append(cols)
# 첫 행 제거
del csv[0]
# csv를 섞어준다.
random.shuffle(csv)

total_len = len(csv)
train_len = int(total_len*2/3)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]

    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("정답률: ",ac_score)

# 문제를 주어 답을 찾는?
real_data = [[5.9,3,4.2,1.5]]

result = clf.predict(real_data)
print(result)
