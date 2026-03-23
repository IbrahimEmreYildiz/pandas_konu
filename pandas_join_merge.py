import pandas as pd

customers = {
    'CustomerId': [1, 2, 3, 4],
    'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
    'LastName': ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

orders = {
    'OrderId': [10, 11, 12, 13],
    'CustomerId': [1, 2, 5, 7],
    'OrderDate': ['2010-07-04', '2010-08-04', '2010-07-07', '2012-07-04']
}


df_customers=pd.DataFrame(customers, columns=["CustomerId","FirstName","LastName"])
df_orders=pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

merged= pd.merge(df_customers,df_orders, how='inner')
merged= pd.merge(df_customers,df_orders, how='left')
merged= pd.merge(df_customers,df_orders, how='right')
merged= pd.merge(df_customers,df_orders, how='outer')



print(merged)






# customersA = {
#     'CustomerId': [1, 2, 3, 4],
#     'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
#     'LastName': ["Yilmaz", "Korkmaz", "Çelik", "Toprak"]
# }



# customersB = {
#     'CustomerId': [4, 5, 6, 7],
#     'FirstName': ["Mert", "Mehmet", "Emre", "Kaan"],
#     'LastName': ["Sürer", "Yardimci", "Yildiz", "Apucu"]
# }

# df_customersA=pd.DataFrame(customersA, columns=["CustomerId","FirstName","LastName"])
# df_customersB=pd.DataFrame(customersB, columns=["CustomerId","FirstName","LastName"])

# result= pd.concat([df_customersA,df_customersB]) #default olarak satır olarak alt alta ekler yani axis= 0
# print(result)
# result= pd.concat([df_customersA,df_customersB], axis=1) # yan yana ekler yani sütun olarak
# print("\n")
# print(result)
