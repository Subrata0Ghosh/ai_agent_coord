from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    task_id: str
    project: str
    description: str

def generate_backend_code(description: str, project: str):
    if "login" in description.lower():
        return {
            "path": "src/api/auth.py",
            "content": """from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post('/login')
def login(username: str, password: str):
    if username == "admin" and password == "1234":
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
"""
        }

    # Default fallback
    return {
        "path": "src/api/routes.py",
        "content": f"""from fastapi import APIRouter

router = APIRouter()

@router.get('/{project.replace(" ", "_")}')
def get():
    return {{'message': 'Hello from {project}'}}"""
    }

@app.post("/task")
async def handle_task(task: Task):
    print("Backend Agent received:", task.description)
    file_data = generate_backend_code(task.description, task.project)
    return {"task_id": task.task_id, "status": "done", "files": [file_data]}
