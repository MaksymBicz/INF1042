import pandas as pd

df = pd.read_csv("nba.csv")


top_salaries = df.sort_values(by="salary", ascending=False)


print(top_salaries[["Team", "salary"]].head(10))