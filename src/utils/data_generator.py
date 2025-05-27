import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from typing import List, Dict

class LoanDataGenerator:
    def __init__(self, num_records: int = 1000):
        self.num_records = num_records
        self.states = [
            'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
        ]
        self.property_types = [
            'Single Family',
            'Condo',
            'Townhouse',
            'Multi Family',
            'Manufactured'
        ]
        self.delinquency_statuses = [
            'Current',
            '30 Days Late',
            '60 Days Late',
            '90 Days Late',
            'Foreclosure'
        ]
    
    def generate_loan_id(self) -> str:
        """Generate a unique loan ID."""
        return f"L{random.randint(100000, 999999)}"
    
    def generate_origination_date(self) -> datetime:
        """Generate a random origination date within the last 2 years."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=730)  # 2 years
        random_days = random.randint(0, (end_date - start_date).days)
        return start_date + timedelta(days=random_days)
    
    def generate_loan_amount(self) -> float:
        """Generate a random loan amount between $100,000 and $1,000,000."""
        return round(random.uniform(100000, 1000000), 2)
    
    def generate_interest_rate(self) -> float:
        """Generate a random interest rate between 3% and 7%."""
        return round(random.uniform(0.03, 0.07), 4)
    
    def generate_loan_term(self) -> int:
        """Generate a random loan term (15 or 30 years)."""
        return random.choice([180, 360])  # 15 or 30 years in months
    
    def generate_ltv_ratio(self) -> float:
        """Generate a random loan-to-value ratio between 0.5 and 0.95."""
        return round(random.uniform(0.5, 0.95), 2)
    
    def generate_credit_score(self) -> int:
        """Generate a random credit score between 580 and 850."""
        return random.randint(580, 850)
    
    def generate_sample_data(self) -> pd.DataFrame:
        """Generate a sample dataset of loan records."""
        data = []
        
        for _ in range(self.num_records):
            loan_amount = self.generate_loan_amount()
            property_value = loan_amount / self.generate_ltv_ratio()
            
            record = {
                'loan_id': self.generate_loan_id(),
                'origination_date': self.generate_origination_date(),
                'original_loan_amount': loan_amount,
                'interest_rate': self.generate_interest_rate(),
                'loan_term': self.generate_loan_term(),
                'property_state': random.choice(self.states),
                'property_type': random.choice(self.property_types),
                'loan_to_value_ratio': self.generate_ltv_ratio(),
                'credit_score': self.generate_credit_score(),
                'delinquency_status': random.choice(self.delinquency_statuses)
            }
            data.append(record)
        
        return pd.DataFrame(data)
    
    def save_to_csv(self, filename: str = 'sample_loan_data.csv'):
        """Generate and save sample data to a CSV file."""
        df = self.generate_sample_data()
        df.to_csv(filename, index=False)
        return filename

if __name__ == "__main__":
    # Generate a sample dataset with 1000 records
    generator = LoanDataGenerator(num_records=1000)
    filename = generator.save_to_csv()
    print(f"Generated sample data saved to {filename}") 