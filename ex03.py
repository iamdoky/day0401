import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')   # class 'pandas.core.frame.DataFrame'
csv_data = csv[["sepal.length","sepal.width","petal.length","petal.width"]]
csv_label = csv["variety"]

train_data,test_data,train_label,test_label = train_test_split(csv_data,csv_label)

clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

score = metrics.accuracy_score(test_label,pre)

realdata = [[5.7,2.8,4.5,1.3]]
result = clf.predict(realdata)

# 사용자 한테 꽃받침의 길이, 꽃받침의 넓이, 꽃잎의 길이, 꽃잎의 넓이를 입력받아
# 붓꽃의 품종을 알아 맞추는 웹어플리케이션을 작성해 보니다


