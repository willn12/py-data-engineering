import os
from src.utils.data_generator import LoanDataGenerator

def main():
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Generate sample data
    print("Generating sample data...")
    generator = LoanDataGenerator(num_records=1000)
    filename = generator.save_to_csv('data/sample_loan_data.csv')
    print(f"Sample data generated successfully: {filename}")
    
    # Start the FastAPI server
    print("\nStarting FastAPI server...")
    print("Visit http://localhost:8000/docs")
    print("Use the /process-loans endpoint to upload the generated CSV file")
    
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main() 