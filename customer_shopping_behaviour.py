import pandas as pd
from sqlalchemy import create_engine

# ------------------------------
# 1. Load CSV from your PC
# ------------------------------
df = pd.read_csv(r"F:/Murtaza DATA ANALYTICS PROJECT/Database upload/customer_shopping_behavior.csv")

print("CSV Loaded Successfully")
print(df.head())

# ------------------------------
# 2. Check missing values
# ------------------------------
print(df.isnull().sum())

# ------------------------------
# 3. Impute missing Review Rating using median per Category
# ------------------------------
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

# ------------------------------
# 4. Rename columns (snake_case)
# ------------------------------
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# ------------------------------
# 5. Create Age Group using qcut
# ------------------------------
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

# ------------------------------
# 6. Map purchase frequency to days
# ------------------------------
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# ------------------------------
# 7. Drop promo_code_used
# ------------------------------
df = df.drop('promo_code_used', axis=1)

print("Data cleaned successfully!")
print(df.head())

# ------------------------------
# 8. Connect to PostgreSQL on your PC
# ------------------------------
username = "postgres"
password = "1234"        # your password
host = "localhost"
port = "5432"
database = "customer_behavior"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# ------------------------------
# 9. Upload DataFrame to PostgreSQL table
# ------------------------------
df.to_sql("customer", engine, if_exists="replace", index=False)

print("✔ Data successfully uploaded to PostgreSQL!")
