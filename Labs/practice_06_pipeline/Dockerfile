# --- Base Python image ---
    FROM python:3.10-slim


    RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*
    
    # --- Set the working directory inside the container ---
    WORKDIR /app
    
    # --- Copy dependency list and install Python packages ---
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # --- Copy all project files into the container ---
    COPY . .
    
    # --- Expose port 8000 for FastAPI ---
    EXPOSE 8000
    
    # --- Command to start the FastAPI server ---
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    