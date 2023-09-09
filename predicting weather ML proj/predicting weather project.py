import pandas as pd
weather = pd.read_csv("weather.csv", index_col="DATE")


null_pct = weather.apply(pd.isnull).sum()/weather.shape[0]
# print(null_pct)

valid_columns = weather.columns[null_pct<0.05]
# print(valid_columns)

weather = weather[valid_columns].copy()

weather.columns= weather.columns.str.lower()

weather = weather.ffill()
weather.apply(pd.isnull).sum()

weather.dtypes

weather.index = pd.to_datetime(weather.index)

weather.index.year.value_counts().sort_index() # checks for mode basically
# print(weather)

weather["target"] = weather.shift(-1)["tmax"]
# print(weather)

weather = weather.ffill()

# print(weather)


# machine learnign algoright (ridge regression model)
from sklearn.linear_model import Ridge
rr= Ridge(alpha=0.1)

predictors = weather.columns[~weather.columns.isin(["target","name","station"])] # give all columns in data except _ _ _ 

def backtest(weather, model, predictors, start= 12312, step = 90):
    allpredictions = []

    for i in range(start, weather.shape[0],step):
        train  = weather.iloc[:i,:] # uses previous data before current row to use as traing data 
        test = weather.iloc[i : (i + step),:] # uses next 90 days to make predictions
        model.fit( train[predictors],train["target"])
        
        preds = model.predict(test[predictors])
        
        preds = pd.Series(preds, index=test.index)

        combinded = pd.concat([test["target"], preds], axis = 1)
        combinded.columns = ["actual", "prediction"]

        combinded["diff"] = (combinded["prediction"]) - (combinded["actual"]).abs()

        allpredictions.append(combinded)
    return pd.concat(allpredictions)


prediction = backtest(weather, rr, predictors)

print(prediction)
