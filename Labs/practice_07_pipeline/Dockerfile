# ---- Base image ----
    FROM python:3.10-slim

    # ---- System dependencies ----
    RUN apt-get update && apt-get install -y \
        libgl1 libglib2.0-0 libpq-dev \
        && rm -rf /var/lib/apt/lists/*
    
    # ---- Set working directory ----
    WORKDIR /app
    
    # ---- Copy dependencies ----
    COPY requirements.txt .
    
    
    # ---- Install the rest of requirements ----
    RUN pip install --no-cache-dir -r requirements.txt
    
    # ---- Copy project files ----
    COPY . .
    
    # ---- Create folder for frames ----
    RUN mkdir -p detected_frames
    
    # ---- Expose port ----
    EXPOSE 8000
    
    # ---- Run FastAPI app ----
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    