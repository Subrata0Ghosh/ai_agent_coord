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
    filename = task.description.replace(" ", "_") + ".py"
    return {
        "task_id": task.task_id,
        "status": "done",
        "files": [
            {
                "path": f"src/api/{filename}",
                "content": f"# Auto-generated API route\nprint('Backend task: {task.description}')"
            }
        ]
    }
