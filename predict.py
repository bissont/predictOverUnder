import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
d = defaultdict(LabelEncoder)
le = LabelEncoder()
tdf = pd.read_csv('table.csv')
#ntdf= tdf.apply(lambda x:d[x.name].fit_transform(x))
tdf['winner'] =  le.fit_transform(tdf['winner'])
tdf['loser'] =  le.transform(tdf['loser'])
#ntdf= tdf.apply(lambda x:d[x.name].fit_transform(x))

to_predict = pd.read_csv('next.csv')
to_predict['winner'] =  le.transform(to_predict['winner'])
to_predict['loser'] =  le.transform(to_predict['loser'])

y = tdf.ptstot
#features = ['ptsw','ptsl', 'ydsw', 'ydsl', 'tow', 'tol']
features = ['winner','loser']
X = tdf[features]

nfl_model = DecisionTreeRegressor(random_state=1)

nfl_model.fit(X, y)

print(to_predict.head())
new_X = to_predict[features]

print("Making predictions for the following 5 houses:")
print(new_X.head())
print("The predictions are")
print(nfl_model.predict(new_X.head()))
