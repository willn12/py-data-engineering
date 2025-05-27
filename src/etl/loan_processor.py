import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoanDataProcessor:
    def __init__(self, ):
        self.required_columns = [
            'loan_id',
            'origination_date',
            'original_loan_amount',
            'interest_rate',
            'loan_term',
            'property_state',
            'property_type',
            'loan_to_value_ratio'
        ]

    def validate_data(self, df: pd.DataFrame) -> bool:
        """Validate that df has all the required columns"""
        missing_columns = set(self.required_columns) - set(df.columns)
        if missing_columns:
            logger.error(f"Missing required columns: {missing_columns}")
            return False
        return True
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the data"""
        if not self.validate_data(df):
            raise ValueError("Invalid data, missing required columns")
        
        #copy of df
        df_clean = df.copy()

        # Convert origination_date to datetime
        df_clean['origination_date'] = pd.to_datetime(df_clean['origination_date'])

        # Clean numeric columns
        numeric_columns = ['original_loan_amount', 'interest_rate', 'loan_to_value_ratio']
        for col in numeric_columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

         # Clean categorical columns
        df_clean['property_state'] = df_clean['property_state'].str.upper()
        df_clean['property_type'] = df_clean['property_type'].str.title()
        
        # Handle missing values
        df_clean['credit_score'] = df_clean['credit_score'].fillna(-1)
        df_clean['delinquency_status'] = df_clean['delinquency_status'].fillna('Unknown')

        return df_clean
    
    def calculate_metrics(self, df: pd.DataFrame) -> dict:
        """Calculate metrics for the data"""
        metrics = {
            'total_loans': len(df),
            'total_loan_amount': df['original_loan_amount'].sum(),
            'avg_loan_amount': df['original_loan_amount'].mean(),
            'avg_interest_rate': df['interest_rate'].mean(),
            'avg_loan_to_value': df['loan_to_value_ratio'].mean(),
            'loans_by_state': df['property_state'].value_counts().to_dict(),
            'loans_by_type': df['property_type'].value_counts().to_dict(),
            'delinquency_rate': (df['delinquency_status'] != 'Current').mean() if 'delinquency_status' in df.columns else None
        }
        return metrics
    
    def process_loan_data(self, input_data: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
        """Main method to process loan data."""
        try:
            # Clean the data
            cleaned_data = self.clean_data(input_data)
            
            # Calculate metrics
            metrics = self.calculate_metrics(cleaned_data)
            
            logger.info(f"Successfully processed {len(cleaned_data)} loan records")
            return cleaned_data, metrics
            
        except Exception as e:
            logger.error(f"Error processing loan data: {str(e)}")
            raise
        
        

