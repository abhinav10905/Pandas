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

# ADDING A NEW COLUMN VALUE USING CONDITION
print(df['payment_method'].value_counts())
def a(x):
    if x=="Net Banking":
        return 1
    elif x=="UPI":
        return 2
    elif x=="Cash":
        return 3
    else:
        return 4
df['Value']=df['payment_method'].apply(a)
print(df)
