# Retail BI Practice Dataset

This is a realistic synthetic retail dataset created for Python project.

## Files
- transactions.csv: 12,003 transaction-line records, including a small number of intentional data-quality issues.
- products.csv: 25 products across five categories.
- customers.csv: 600 customers.
- stores.csv: 8 stores.
- calendar.csv: daily calendar dimension for 2024–2025.

## Relationships
- transactions.product_id -> products.product_id
- transactions.customer_id -> customers.customer_id
- transactions.store_id -> stores.store_id
- transactions.transaction_date -> calendar.date

## Important
The dataset is synthetic, not a real company's confidential data. A few missing values, invalid numeric values and duplicate rows are intentionally included for data-cleaning.

## Revenue convention for later days
Define and document the revenue formula, including the effect of discount_pct. Do not assume a formula without checking the business definition.
