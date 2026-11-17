import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class CSVReader:
    
    # Constructor to initialize the csvreader object with the filename and read the CSV data.
    def __init__(self,file_path : Path):
        #self.file_path = Path("data") / "raw" / filename
        self.file_path = file_path
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")
        self.data = []
           
    # read csv file and store data in list of dictionaries.    
    def read_csv(self)  -> list[dict[str, str]]: 
        logger.info(f"Reading CSV file: {self.file_path}")
        self.data = []
        with self.file_path.open(mode="r",encoding="utf-8-sig",newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append(row)
        return self.data    
   
    #Count total rows.
    def get_total_rows(self) -> int:
        return len(self.data)
    