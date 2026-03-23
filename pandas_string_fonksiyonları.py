import pandas as pd


data= pd.read_csv('all_seasons.csv')
df=pd.DataFrame(data)
df.dropna(inplace=True) # Orijinal data üzerinde işlem yapar
column_inf= df.columns
df["player_name"]= df["player_name"].str.upper()

# df["index"]= df["player_name"].str.find("R")
# print(df["index"])

data= df[df["player_name"].str.contains('JORDAN')]
df["player_name"]= df["player_name"].str.replace(" ", "-")
print(df["player_name"])




#print(df["player_name"])






#print(column_inf)
