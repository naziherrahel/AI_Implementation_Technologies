Practice 3_1: FastAPI Introduction

##  Objective
Build a minimal FastAPI application that serves dummy detection data via a REST API.

##  Structure
- `main.py`: Contains FastAPI app
- `GET /detections`: Returns filtered list of detection entries
- `GET /ping`: Health check endpoint

##  How to Run

###  1. Install requirements (in a virtual env)
```bash
pip install fastapi uvicorn pydantic
```

### 2. Run server
```bash
python main.py
```
Or if using `uvicorn` directly:
```bash
uvicorn main:app --reload
```

###  3. Test endpoints
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → Swagger UI
- Example query:
```bash
curl "http://127.0.0.1:8000/detections?min_confidence=0.8"
```

## Key Concepts
- `@app.get` decorators
- Pydantic models for structured response
- Query parameter filtering

## Your Tasks 
1. **Add POST endpoint**: `POST /detections` to accept a new detection via body
2. **Custom error**: Raise 404 if no detections match query
3. **Add timestamp range filter**: filter by `start_time`, `end_time`
4. **Optional: Write unit tests** using `pytest` or `httpx`

## Submission
Submit:
- Screenshot of Swagger UI response
- Extended script (if any changes made)
- Markdown doc (max 1 page) explaining:
  - What endpoints you tested
  - What you added/modified
