
import pandas as pd

df = pd.read_csv("nba.csv")


positions = df["position"].value_counts()

print(positions)