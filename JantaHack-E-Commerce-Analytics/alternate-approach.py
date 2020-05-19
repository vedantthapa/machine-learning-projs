from fastai.imports import *
from fastai.structured import *
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

import warnings
warnings.filterwarnings(action='ignore')

# Cross-validation
def cross_val(model, X, y):
    rskfold = RepeatedStratifiedKFold(n_splits=4, n_repeats=3, random_state=42)
    scores = cross_val_score(model, X, y, cv=rskfold, scoring='accuracy')
    print('CV score: {:.2%} (+/- {:.2})'.format(scores.mean(), scores.std()))

# Load the data
path = 'data/'
train = pd.read_csv(f'{path}train_8wry4cB.csv')
test = pd.read_csv(f'{path}test_Yix80N0.csv')

# Convert variables into right format
train['startTime'] = pd.to_datetime(train['startTime'])
train['endTime']= pd.to_datetime(train['endTime'])
train['gender'] = train.gender.astype('category')
mapper = dict(enumerate(train.gender.cat.categories))

# Subset for train and test
m1_train = train.copy()
m1_test = test.copy()

# Feature engg
m1_train['Prod_count'] = m1_train['ProductList'].apply(lambda x: len(x.split(';')))
all_prods = ';'.join(m1_train['ProductList']).split(';')
all_prods = pd.DataFrame([p.strip('/').split('/') for p in all_prods])

m1_train_r = pd.DataFrame({'session_id': np.repeat(m1_train['session_id'], m1_train['Prod_count']),
              'startTime': np.repeat(m1_train['startTime'], m1_train['Prod_count']),
              'endTime': np.repeat(m1_train['endTime'], m1_train['Prod_count']),
              'ProductList': np.repeat(m1_train['ProductList'], m1_train['Prod_count']),
              'Prod_count': np.repeat(m1_train['Prod_count'], m1_train['Prod_count']),
              'gender': np.repeat(m1_train['gender'], m1_train['Prod_count'])})

m1_train_r.reset_index(drop=True, inplace=True)
m1_train = pd.concat([m1_train_r, all_prods], axis=1)
m1_train.rename(columns={0:'catA', 1:'catB', 2:'catC', 3:'catD'}, inplace=True)
m1_train.drop('ProductList', axis=1, inplace=True)

add_datepart(m1_train_r, ['startTime', 'endTime'], time=True)
train_cats(m1_train_r)
features, target, _ = proc_df(m1_train_r, 'gender')
features['duration'] = features['endTimeElapsed'] - features['startTimeElapsed']

# Split for training and testing
X_train, X_valid, y_train, y_valid = train_test_split(features, target, stratify=target, shuffle=True, test_size=0.30, random_state=42)

# Training and evaluating the model
forest = RandomForestClassifier(n_estimators=40, n_jobs=-1, min_samples_leaf=7, random_state=42)
forest.fit(X_train, y_train)

scores = cross_val(forest, X_train, y_train)
print('Accuracy score is {:.3%}'.format(forest.score(X_valid, y_valid)))

# Save the model
joblib.dump(forest, 'models/random-forest.pkl')
