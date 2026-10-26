import pandas as pd

# UPLOADING THE DATA
df=pd.read_csv(r"C:\Users\ASUS\Desktop\PANDAS\sales_data.csv")

# FINDING DATA FROM CITY DELHI
print(df[df['city']=='Delhi'])

# FINDING DATA FROM CITY DELHI AND PRODUCT LAPTOP
print(df[(df['city']=='Delhi') & (df['product']=='Laptop')])
