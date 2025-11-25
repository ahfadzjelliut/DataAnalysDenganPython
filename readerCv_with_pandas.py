import pandas as pd
pd.set_option("display.max_columns",50)

table = pd.read_csv("https://opendata.limapuluhkotakab.go.id/download/c01e5dc1d2b9467a944519ec10c45862.csv")
table.head()
print(table)
