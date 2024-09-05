import pandas as pd
import numpy as np


print(pd.__version__)

print(np.__version__)


df = pd.read_csv("supermarket_sales_dataset.csv")


print("Data:")

print(df)

print("\nDetails:")

print(f"Number of rows: {df.shape[0]}")

print(f"Number of columns: {df.shape[1]}")

print(f"Memory usage: {df.memory_usage().sum()} bytes")


df = df.dropna()

print("\nUpdated Data:")

print(df)

d= df.dropna()

df['Total Cost Before Tax'] = df['Unit price'] * df['Quantity']

print("\nInvoice ID and Total Cost Before Tax:")

print(df[['Invoice ID', 'Total Cost Before Tax']])


df['Total Cost Before Tax'] = df['Total Cost Before Tax'].round(1)

print("\nTotal Cost Before Tax (rounded to one decimal place):")

print(df['Total Cost Before Tax'])


print("\nBranches:")

print(df['Branch'].unique())


print("\nMax Total:", df['Total'].max())

print("Min Total:", df['Total'].min())


product_lines = ['Electronic accessories', 'Sports and travel', 'Health and beauty', 'Home and lifestyle', 'Food and beverages', 'Fashion accessories']
for product_line in product_lines:
    print(f"Number of '{product_line}' product lines: {df[df['Product line'] == product_line].shape[0]}")


df['Gender'] = df['Gender'].replace(['Female', 'Male'], ['F', 'M'])

print("\nGender (replaced):")

print(df['Gender'])


payment_methods = ['Ewallet', 'Cash', 'Credit card']
for payment_method in payment_methods:
    print(f"Number of purchases paid with '{payment_method}': {df[df['Payment'] == payment_method].shape[0]}")


df['Final Cost'] = df['Total'] * 1.05

print("\nFinal Cost (with 5% tax):")

print(df['Final Cost'])


branch_data = df.groupby('Branch')[['Quantity', 'Final Cost']].sum()

print("\nBranch Data:")

print(branch_data)


customer_types = df['Customer type'].value_counts()

print("\nCustomer Types:")

print(customer_types)


def added_Tax_Fun(df):
    df['Final Cost with 3% Tax'] = df['Total'] * 1.03
    return df

df = added_Tax_Fun(df)

print("\nFinal Cost (with 3% tax):")

print(df['Final Cost with 3% Tax'])


df = df.apply(pd.to_numeric, errors='coerce')

print("\nNumeric Data:")

print(df.dtypes)