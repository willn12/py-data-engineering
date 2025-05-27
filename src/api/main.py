from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from typing import Dict, Any
import logging
from ..etl.loan_processor import LoanDataProcessor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Fannie Mae Data Engineering Demo",
    description="API for processing and analyzing housing and loan data",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the loan processor
loan_processor = LoanDataProcessor()

@app.get("/")
async def root():
    """Root endpoint returning API information."""
    return {
        "message": "Welcome to the Fannie Mae Data Engineering Demo API",
        "endpoints": {
            "/process-loans": "Process loan data from CSV file",
            "/metrics": "Get current loan metrics",
            "/health": "Check API health"
        }
    }

@app.post("/process-loans")
async def process_loans(file: UploadFile = File(...)) -> Dict[str, Any]:
    """
    Process loan data from a CSV file.
    
    Args:
        file: CSV file containing loan data
        
    Returns:
        Dictionary containing processing results and metrics
    """
    try:
        # Read the uploaded file
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        # Process the data
        cleaned_data, metrics = loan_processor.process_loan_data(df)
        
        return {
            "message": "Successfully processed loan data",
            "metrics": metrics,
            "sample_data": cleaned_data.head().to_dict(orient='records')
        }
        
    except Exception as e:
        logger.error(f"Error processing loan data: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 

