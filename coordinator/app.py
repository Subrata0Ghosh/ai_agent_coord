from fastapi import FastAPI, Body
from gpt4all import GPT4All
import requests, os, json
from pathlib import Path

app = FastAPI()

MODEL_PATH = "/home/asus/.cache/huggingface/hub/models--orel12--ggml-gpt4all-j-v1.3-groovy/snapshots/9ff9297dc2b604b9845e8c3f38ec338fa5ea8179"
MODEL_FILE = "ggml-gpt4all-j-v1.3-groovy.bin"

llm = GPT4All(model_name=MODEL_FILE, model_path=MODEL_PATH, allow_download=False)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/submit_brief")
async def submit_brief(brief: dict = Body(...)):
    project = brief.get("project", "UntitledProject")
    text = brief.get("brief", "")

    # 🧠 Local LLM generates structured tasks
    prompt = f"""
    Split this project into frontend and backend tasks:
    {text}
    Return JSON only, like:
    [{{"type":"frontend","description":"..." }},{{"type":"backend","description":"..."}}]
    """

    tasks_raw = llm.generate(prompt, max_tokens=300)

    try:
        tasks_str = tasks_raw.strip().split("```")[-1]
        tasks = json.loads(tasks_str)
    except Exception:
        tasks = [
            {"type": "frontend", "description": "Build UI"},
            {"type": "backend", "description": "Build API"},
        ]

    results = []

    for i, t in enumerate(tasks, start=1):
        task = {
            "task_id": str(i),
            "project": project,
            "description": t["description"],
        }

        # 🎯 Send to correct agent
        if t["type"].lower() == "frontend":
            url = "http://127.0.0.1:9001/task"
        else:
            url = "http://127.0.0.1:9002/task"

        try:
            res = requests.post(url, json=task, timeout=10)
            results.append(res.json())
        except Exception as e:
            results.append({"task_id": i, "error": str(e)})

    summary_path = os.path.join(OUTPUT_DIR, f"{project}_summary.json")
    with open(summary_path, "w") as f:
        json.dump({"project": project, "results": results}, f, indent=2)

    return {"project": project, "results": results}
