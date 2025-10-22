# **FastAPI + YOLO Detection App — Student Deployment Guide**

> **Goal:** deploy and test a YOLOv8 detection API (FastAPI) backed by PostgreSQL using Docker on a remote GPU server. I will provide the project folder (contains `main.py`, `Dockerfile`, `docker-compose.yml`, `requirements.txt`, and `sample_video.mp4`). This guide starts from SSH key setup and covers the full deployment workflow.

---

## Quick checklist (what you should have before starting)
- Server public IP and access.
- SSH private key.
- Project folder on your local machine: `practice_07_pipeline` (contains the files above).

---

## 1. SSH key generation & install public key on server (local machine)
**Generate a key pair (local machine)**
```bash
ssh-keygen -t ed25519 -C "student@practice07"
# accept defaults (press Enter), this creates ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519.pub
```

**Copy the public key to the server (recommended)**
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub root@<server_public_ip>
```

**If `ssh-copy-id` is not available, manual method:**
```bash
cat ~/.ssh/id_ed25519.pub    # copy the printed key
# then on the server (after logging in with password or via provider console):
mkdir -p ~/.ssh && nano ~/.ssh/authorized_keys
# paste the public key, save (Ctrl+O Enter) and exit (Ctrl+X)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

**Connect to the server**
```bash
ssh -i ~/.ssh/id_ed25519 root@<server_public_ip>
```

---

## 2. Create project folder on server and upload files
**Create folder on the server (run on the server after SSH):**
```bash
mkdir -p ~/detection_app
cd ~/detection_app
```

**From local machine: copy project into the server**
```bash
# Example Windows (Git Bash):
scp -i ~/.ssh/id_ed25519 -r "/c/Users/<you>/Desktop/edu/practice_07_pipeline" root@<server_public_ip>:/root/detection_app

# Example Linux/macOS:
scp -i ~/.ssh/id_ed25519 -r ~/path/to/practice_07_pipeline root@<server_public_ip>:/root/detection_app
```

**Verify files on server**
```bash
ssh -i ~/.ssh/id_ed25519 root@<server_public_ip>
cd ~/detection_app
ls -la
# Expected: docker-compose.yml, Dockerfile, main.py, requirements.txt, sample_video.mp4, detected_frames (may be created later)
```

---

## 3. Initial server setup (install Docker & Docker Compose plugin)
Run these commands **on the server** (Ubuntu 24.04 LTS):

```bash
# update packages
apt update && apt upgrade -y

# install Docker
apt install -y docker.io
systemctl enable --now docker

# install Docker Compose (standalone binary)
curl -SL https://github.com/docker/compose/releases/download/v2.23.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
export PATH=/usr/local/bin:$PATH
hash -r

# verify
docker --version
docker-compose version

# optional: add current user to docker group so you can run docker without sudo (logout/login required)
usermod -aG docker $USER
```

**If you receive Python `distutils` errors with `docker-compose`, use the standalone binary (above) and make sure older python package is removed or moved**.

---

## 4. (If disk was resized) make OS use the new disk size
If the cloud control panel changed the disk size, the server may still be using an old partition size. Check and expand if needed.

```bash
# check partition and free space
lsblk
df -h

# if disk grew but partition didn't, install `cloud-guest-utils` then grow
apt install -y cloud-guest-utils
# example for /dev/sda1 (verify with lsblk):
growpart /dev/sda 1
resize2fs /dev/sda1
# check new size
df -h
```

> **Note:** only run this if you encounter "no space left on device" while building images.

---

## 5. Confirm project Docker files
You do **not** need to edit or paste the contents — just confirm the files exist:
```bash
cat docker-compose.yml
cat Dockerfile
cat requirements.txt
cat main.py
```

Key expectation:
- `docker-compose.yml` has `db` (postgres:15) and `app` (either `build: .` or `image:`). For this lab the `app` uses `build: .`.
- `Dockerfile` installs required Python packages (uvicorn, fastapi, psycopg2-binary, etc.) and exposes port 8000.
- `requirements.txt` contains the needed libraries.

---

## 6. Build and run the app with Docker Compose
From the project folder on the server:

```bash
# remove old containers
docker-compose down -v

# build from Dockerfile and run in background
docker-compose up -d --build

# If you want to force a clean rebuild
docker-compose build --no-cache
docker-compose up -d
```

**Check running containers**
```bash
docker ps
```
You should see `postgres_db` and `yolo_fastapi_app`.

**Follow logs**
```bash
docker-compose logs -f app
```

---

## 7. Test the detection API
**From your laptop (browser or curl):**
```
http://<server_public_ip>:8000/detect
```
**Expected response:**
```json
{ "message": "Frame saved and detection logged: detected_frames/<timestamp>.jpg" }
```

**On the server: list saved frames**
```bash
ls -lh detected_frames/
```

---

## 8. Inspect database entries
```bash
# connect to Postgres container
docker exec -it postgres_db psql -U postgres -d detection_db

# inside psql:
SELECT * FROM detections;
\q
```

---

## 9. View / download images
**Option A — quick download to local machine**
```bash
scp -i ~/.ssh/id_ed25519 root@<server_public_ip>:/root/detection_app/detected_frames/<image_name>.jpg ./
```

**Option B — serve frames via FastAPI**
Since `main.py` mounts `detected_frames` as static files, images are available at:
```
http://<server_public_ip>:8000/frames/<image_name>.jpg
```

---

## 10. Useful commands & troubleshooting notes
- Stop containers: `docker-compose down`
- Rebuild without cache: `docker-compose build --no-cache`
- Clean Docker to free space: `docker system prune -af && docker volume prune -f`
- Check disk space: `df -h`
- If old files persist after `scp`: remove the server folder first `rm -rf ~/detection_app` then re-copy.

---

## 11. Security & access notes (important)
- By default the app on port 8000 is reachable from the public Internet when server IP and firewall allow it.
- To restrict access:
  - Use the cloud provider firewall to allow only specific IPs to connect to port 8000.
---

## 12. Lab wrap-up tasks (what to submit)
- Screenshot of `/detect` JSON response.
- One downloaded detected frame (image) you obtained from the server.
- A short note (3–5 lines) about what didn’t work and how you fixed it (if anything).

---

