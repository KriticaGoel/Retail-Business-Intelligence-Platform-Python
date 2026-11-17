from enums.quantity_status import QuantityStatus
import logging
 
logger=logging.getLogger(__name__)

class TransactionAnalyzer:
    
    def __init__(self,data):
        self.data=data

    #Calculate total valid transaction quantities.
    def get_total_quantity(self) -> int:
        transaction_quantity=0
        for row in self.data:
           status = self.get_quantity_classification(row.get("quantity"))
           if status == QuantityStatus.VALID:
                transaction_quantity += int(row.get("quantity"))
                
        logger.info(f"Total transaction quantity : {transaction_quantity}")
        return transaction_quantity
    
    #Count records with missing quantities.
    def get_missing_quantity(self) -> int:
        missing_quantity=0
        for row in self.data:
             if(self.get_quantity_classification(row.get('quantity'))==QuantityStatus.MISSING):
                 missing_quantity += 1
        return missing_quantity
    
    #Count records with invalid, non-numeric quantities.
    def get_invalid_quantity(self) -> int:
        invalid_quantity=0
        for row in self.data:
            if self.get_quantity_classification(row.get('quantity'))==QuantityStatus.INVALID:
                invalid_quantity += 1
        return invalid_quantity
    
    #Identify negative quantities and count them separately.
    def get_negative_quantity(self) -> int:
        negative_quantity=0
        for row in self.data:
            if self.get_quantity_classification(row.get('quantity'))==QuantityStatus.VALID and int(row.get('quantity')) < 0:
                negative_quantity += 1
            
        return negative_quantity
    
    
    def get_quantity_classification(self,qty) -> QuantityStatus:
        try:
            if(qty is None or str(qty).strip() == ''):
                return QuantityStatus.MISSING
            elif int(qty) <0:
                return QuantityStatus.VALID
        except TypeError , ValueError:
            return QuantityStatus.INVALID
        return QuantityStatus.VALID
        
   