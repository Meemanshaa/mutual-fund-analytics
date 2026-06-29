import os
import pandas as pd
from sqlalchemy import create_engine

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

engine = create_engine("sqlite:///database/bluestock_mf.db")

files = [
    "01_fund_master.csv",
    "02_nav_history_clean.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance_clean.csv",
    "08_investor_transactions_clean.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    if "_clean" in file:
        path = os.path.join(PROCESSED_FOLDER, file)
    else:
        path = os.path.join(RAW_FOLDER, file)

    df = pd.read_csv(path)

    # Generic cleaning
    df = df.drop_duplicates()

    table_name = file.replace(".csv", "").replace("_clean", "")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} : {len(df)} rows loaded")

print("\nDatabase created successfully!")