
from ingestion.csvreader import csvreader


csv=csvreader("transactions.csv")
print(f"Column Names: {csv.getColumnName()}")
print(f"Total Rows: {csv.getTotalRows()}")
