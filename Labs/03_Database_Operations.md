
# Practice A_1: PostgreSQL & Python – Database Operations

## Objective
Use Python (psycopg2) to connect to a PostgreSQL database, create a table, insert sample records, and query them.

## Pre-requisites
- PostgreSQL installed 
- psycopg2 installed: `pip install psycopg2-binary`
- Database `dust_detection` must exist

## Step-by-step Instructions

### Setup
1. Open terminal and start your PostgreSQL server.
2. Edit `db_config.py` to match your DB credentials.

### Create Table & Insert Data
```bash
python setup_database.py
```
You should see: `Table created and sample data inserted.`

###  Query the Table
```bash
python query_database.py
```
You should see a printed list of all entries sorted by timestamp.

##  Your Tasks
- [ ] Add a new detection manually by modifying `setup_database.py`
- [ ] Extend schema to include fields like `camera_angle`, `temperature`, or `model_version`
- [ ] Use SQL `UPDATE` to change the confidence of a row
- [ ] Use a `WHERE` clause to filter by `camera_id` in `query_database.py`
- [ ] BONUS: Write a function to insert new detections from Python input

##  Submission
- Screenshot: terminal output after running both scripts, and modified schema and filtered results.
