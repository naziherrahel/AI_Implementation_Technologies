# Practice : Docker – FastAPI + PostgreSQL

## Objective
Learn how to use Docker to run and manage servise FastAPI + PostgreSQL applications. Explore images, containers, volumes, and networking.

---

## Step 0 – Setup
- Make sure your FastAPI + PostgreSQL is working locally.

---

## Task 1 – Containers & Images
1. Use Docker to **list all images** on your system.
2. Check if your old FastAPI image exists.  
   *(Hint: `docker images`)*

---

## Task 2 – Build & Run
1. Build a new FastAPI Docker image (`tag it v3`).
2. Start your FastAPI + PostgreSQL containers using `docker-compose`.
3. Confirm that both containers are running.  
   *(Hint: `docker ps`)*

---

## Task 3 – Inspect & Access
1. Enter the FastAPI container and confirm you can **see environment variables**.
2. Connect to PostgreSQL from inside the container using `psql`.  
   *(Hint: `docker exec` and `psql` docs)*

---

## Task 4 – Volumes & Persistence
1. Create a **new Docker volume** for PostgreSQL.
2. Modify `docker-compose.yml` to use the new volume.
3. Insert a detection via API.
4. Stop and start the database container and confirm the data is still there.  
   *(Hint: check if POSTed data persists)*

---

## Task 5 : 
1. Run **two FastAPI containers** pointing to the same database but different ports.
2. Test both APIs simultaneously.

---

## Deliverables
- Screenshots:
  - `docker ps` with running containers
  - API POST + GET requests returning data
  - Data persistence after restart
- Short notes:
  - How volumes preserved data
  - How FastAPI connects to PostgreSQL
  - Environment variables tested

---

### Notes:
- Use the **official Docker documentation** to find commands.
- Don’t copy/paste blindly — understand what each command does.

