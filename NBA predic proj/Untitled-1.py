import pandas as pd 
datafile = pd.read_csv("nba_games.csv", index_col=0) #first column is going to be pd index)


datafile = datafile.sort_values("date") #sorts data by data from oldest to newest but messes up the indexing
datafile = datafile.reset_index(drop=True) #makes old index a column and doesnt keep the old index (thats what drop = True basically does) 


# cleaning up the data by removing keys(columns) which are giving uncecessary information 
del datafile["mp.1"]
del datafile["mp_opp.1"]
del datafile["index_opp"]


def addtarget(team):
    team["target"] = team["won"].shift(-1)
    return team

datafile = datafile.groupby("team", group_keys= False).apply(addtarget) # splits data frame into one data frame per team


datafile["target"][pd.isnull(datafile["target"])] = "nda" # takes target column and uses pandas isnull funciton to return True if a value is Null and False if it isnt

datafile["target"] = datafile["target"].astype(int, errors ="ignore")



# print(datafile["won"].value_counts())

# print(datafile["target"].value_counts())


nulls = pd.isnull(datafile)

nulls = nulls.sum()

nulls = nulls[nulls>0]

validcolumns = datafile.columns[~datafile.columns.isin(nulls.index)] # ~ is a negation operator for pandas library

datafile = datafile[validcolumns].copy() # do not want to mess with original data

print(validcolumns)

# validccolumns = datafile.columns

#machine learning model 


from sklearn.model_selection import TimeSeriesSplit
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import RidgeClassifier # rige reg


rige = RidgeClassifier(alpha=1) 
tsp = TimeSeriesSplit(n_splits=3)


sfs = SequentialFeatureSelector(rige, n_features_to_select= 30, direction= "forward", cv=tsp)

remove = ["season", "date", 'won', "target", "team", "team_opp"]

selected = datafile.columns[~datafile.columns.isin(remove)]

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

datafile[selected] = scaler.fit_transform(datafile[selected])


# datafile["target"] = datafile["target"].astype(int)

sfs.fit(datafile[selected], datafile["target"])


predictors = list(selected[sfs.get_support()])


