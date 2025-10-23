from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    task_id: str
    project: str
    description: str

@app.post("/task")
async def handle_task(task: Task):
    print("Backend Agent received:", task.description)
    code = f"from fastapi import APIRouter\nrouter = APIRouter()\n@router.get('/{task.project}')\ndef get():\n    return {{'message': 'Hello from {task.project}'}}"
    return {"task_id": task.task_id, "status": "done", "files": [{"path": "src/api/routes.py", "content": code}]}

