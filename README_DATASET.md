# Retail BI — Realistic Dirty Dataset

## Purpose
This is a **synthetic training dataset** designed to resemble a multi-store retail business export. It intentionally contains data-quality issues for data profiling, cleaning, validation, joins, analytics, testing and dashboard development.

**Important:** All people, emails, suppliers, transactions and business records are synthetic. The date range is 2024-01-01 through 2025-12-31. This is not a real company's production data.

## Files
- `transactions.csv` — transaction line-level records. Includes `order_id` so order-level metrics can be practised.
- `products.csv` — product master with category, brand, cost, catalog price and supplier.
- `customers.csv` — customer master with synthetic email, city, signup date and segment.
- `stores.csv` — store master.
- `calendar.csv` — date dimension.
- `inventory.csv` — quarterly store/product inventory snapshots.
- `suppliers.csv` — supplier master and expected lead times.

## Key relationships
- transactions.customer_id -> customers.customer_id
- transactions.store_id -> stores.store_id
- transactions.product_id -> products.product_id
- transactions.transaction_date -> calendar.date
- products.supplier_id -> suppliers.supplier_id
- inventory.store_id -> stores.store_id
- inventory.product_id -> products.product_id

## Important business rules to investigate
1. Negative transaction quantity represents a return and is not automatically an error.
2. Transaction `unit_price` is the historical selling price. Do not replace it with the current product catalog price.
3. `discount_pct` is a percentage. Missing discount must be handled under an explicit rule, not silently replaced with zero.
4. `quantity_on_hand` should not be negative unless your business model explicitly supports backorders.
5. Inventory is a quarterly snapshot, not a live stock feed.
6. A transaction row is a line-level sale/return. `order_id` groups lines into orders; transaction count and order count are not interchangeable.
7. Profit is an estimate: net sales less quantity multiplied by product unit cost. Returns should reverse sales and cost consistently.

## Suggested metrics
- Gross sales before discount = quantity * unit_price
- Net sales = quantity * unit_price * (1 - discount_pct / 100)
- Estimated gross profit = net sales - quantity * unit_cost
- Average Order Value = net sales / distinct order_id, after resolving invalid/missing order IDs
- Stock cover and reorder risk must be treated cautiously: inventory is periodic, while sales are daily. Document the method and assumptions.

## Suggested learning workflow
1. Profile raw files before cleaning.
2. Write a data-quality report.
3. Define cleaning rules and preserve raw source files.
4. Create cleaned/standardized datasets in `data/processed/`.
5. Validate primary keys, foreign keys, date coverage and business constraints.
6. Build analytics from validated data.
7. Add unit and integration tests.
8. Build the Streamlit dashboard.

See `answer_key/data_quality_issue_manifest.csv` for the instructor QA checklist. Keep that file away from developers until they have completed their initial profiling exercise.
