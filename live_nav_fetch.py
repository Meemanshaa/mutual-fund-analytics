import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url, timeout=20)

print("Status:", response.status_code)

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv("data/raw/hdfc_top100_nav.csv", index=False)

print("Rows:", len(df))
print("Data saved successfully!")