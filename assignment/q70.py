test_df.loc[test_df['Age'] < 1] = 1
test_df.fillna({'Age' : test_df['Age'].median()} , inplace=True)
test_df['Sex']=test_df['Sex'].map({'female':0, 'male':1})
test_df['Fare']=test_df['Fare'].astype(int)
test_df['Age']=test_df['Age'].astype(int)
test_df.dropna(subset='Embarked', inplace=True)
test_df = test_df[test_df['Embarked'] != 1]
test_df['Embarked']=test_df['Embarked'].map({'S':0, 'C':1 , 'Q':2})
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
test_df[['Age', 'Fare']] = scaler.fit_transform(test_df[['Age', 'Fare']])
