import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')
df.head()
#1.
df['creationdate']=pd.to_datetime(df['creationdate'])
df_bef_2014 = df[df['creationdate']<'2014-01-01']
df_bef_2014

#2.
df_more_50 = df[df['score']>50]
df_more_50

#3.
df_between_50_and_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
df_between_50_and_100

#4.
answered = df[df['ans_name']=='Scott Boston']
answered

#5. 
users = ['Scott Boston', 'User2', 'User3', 'User4', 'User5']
for_5 = df[df['ans_name'].isin(users)]
for_5

#6.

df['creationdate'] = pd.to_datetime(df['creationdate'])
mask = (
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
)

result = df[mask]
result

#7.
questions_filtered = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
]
questions_filtered

#8.

not_answered = df[df['ans_name']!='Scott Boston']
not_answered


#Homework 3.
titanic_df = pd.read_csv("titanic.csv")


#1.
extracted = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]
extracted
#2.
high_fare = titanic_df[titanic_df['Fare'] > 100]
high_fare

#3.
alone_survivors = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
alone_survivors

#4.
embarked_c_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
embarked_c_fare_50

#5.
sibsp_parch = titanic_df[
    (titanic_df['SibSp'] > 0) & 
    (titanic_df['Parch'] > 0)
]
sibsp_parch
#6.
young_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
young_not_survived

#7
high_fare_cabin = titanic_df[
    titanic_df['Cabin'].notna() & 
    (titanic_df['Fare'] > 200)
]
high_fare_cabin

#8.
odd_passenger_ids = titanic_df[
    titanic_df['PassengerId'] % 2 == 1
]
odd_passenger_ids

#9.
unique_ticket_passengers = titanic_df[
    ~titanic_df['Ticket'].duplicated(keep=False)
]
unique_ticket_passengers

#10.
miss_class1 = titanic_df[
    titanic_df['Name'].str.contains('Miss') & 
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Sex'] == 'female')
]
miss_class1
