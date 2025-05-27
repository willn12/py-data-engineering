from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class LoanData(BaseModel):
    loan_id: str = Field()
    origination_date: date = Field()
    original_loan_amount: float = Field()
    interest_rate: float = Field()
    loan_term: int = Field()
    property_state: str = Field()
    property_type: str = Field()
    loan_to_value_ratio: float = Field()
    credit_score: Optional[int] = Field(None)
    delinquency_status: Optional[str] = Field(None)
