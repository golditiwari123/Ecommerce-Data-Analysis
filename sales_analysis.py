import pandas as pd
import numpy as np
df = pd.read_csv("sales_data.csv")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.dtypes)
df["Date"]=pd.to_datetime(df["Date"])
print(df.dtypes)
df["Revenue"]=df["Quantity"]*df["Price"]
print(df)


total_revenue = np.sum(df["Revenue"])
print("Total Revenue:", total_revenue)

average_revenue = np.mean(df["Revenue"])
print("Average Revenue:", average_revenue)

highest_revenue = np.max(df["Revenue"])
print("Highest Revenue:", highest_revenue)

lowest_revenue = np.min(df["Revenue"])
print("Lowest Revenue:", lowest_revenue)

total_quantity = np.sum(df["Quantity"])
print("Total Quantity Sold:", total_quantity)

average_quantity = np.mean(df["Quantity"])
print("Average Quantity:", average_quantity)

df["Sale_Type"] = np.where(
    df["Revenue"] >= 50000,
    "High Sale",
    "Normal Sale"
)
print(df[["Product", "Revenue", "Sale_Type"]])

index = np.argmax(df["Revenue"])
print(df.iloc[index])

laptop = df[df["Product"] == "Laptop"]
print(laptop)

noida_sales = df[df["City"] == "Noida"]
print(noida_sales)

result = df[
    (df["City"] == "Noida") &
    (df["Category"] == "Electronics")
]

print(result)

sorted_df = df.sort_values(
    "Revenue",
    ascending=False
)

print(sorted_df)

print(
    df.sort_values(
        "Revenue",
        ascending=False
    ).head(5)
)

category_sales = df.groupby("Category")["Revenue"].sum()
print(category_sales)

product_sales = df.groupby("Product")["Revenue"].sum()
print(product_sales)

city_sales = df.groupby("City")["Revenue"].sum()
print(city_sales)

product_quantity = df.groupby("Product")["Quantity"].sum()
print(product_quantity)

product_summary = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
)
print(product_summary)


best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)
print("Best Selling Product:", best_product)


best_revenue_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .idxmax()
)

print(
    "Highest Revenue Product:",
    best_revenue_product
)

df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Revenue"].sum()

print(monthly_sales)

print(df["Revenue"].describe())
std = np.std(df["Revenue"])

print("Revenue Standard Deviation:", std)



print("\n========== BUSINESS INSIGHTS ==========")

print("Total Revenue:", df["Revenue"].sum())

print("Total Units Sold:", df["Quantity"].sum())

print(
    "Best Selling Product:",
    df.groupby("Product")["Quantity"].sum().idxmax()
)

print(
    "Highest Revenue Product:",
    df.groupby("Product")["Revenue"].sum().idxmax()
)

print(
    "Best City:",
    df.groupby("City")["Revenue"].sum().idxmax()
)

print(
    "Best Category:",
    df.groupby("Category")["Revenue"].sum().idxmax()
)

df.to_csv(
    "final_sales_analysis.csv",
    index=False
)