
from ingestion.csvreader import CSVReader
from validation.transaction_validator import TransactionAnalyzer
from config_loader import TRANSACTIONS_FILE
from config_loader import configure_logging


configure_logging()

import logging

logger = logging.getLogger(__name__)

def main():
    logger.info("Retail BI application started")
    csv_reader=CSVReader(TRANSACTIONS_FILE)
    transaction_data=csv_reader.read_csv()
    transaction_analyzer =TransactionAnalyzer(transaction_data)
    logger.info("TRANSACTION SUMMARY")
    logger.info("-------------------")
    logger.info(f"Total Rows: {csv_reader.get_total_rows()}")
    logger.info(f"Total transaction quantity : {transaction_analyzer.get_total_quantity()}")
    logger.info(f"Invalid quantities: {transaction_analyzer.get_invalid_quantity()}")
    logger.info(f"Missing quantities: {transaction_analyzer.get_missing_quantity()}")
    logger.info(f"Negative quantities: {transaction_analyzer.get_negative_quantity()}")


if __name__ == "__main__":
    main()