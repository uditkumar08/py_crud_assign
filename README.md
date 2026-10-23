# Python CRUD API

A beginner-friendly task API built with **FastAPI**. Create, view, update, and
delete tasks using JSON over HTTP. Run it with Python or Docker, then explore
the endpoints in FastAPI's interactive documentation.

> **Note:** Tasks are stored in memory. They disappear when the app stops or
> restarts. This project is a simple learning example, not a persistent
> production database.

## What you need

- **Python 3.10 or newer** for a local run
- **Git** to clone the project and use GitHub or GitLab
- **Docker Desktop** (Windows/macOS) or Docker Engine (Linux) for a Docker run

You only need Docker to use the Docker instructions.

## Get the project

Clone it from the GitHub or GitLab repository:

```bash
git clone <repository-url>
cd py_crud_assign
```

Replace `<repository-url>` with the URL shown by your repository host. For
example:

```bash
git clone https://github.com/YOUR-USERNAME/py_crud_assign.git
```

Or download the repository as a ZIP and extract it.

## Run locally with Python

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

If PowerShell blocks virtual environment activation, you can run the venv's
Python directly instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

The API is now available at <http://localhost:8000>.

## Run with Docker

Make sure Docker Desktop or Docker Engine is running, then, from the project
folder:

```bash
docker build -t python-crud-api .
docker run --name python-crud-api -p 8000:8000 python-crud-api
```

Open <http://localhost:8000/docs> to try the API. The `-p 8000:8000` option
maps port 8000 inside the container to port 8000 on your computer.

To stop the container, press `Ctrl+C`. To remove its stopped container:

```bash
docker rm python-crud-api
```

If port 8000 is already in use, map a different host port, for example
`-p 8001:8000`, and open <http://localhost:8001/docs>.

## Try the API

### Interactive API documentation

Visit <http://localhost:8000/docs> and expand an endpoint to see its inputs,
submit a request, and inspect the response. The alternative documentation
page is <http://localhost:8000/redoc>.

### Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/health` | Check that the API is running |
| `POST` | `/tasks` | Create a task |
| `GET` | `/tasks` | List all tasks |
| `GET` | `/tasks/{task_id}` | Get one task |
| `PUT` | `/tasks/{task_id}` | Replace a task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

A task has three input fields:

```json
{
  "task": "Read the Docker guide",
  "description": "Build and run the project in a container",
  "is_done": false
}
```

The API assigns each task an `id` and includes it in responses. For example,
create a task with `curl`:

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"task\":\"Read the Docker guide\",\"description\":\"Build and run the project in a container\",\"is_done\":false}"
```

Example response:

```json
{
  "task": "Read the Docker guide",
  "description": "Build and run the project in a container",
  "is_done": false,
  "id": 1
}
```

List tasks:

```bash
curl http://localhost:8000/tasks
```

Get task `1`:

```bash
curl http://localhost:8000/tasks/1
```

Update task `1` (send all three task fields):

```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d "{\"task\":\"Read the Docker guide\",\"description\":\"I finished the guide\",\"is_done\":true}"
```

Delete task `1`:

```bash
curl -X DELETE http://localhost:8000/tasks/1
```

The examples use `curl`, available on most systems. In Windows PowerShell,
use `curl.exe` in place of `curl` if `curl` refers to PowerShell's web-request
alias.

Requests for a task ID that does not exist return `404 Task not found`.

## Git basics

Check which files have changed:

```bash
git status
```

Stage and commit your changes:

```bash
git add README.md
git commit -m "Improve project documentation"
```

Replace `README.md` with the files you actually changed, or use `git add .` to
stage all changes after reviewing `git status`.

## Push to GitHub or GitLab

1. Create a **blank repository** on [GitHub](https://github.com/) or
   [GitLab](https://gitlab.com/). If you are pushing this existing project,
   avoid initializing the new repository with another README.
2. Copy the repository's HTTPS or SSH URL from the host.
3. In a terminal at the project folder, check whether a remote is already set:

   ```bash
   git remote -v
   ```

4. If there is no `origin` remote, add the URL you copied:

   ```bash
   git remote add origin <repository-url>
   ```

   For example, a GitLab URL looks like
   `https://gitlab.com/YOUR-USERNAME/py_crud_assign.git`; a GitHub URL looks
   like `https://github.com/YOUR-USERNAME/py_crud_assign.git`.

5. Push the current `main` branch:

   ```bash
   git branch -M main
   git push -u origin main
   ```

If `origin` already exists but points to a different repository, inspect it
with `git remote -v` and update it only if you intend to replace that
destination:

```bash
git remote set-url origin <repository-url>
```

GitHub and GitLab may ask you to authenticate. Follow the host's current
instructions for HTTPS credentials or SSH keys; do not put passwords or
access tokens in this README or in Git.

After the first push, the usual workflow is:

```bash
git add .
git commit -m "Describe your change"
git push
```

## Project files

```text
.
├── main.py            # FastAPI app and in-memory task CRUD endpoints
├── requirements.txt   # Python dependencies
├── Dockerfile         # Instructions for building the container image
├── .dockerignore      # Files excluded from the Docker build context
└── README.md          # Project and setup instructions
```

## Troubleshooting

- **`python` is not recognized on Windows:** Try `py` instead, or install
  Python and enable the option to add it to `PATH`.
- **Port 8000 is busy:** Stop the other service or use a different host port,
  such as `docker run --name python-crud-api -p 8001:8000 python-crud-api`.
- **Docker cannot connect:** Start Docker Desktop (or the Docker Engine
  service) and retry.
- **A task disappeared:** This API uses an in-memory dictionary; restarting
  the process clears all tasks.
- **`git push` is rejected:** Check that the remote URL is correct and that
  you have permission to push. If the remote repository already has commits,
  fetch and reconcile those changes before pushing.