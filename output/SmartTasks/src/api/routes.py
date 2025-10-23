from fastapi import APIRouter

router = APIRouter()

@router.get('/SmartTasks')
def get():
    return {'message': 'Hello from SmartTasks'}