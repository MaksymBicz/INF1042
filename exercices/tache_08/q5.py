
import pandas as pd

df = pd.read_csv("nba.csv")


stats = df.groupby("position")["salary"].agg(["mean", "max", "min"])

print(stats)