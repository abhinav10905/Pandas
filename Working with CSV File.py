import pandas as pd

# UPLOADING THE DATA
df=pd.read_csv(r"C:\Users\ASUS\Desktop\PANDAS\sales_data.csv")
print(df)
print(type(df))

# INSPECTING THE DATA
print(df.head()) # GIVES FIRST 5 ROWS BY DEFAULT ( WE CAN ALSO PROVIDE VALUES)
