import csv

class CSVReader:
    
    # Constructor to initialize the csvreader object with the filename and read the CSV data.
    def __init__(self,filename):
        self.filename = self.filePath()+filename
        self.data = []
        
    # Get the file path.
    def filePath(self):
        return "data/raw/"
    
    # read csv file and store data in list of dictionaries.    
    def read_csv(self):
        print(f"Reading CSV file: {self.filename}")
        self.data = []
        try:
            with open(self.filename,'r') as file:
                reader = csv.DictReader(file)
               # self.header = reader.fieldnames

                for row in reader:
                    self.data.append(row)
                # for i,line in enumerate(file):
                #     if i==0:
                #         self.header=line.strip().split(",")
                #     else:
                #         try:
                #             datadict={}
                #             for j,row in enumerate(line.strip().split(",")):                            
                #                 datadict[self.header[j]]=row
                                
                #             self.data.append(datadict)
                #         except (IndexError, TypeError) as e:
                #             pass
                            #print(f"Error occurred while reading line {i}: {e}")

                    #print(f"Reading line:{i} {line.strip()}")
                #print(f"Data:{self.data[0].get('transaction_id', 'Not Found')}")
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
        return self.data    
   
    #Count total rows.
    def get_total_rows(self):
        return len(self.data)
    