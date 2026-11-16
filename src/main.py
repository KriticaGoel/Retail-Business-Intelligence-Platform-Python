
from ingestion.csvreader import CSVReader
from validation.transaction_validator import TransactionAnalyzer

def main():
    csv_reader=CSVReader("transactions.csv")
    transaction_data=csv_reader.read_csv()
    transaction_analyzer =TransactionAnalyzer(transaction_data)
    print("TRANSACTION SUMMARY")
    print("-------------------")
    print(f"Total Rows: {csv_reader.get_total_rows()}")
    print(f"Total transaction quantity : {transaction_analyzer.get_total_quantity()}")
    print(f"Invalid quantities: {transaction_analyzer.get_invalid_quantity()}")
    print(f"Missing quantities: {transaction_analyzer.get_missing_quantity()}")
    print(f"Negative quantities: {transaction_analyzer.get_negative_quantity()}")


if __name__ == "__main__":
    main()