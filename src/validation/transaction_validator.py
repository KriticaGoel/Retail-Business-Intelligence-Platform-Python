


from enums.quantity_status import QuantityStatus


class TransactionAnalyzer:
    
    def __init__(self,data):
        self.data=data

    #Calculate total valid transaction quantities.
    def get_total_quantity(self):
        transaction_quantity=0
        for row in self.data:
            if self.get_quantity_classification(row.get('quantity'))==QuantityStatus.VALID or self.get_quantity_classification(row.get('quantity'))==QuantityStatus.NEGATIVE:
                transaction_quantity =transaction_quantity + int(row.get('quantity'))
        return transaction_quantity
    
    #Count records with missing quantities.
    def get_missing_quantity(self):
        missing_quantity=0
        for row in self.data:
             if(self.get_quantity_classification(row.get('quantity'))==QuantityStatus.MISSING):
                 missing_quantity += 1
        return missing_quantity
    
    #Count records with invalid, non-numeric quantities.
    def get_invalid_quantity(self):
        invalid_quantity=0
        for row in self.data:
            if self.get_quantity_classification(row.get('quantity'))==QuantityStatus.INVALID:
                invalid_quantity += 1
        return invalid_quantity
    
    #Identify negative quantities and count them separately.
    def get_negative_quantity(self):
        negative_quantity=0
        for row in self.data:
            if self.get_quantity_classification(row.get('quantity'))==QuantityStatus.NEGATIVE:
                negative_quantity += 1
            
        return negative_quantity
    
    
    def get_quantity_classification(self,quantity):
        if(quantity is None or str(quantity).strip() == ''):
            return QuantityStatus.MISSING
        try:
            if  int(quantity) < 0:
                return QuantityStatus.NEGATIVE
        except ValueError:
            return QuantityStatus.INVALID
        return QuantityStatus.VALID
        
   