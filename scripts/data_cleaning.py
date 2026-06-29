####################################2####################################
import pandas as pd
import os
import numpy as np
from sqlalchemy import create_engine

RAW_FOLDER="data/raw"
PROCESSED_FOLDER="data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

nav=pd.read_csv("data/raw/02_nav_history.csv")
print(nav.head())
print(nav.info())

#convert date
nav["date"] = pd.to_datetime(nav["date"])

#sort data
nav = nav.sort_values(
    by=["amfi_code", "date"]
)

#forward fill missing nav values for each amfi_code
nav["nav"] = (
    nav
    .groupby("amfi_code")["nav"]
    .ffill()
)

#remove duplicate rows
before = len(nav)

nav = nav.drop_duplicates()

after = len(nav)

print(f"Duplicates Removed : {before-after}")

#validate nav values are not null
invalid_nav = nav[nav["nav"] <= 0]

print("Invalid NAV Rows")

print(invalid_nav)

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED_FOLDER}/02_nav_history_clean.csv",
    index=False
)

print("nav_history cleaned successfully")

print("\n========== CLEANING SUMMARY ==========")
print(f"Original Rows : {46000}")
print(f"Final Rows    : {len(nav)}")
print(f"Duplicates Removed : {before-after}")
print(f"Invalid NAV Removed : {len(invalid_nav)}")
print("Output File : data/processed/02_nav_history_clean.csv")
print("======================================")

#################################8#################################

transactions = pd.read_csv(f"{RAW_FOLDER}/08_investor_transactions.csv")

print(transactions.head())
print(transactions.info())
print(transactions.columns)

#to read the dataset
print("\nCleaning investor_transactions.csv...")

transactions = pd.read_csv(f"{RAW_FOLDER}/08_investor_transactions.csv")

original_rows = len(transactions)

#covert date format
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

print("Transaction Date Datatype:")
print(transactions["transaction_date"].dtype)

#to standardized
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .replace({
        "Sip": "SIP",
        "Lump Sum": "Lumpsum",
        "Redeem": "Redemption"
    })
)

#to check unique value
print("\nTransaction Types:")
print(transactions["transaction_type"].unique())

#to check valid amount
invalid_amount = transactions[
    transactions["amount_inr"] <= 0
]

print("\nInvalid Amount Rows:")
print(len(invalid_amount))
transactions = transactions[
    transactions["amount_inr"] > 0
]

#valid kyc status
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

#FIND INVALID ROWS
invalid_kyc = transactions[
    ~transactions["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Rows:")
print(len(invalid_kyc))

#remove duplicate rows
before = len(transactions)

transactions = transactions.drop_duplicates()

after = len(transactions)

print("\nDuplicates Removed:", before-after)

#save clean file
transactions.to_csv(
    f"{PROCESSED_FOLDER}/08_investor_transactions_clean.csv",
    index=False
)

#print summary
print("\n========== CLEANING SUMMARY ==========")
print(f"Original Rows : {original_rows}")
print(f"Final Rows    : {len(transactions)}")
print(f"Duplicates Removed : {before-after}")
print(f"Invalid Amount Removed : {len(invalid_amount)}")
print(f"Invalid KYC Rows : {len(invalid_kyc)}")
print("Output File : data/processed/08_investor_transactions_clean.csv")
print("======================================")


######################################8####################################
print("\nCleaning scheme_performance.csv...")

performance = pd.read_csv(
    f"{RAW_FOLDER}/07_scheme_performance.csv"
)

print(performance.head())
print(performance.info())
print(performance.columns)

original_rows = len(performance)

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

print("\nMissing Values")

print(performance[return_columns].isnull().sum())

anomalies = performance[
    (performance["return_1yr_pct"] < -100) |
    (performance["return_1yr_pct"] > 100) |
    (performance["return_3yr_pct"] < -100) |
    (performance["return_3yr_pct"] > 100) |
    (performance["return_5yr_pct"] < -100) |
    (performance["return_5yr_pct"] > 100)
]

print("\nReturn Anomalies")

print(anomalies)

invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio")

print(invalid_expense)

performance = performance[
    (performance["expense_ratio_pct"] >= 0.1) &
    (performance["expense_ratio_pct"] <= 2.5)
]
before = len(performance)

performance = performance.drop_duplicates()

after = len(performance)

print("\nDuplicates Removed:", before-after)

performance.to_csv(
    f"{PROCESSED_FOLDER}/07_scheme_performance_clean.csv",
    index=False
)

print("\n========== CLEANING SUMMARY ==========")
print(f"Original Rows : {original_rows}")
print(f"Final Rows    : {len(performance)}")
print(f"Duplicates Removed : {before-after}")
print(f"Expense Ratio Anomalies : {len(invalid_expense)}")
print(f"Return Anomalies : {len(anomalies)}")
print("Output File : data/processed/07_scheme_performance_clean.csv")
print("======================================")

def clean_generic_dataset(filename):
    print(f"\nCleaning {filename}...")

    df = pd.read_csv(f"{RAW_FOLDER}/{filename}")

    original_rows = len(df)

    print("\nMissing Values:")
    print(df.isnull().sum())

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    df.to_csv(
        f"{PROCESSED_FOLDER}/{filename.replace('.csv', '_clean.csv')}",
        index=False
    )

    print("\n========== CLEANING SUMMARY ==========")
    print(f"Original Rows : {original_rows}")
    print(f"Final Rows    : {len(df)}")
    print(f"Duplicates Removed : {before-after}")
    print("======================================")

    # Generic Cleaning Function

# ----------------------------
# Generic Cleaning Function
# ----------------------------

def clean_generic_dataset(filename):

    print(f"\nCleaning {filename}...")

    df = pd.read_csv(f"{RAW_FOLDER}/{filename}")

    original_rows = len(df)

    print("\nMissing Values:")
    print(df.isnull().sum())

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    df.to_csv(
        f"{PROCESSED_FOLDER}/{filename.replace('.csv', '_clean.csv')}",
        index=False
    )

    print("\n========== CLEANING SUMMARY ==========")
    print(f"Original Rows : {original_rows}")
    print(f"Final Rows    : {len(df)}")
    print(f"Duplicates Removed : {before-after}")
    print("======================================")

    generic_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

engine = create_engine("sqlite:///database/bluestock_mf.db")

processed_folder = "data/processed"

for file in os.listdir(processed_folder):
    if file.endswith(".csv"):
        table_name = file.replace("_clean.csv", "")
        df = pd.read_csv(os.path.join(processed_folder, file))

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"{table_name}: {len(df)} rows loaded")

print("\nAll datasets loaded successfully.")