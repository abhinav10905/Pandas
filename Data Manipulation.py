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

# DELETING A ROW TEMPORARILY
df.drop(index=3)

# DELETING A ROW PERMANENTLY
df.drop(index=3,inplace=True)
print(df)

# DELETING A ROW PERMANENTLY
df.drop(index=3,inplace=True)
print(df)

# DELETING A COLUMN PERMANENTLY
df.drop(columns='Value',inplace=True)
print(df)

# DELETING A ROW OR COLUMN USING AXIS 
# axis 0 : row
# axis 1 : column
print(df.drop(1,axis=0))
print(df.drop('Double Discount',axis=1))
