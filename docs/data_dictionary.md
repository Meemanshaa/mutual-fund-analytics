# Data Dictionary

## 01 Fund Master

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| scheme_name | TEXT | Mutual Fund Scheme |
| fund_house | TEXT | AMC Name |
| category | TEXT | Fund Category |
| plan | TEXT | Direct/Regular |

---

## 02 NAV History

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## 07 Scheme Performance

| Column | Type | Description |
|--------|------|-------------|
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year Return |
| return_5yr_pct | REAL | 5 Year Return |
| expense_ratio_pct | REAL | Expense Ratio |
| sharpe_ratio | REAL | Risk Adjusted Return |

---

## 08 Investor Transactions

| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| kyc_status | TEXT | KYC Verification |