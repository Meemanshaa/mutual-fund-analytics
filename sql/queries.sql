-- 1 Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM 07_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2 Average NAV Per Month

SELECT
strftime('%Y-%m',date) AS Month,
AVG(nav) AS Average_NAV
FROM 02_nav_history
GROUP BY Month;


-- 3 SIP YoY Growth

SELECT
year,
SUM(sip_inflow_crore)
FROM 04_monthly_sip_inflows
GROUP BY year;


-- 4 Transactions By State

SELECT
state,
SUM(amount_inr)
FROM 08_investor_transactions
GROUP BY state;


-- 5 Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM 07_scheme_performance
WHERE expense_ratio_pct < 1;


-- 6 Highest Sharpe Ratio

SELECT
scheme_name,
sharpe_ratio
FROM 07_scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;


-- 7 Highest 5-Year Returns

SELECT
scheme_name,
return_5yr_pct
FROM 07_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- 8 Average Transaction Amount By City Tier

SELECT
city_tier,
AVG(amount_inr)
FROM 08_investor_transactions
GROUP BY city_tier;


-- 9 Total AUM By Fund House

SELECT
fund_house,
SUM(aum_crore)
FROM 07_scheme_performance
GROUP BY fund_house;


--10 Risk Grade Distribution

SELECT
risk_grade,
COUNT(*)
FROM 07_scheme_performance
GROUP BY risk_grade;