import pandas as pd
from sklearn.tree import DecisionTreeRegressor
def mhash(s):
    return hash(s) % 2147483647

tdf = pd.read_csv('table.csv')

y = tdf.ptstot
#features = ['ptsw','ptsl', 'ydsw', 'ydsl', 'tow', 'tol']
features = ['winner','loser', 'time']
X = tdf[features]

nfl_model = DecisionTreeRegressor(random_state=1)

nfl_model.fit(X, y)

to_predict = pd.read_csv('next.csv')
new_X = to_predict[features]

print("Making predictions for the following 5 houses:")
print(new_X.head())
print("The predictions are")
print(nfl_model.predict(new_X.head()))