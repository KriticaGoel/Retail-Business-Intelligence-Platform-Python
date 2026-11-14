


class transactions:
    
    def __init__(self,data):
        self.data=data

    #Calculate total valid transaction quantities.
    def getTotalTransactionQuantity(self):
        transaction_quantity=0
        for row in self.data:
            try:
                transaction_quantity =transaction_quantity + int(row.get('quantity', 0))
            except (ValueError, TypeError) as e:
                pass
                #print(f"Error occurred while calculating total transaction quantity: {e}")
        return transaction_quantity
    
    #Count records with missing quantities.
    def getMissingQuantity(self):
        missing_quantity=0;
        for row in self.data:
             if(row.get('quantity') is None or row.get('quantity') == ''):
                 missing_quantity += 1
        return missing_quantity
    
    #Count records with invalid, non-numeric quantities.
    def getInvalidQuantity(self):
        invalid_quantity=0;
        for row in self.data:
            try:
                int(row.get('quantity', 0))
            except (ValueError, TypeError) as e:
                invalid_quantity += 1
        return invalid_quantity
    #Identify negative quantities and count them separately.
    def getNegativeQuantity(self):
        negative_quantity=0
        for row in self.data:
            try:
                if(row.get('quantity') is not None and int(row.get('quantity', 0)) < 0):
                    negative_quantity += 1
            except (ValueError, TypeError) as e:
                pass
                #print(f"Error occurred while calculating negative transaction quantity: {e}")
        return negative_quantity
   