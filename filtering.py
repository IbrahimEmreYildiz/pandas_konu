import pandas as pd
import numpy as np



data= np.random.randint(10,100,75).reshape(15,5)

#print(data)

df=pd.DataFrame(data, columns=["Column1","Column2","Column3","Column4","Column5"])
clmn_info= df.columns

result=df
#print(clmn_info) # Column'lar hakkında bilgi verir
#ilk 5 satırı .ağırmak için head() kullanılır içine sayı yazarsak o kadarını gösterir

result =df.head(8)
# eğer sondan 5 satır falan istersek tail() kullanılıyor
result= df.tail(6)
#head kullanarak şu şekilde de yapabiliriz

result = df["Column1"].head(7) # Yazılı column'un istediğimiz kadar satırını getirir
result=df[["Column1","Column2"]].head(6) # Çoklu column istersek böyle
result= df[5:15][["Column1","Column3"]].head(4)
result = df > 40 # Öyle mi değil mi diye true false döndürür
result = df[df>50] # Bu koşulu sağlayanları yazdırır sağlamayanlara NaN yazdırır.
result = df[df%2==0] # Bu şekilde filtrelemeler yapabiliriz
result = df[["Column1","Column2"]]>50 # parantezin içine yazarsak değerleri verir dışına yazarsak true false verir
result = df[df["Column1"] > 50][["Column1","Column2"]] #Column1 deki 50 den büyük satırların olduğu indexteki column1 ve 2 yi getirir
result = df[(df["Column1"]>50) & (df["Column2"] < 90)][["Column1","Column2"]]
# query() kullanınca string olarak vermek de sorguyu yapıyor
result= df.query("Column1 >30 & Column3 %3==0")[["Column1","Column2"]]

print(result)