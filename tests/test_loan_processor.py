import pytest
import pandas as pd
from src.etl.loan_processor import LoanDataProcessor

@pytest.fixture
def sample_data():
    """Create a sample DataFrame for testing."""
    data = {
        'loan_id': ['L123456', 'L789012'],
        'origination_date': ['2023-01-01', '2023-02-01'],
        'original_loan_amount': [300000.00, 400000.00],
        'interest_rate': [0.045, 0.055],
        'loan_term': [360, 180],
        'property_state': ['CA', 'NY'],
        'property_type': ['Single Family', 'Condo'],
        'loan_to_value_ratio': [0.80, 0.75],
        'credit_score': [750, 800],
        'delinquency_status': ['Current', '30 Days Late']
    }
    return pd.DataFrame(data)

def test_validate_data(sample_data):
    processor = LoanDataProcessor()
    assert processor.validate_data(sample_data) is True

def test_clean_data(sample_data):
    """Test data cleaning functionality."""
    processor = LoanDataProcessor()
    cleaned_data = processor.clean_data(sample_data)
    
    # Check data types
    assert isinstance(cleaned_data['origination_date'].iloc[0], pd.Timestamp)
    assert isinstance(cleaned_data['original_loan_amount'].iloc[0], float)
    assert isinstance(cleaned_data['interest_rate'].iloc[0], float)
    
    # Check string formatting
    assert cleaned_data['property_state'].iloc[0] == 'CA'
    assert cleaned_data['property_type'].iloc[0] == 'Single Family'

def test_calculate_metrics(sample_data):
    """Test metrics calculation."""
    processor = LoanDataProcessor()
    cleaned_data = processor.clean_data(sample_data)
    metrics = processor.calculate_metrics(cleaned_data)
    
    # Check basic metrics
    assert metrics['total_loans'] == 2
    assert metrics['total_loan_amount'] == 700000.00
    assert metrics['avg_loan_amount'] == 350000.00
    assert metrics['avg_interest_rate'] == 0.05
    
    # Check state distribution
    assert metrics['loans_by_state']['CA'] == 1
    assert metrics['loans_by_state']['NY'] == 1

def test_process_loan_data(sample_data):
    """Test the complete loan processing pipeline."""
    processor = LoanDataProcessor()
    cleaned_data, metrics = processor.process_loan_data(sample_data)
    
    # Check that both cleaned data and metrics are returned
    assert isinstance(cleaned_data, pd.DataFrame)
    assert isinstance(metrics, dict)
    assert len(cleaned_data) == 2
    assert metrics['total_loans'] == 2

def test_invalid_data():
    """Test handling of invalid data."""
    processor = LoanDataProcessor()
    invalid_data = pd.DataFrame({'invalid_column': [1, 2, 3]})
    
    with pytest.raises(ValueError):
        processor.clean_data(invalid_data)
