import pandas as pd

# UPLOADING THE DATA
df=pd.read_csv(r"C:\Users\ASUS\Desktop\PANDAS\sales_data.csv")

# FINDING DATA FROM CITY DELHI
print(df[df['city']=='Delhi'])

# FINDING DATA FROM CITY DELHI AND PRODUCT LAPTOP
print(df[(df['city']=='Delhi') & (df['product']=='Laptop')])

# FINDING DATA FROM CITY DELHI OR PRODUCT LAPTOP
print(df[(df['city']=='Delhi') | (df['product']=='Laptop')])

# ADDING A NEW COLUMN DOUBLE DISCOUNT
df['Double Discount']=df['discount_pct']*2
print(df)
