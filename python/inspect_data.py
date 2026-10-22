
import pandas as pd

df = pd.read_csv("data/raw/train.csv")
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d/%m/%Y"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%d/%m/%Y"
)

print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


print("\nDuplicate rows:", df.duplicated().sum())

print("\nUnique orders:", df["Order ID"].nunique())
print("Unique customers:", df["Customer ID"].nunique())
print("Unique products:", df["Product ID"].nunique())

print("\nDate samples:")
print(df[["Order Date", "Ship Date"]].head())

print("\nSales summary:")
print(df["Sales"].describe())

print("\nOrder date range (raw values):")
print("Earliest:", df["Order Date"].min())
print("Latest:", df["Order Date"].max())

print("\nOrder date range:")
print("Earliest:", df["Order Date"].min())
print("Latest:", df["Order Date"].max())




# Handle missing values
df["Postal Code"] = df["Postal Code"].astype("Int64")

# Save the cleaned dataset
df.to_csv("data/cleaned/retail_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Dataset shape:", df.shape)
print("Missing values after cleaning:")
print(df.isnull().sum())
