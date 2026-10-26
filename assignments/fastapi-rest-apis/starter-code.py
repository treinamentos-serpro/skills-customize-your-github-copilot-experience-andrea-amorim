from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


# Use an in-memory collection to store tasks and assign unique IDs.
tasks = {}
next_task_id = 1


@app.get("/tasks")
def list_tasks():
    # Return all tasks as JSON.
    pass


# TODO: Add POST /tasks to create a task.
# TODO: Add GET /tasks/{task_id} to retrieve one task.
# TODO: Add PUT /tasks/{task_id} to update a task.
# TODO: Add DELETE /tasks/{task_id} to delete a task.
