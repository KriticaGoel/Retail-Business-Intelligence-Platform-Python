from enum import Enum

class QuantityStatus(Enum):
    VALID = "Valid"
    MISSING = "Missing"
    INVALID = "Invalid"
    NEGATIVE = "Negative"