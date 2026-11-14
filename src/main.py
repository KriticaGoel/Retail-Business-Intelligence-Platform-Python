
from ingestion.csvreader import CSVReader
from validation.transaction_validator import TransactionAnalyzer


csvread=CSVReader("transactions.csv")
transaction_data=csvread.read_csv()
transactions =TransactionAnalyzer(transaction_data)
print("TRANSACTION SUMMARY")
print("-------------------")
print(f"Column Names: {csvread.getColumnName()}")
print(f"Total Rows: {csvread.get_total_rows()}")
print(f"Total transaction quantity : {transactions.get_total_quantity()}")
print(f"Invalid quantities: {transactions.get_invalid_quantity()}")
print(f"Missing quantities: {transactions.get_missing_quantity()}")
print(f"Negative quantities: {transactions.get_negative_quantity()}")