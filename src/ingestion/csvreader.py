

class csvreader:
    
    # Constructor to initialize the csvreader object with the filename and read the CSV data.
    def __init__(self,filename):
        self.filename = self.filePath()+filename
        self.data = []
        self.header=[]
        
    # Get the file path.
    def filePath(self):
        return "data/raw/"
    
    # read csv file and store data in list of dictionaries.    
    def read_csv(self):
        with open(self.filename,'r') as file:
            for i,line in enumerate(file):
                if i==0:
                    self.header=line.strip().split(",")
                else:
                    try:
                        datadict={}
                        for j,row in enumerate(line.strip().split(",")):                            
                            datadict[self.header[j]]=row
                            
                        self.data.append(datadict)
                        print(self.data)
                    except (IndexError, TypeError) as e:
                        pass
                        #print(f"Error occurred while reading line {i}: {e}")

                #print(f"Reading line:{i} {line.strip()}")
            #print(f"Data:{self.data[0].get('transaction_id', 'Not Found')}")
        return self.data    
    #Inspect column names.        
    def getColumnName(self):
        return self.header
    
    #Count total rows.
    def getTotalRows(self):
        return len(self.data)
    