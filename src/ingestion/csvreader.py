import csv
from pathlib import Path
class CSVReader:
    
    # Constructor to initialize the csvreader object with the filename and read the CSV data.
    def __init__(self,filename):
        self.file_path = Path("data") / "raw" / filename
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")
        self.data = []
           
    # read csv file and store data in list of dictionaries.    
    def read_csv(self):
        print(f"Reading CSV file: {self.file_path}")
        self.data = []
        with self.file_path.open(mode="r",encoding="utf-8-sig",newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append(row)
        return self.data    
   
    #Count total rows.
    def get_total_rows(self):
        return len(self.data)
    