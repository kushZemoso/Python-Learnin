import pandas as pd
data=pd.read_csv("Ecommerce_Purchases.csv")
print(data.to_string())
print(data)

# 1. Display top 10 rows in data set
print(data.head(10).to_string())

# 2.Check last 10 rows of dataset
print(data.tail(10).to_string())

# 3. Check dataType of each column
print(data.dtypes)

# 4.Check null value in data set
print(data.isnull().sum())

# 5.How many rows and columns are in data set
print(len(data.columns))
print(len(data))

# 6. Highest and lowest purchages prices
print(data["Purchase Price"].max())
print(data["Purchase Price"].min())

# 7.Average purchase Price
print(data["Purchase Price"].mean())

# 8. How many people have Freanch "fr "as their language
print(len(data[data["Language"]=="fr"]))

#9 Job Title contains Engineer
print(len(data[data["Job"].str.contains("engineer",case=False)]))

# 10 Find email of the following ip address 132.207.160.22
print(data[data["IP Address"]=="132.207.160.22"]["Email"])

# print(data.info())