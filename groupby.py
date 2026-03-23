import pandas as pd
import numpy as np


personeller = {
    'Worker': ['Ahmet Yilmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Demir', 'Ayşe Kaya', 'Fatma Şahin'],
    'Department': ['İnsan Kaynaklari', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynaklari', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynaklari'],
    'Age': [30, 25, 45, 50, 23, 34, 42],
    'Place': ['Kadiköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadiköy'],
    'Salary': [5000, 3000, 4000, 3500, 2750, 6500, 4500]
}

df= pd.DataFrame(personeller)
result= df
result= df.groupby("Department").groups # Aynı ögeleri gruplandırır. groups ise onları görmemizi ve lokasyonlarını görmemizi sağlar

#print(result)

semtler= df.groupby(["Place","Department"])

# for semt, departman in semtler:
#     print(semt)
#     print(departman)
#     print("\n")


result= df.groupby("Department").get_group("İnsan Kaynaklari")
result= df.groupby("Place")["Salary"].mean().round(2) # virgülden sonraki basamak sayısı
result= df.groupby("Place")["Worker"].count() # Yerlere göre çalışan sayısı
result= df.groupby("Place")["Salary"].max()["Kadiköy"]
result= df.groupby("Department")["Salary"].agg(["mean","max","min"])
result= df.groupby("Department")["Salary"].agg([np.mean,np.max,np.min])
print(result)