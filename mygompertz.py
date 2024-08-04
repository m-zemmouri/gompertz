import pandas as pd
DataFrame = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
print(DataFrame.head(5))
print(DataFrame.iloc[0:4])