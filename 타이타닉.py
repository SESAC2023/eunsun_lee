import pandas as pd

# train.csv 파일을 로드합니다.
train_data = pd.read_csv("train.csv")

train_data['Pclass'] = train_data['Pclass'].fillna(0)
train_data['Sex'].fillna(0)
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data['Fare'].fillna(train_data['Fare'].median(), inplace=True)
train_data['Embarked'] = train_data['Embarked'].map({'S': 0, 'C': 1, 'Q' : 2})
train_data.dropna(subset=['Embarked'])

# test.csv 파일을 로드합니다.
test_data = pd.read_csv("test.csv")

test_data['Pclass'] = test_data['Pclass'].fillna(0)
test_data['Sex'].fillna(0)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)
test_data['Embarked'] = test_data['Embarked'].map({'S': 0, 'C': 1, 'Q' : 2})
test_data['Embarked'].dropna()
test_data.dropna(subset=['Embarked'])

# 생존 여부(Survived)를 제외한 필요한 특성들을 선택합니다.
features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
train_data.info()
train_data.info()

# 학습 데이터를 준비합니다.
X_train = train_data[features]
y_train = train_data['Survived']


# 테스트 데이터를 준비합니다.
X_test = test_data[features]

from sklearn.ensemble import RandomForestClassifier

# 모델을 초기화합니다.
model = RandomForestClassifier(random_state=1)

# 모델을 학습합니다.
model.fit(X_train, y_train)

# 테스트 데이터에 대한 예측 결과를 생성합니다.
predictions = model.predict(X_test)

submission3 = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': predictions})

# CSV 파일로 저장합니다.
submission3.to_csv('submission5.csv', index=False)
