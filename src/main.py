
from ingestion.csvreader import csvreader
from validation.transactions import transactions


csvread=csvreader("transactions.csv")
csv=csvread.read_csv()
transactions =transactions(csv)
print("TRANSACTION SUMMARY")
print("-------------------")
print(f"Column Names: {csvread.getColumnName()}")
print(f"Total Rows: {csvread.getTotalRows()}")
print(f"Total transaction quantity : {transactions.getTotalTransactionQuantity()}")
print(f"Invalid quantities: {transactions.getInvalidQuantity()}")
print(f"Missing quantities: {transactions.getMissingQuantity()}")
print(f"Negative quantities: {transactions.getNegativeQuantity()}")