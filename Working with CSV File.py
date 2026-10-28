import pandas as pd

# UPLOADING THE DATA
df=pd.read_csv(r"C:\Users\ASUS\Desktop\PANDAS\sales_data.csv")
print(df)
print(type(df))

# INSPECTING THE DATA
print(df.head()) # GIVES FIRST 5 ROWS BY DEFAULT ( WE CAN ALSO PROVIDE VALUES)
print(df.tail()) # GIVES LAST 5 ROWS BY DEFAULT ( WE CAN ALSO PROVIDE VALUES)
print(df.shape) # GIVES A TUPLE CONTAINING THE NUMBER OF ROWS AND COLUMNS PRESENT IN THE DATA
print(df.columns) # GIVES THE NAME OF ALL THE COLUMNS

# EXTRACTING SINGLE COLUMN
print(df['order_date']) # GIVES THE DATA PRESENT IN ANY PARTICULAR COLUMN
print(type(df['order_date'])) # AS WE HAVE JUST EXTRACTED ONE COLUMN, SO THE TYPE WOULD BE SERIES

# EXTRACTING MULTIPLE COLUMNS
print(df[['order_date','city']]) # GIVES THE DATA PRESENT IN ANY PARTICULAR COLUMN
print(type(df[['order_date','city']])) # AS WE HAVE EXTRACTED MORE THAN ONE COLUMN, SO THE TYPE WOULD BE DATAFRAME

# FINDING TOTAL QUANTITY OF PRODUCTS
print(df['quantity'].sum())

# COUNTING ORDERS FROM DIFFERENT CITIES
print(df['city'].value_counts())

# FINDING MAXIMUM, MINIMUM, AVERAGE and STANDARD DEVIATION CUSTOMER RATING
print(df['customer_rating'].max())
print(df['customer_rating'].min())
print(df['customer_rating'].mean())
