# Data Quality Assignment

Before cleaning:
1. Load each CSV without modifying it.
2. Record row count, column count, inferred data types and null counts.
3. Check primary-key uniqueness and foreign-key integrity.
4. Profile categorical values and numeric ranges.
5. Check date parsing and date-dimension consistency.
6. Identify business-rule violations separately from legitimate business events.
7. Create a proposed cleaning policy with a reason for each action.

Do not use `dropna()` or `drop_duplicates()` as a blanket fix.
Do not overwrite files in `data/raw/`.
Every rejected, corrected, imputed or quarantined record must be traceable.
