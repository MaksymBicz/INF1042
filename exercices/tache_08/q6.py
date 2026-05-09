
import pandas as pd

df = pd.read_csv("nba.csv")


resultat = df.groupby(["Team", "country"]).size()

print(resultat)