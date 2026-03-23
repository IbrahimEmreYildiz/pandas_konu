import pandas as pd


data = pd.read_csv('imdb_bottom_250_movies.csv')
df=pd.DataFrame(data)

result= df.head() # ilk 5 kayıt
result= df.head(10) # ilk 10 kayıt
result= df.tail() # son 5 satır
result= df.tail(10)# son 10 satır
result= df["Title"] # sadece title column
result= df["Title"].head() # Title ilk 5 satır
result= df[["Title","Rated"]].head()
result= df[["Title","Rated"]].tail(7)
result= df[["Title","Rated"]][6:11]
result= df[(df["imdbRating"]> 1.0)][["Title","Rated","imdbRating"]].head(50)
df["Year"]=pd.to_numeric(df["Year"], errors= "coerce")
result= df[(df["Year"]>=2014) & (df["Year"]<= 2015)]["Title"]
df["imdbVotes"] = df["imdbVotes"].str.replace(",", "").pipe(pd.to_numeric, errors="coerce") # pipe string işleminin çıktısını to numeric'e gönderiyor.
df["imdbRating"] = pd.to_numeric(df["imdbRating"], errors="coerce")
result= df[(df["imdbVotes"]>10000) & (df["imdbRating"]>=1.8) & (df["imdbRating"]<=2.9)]

#result= df.head()
print(result)