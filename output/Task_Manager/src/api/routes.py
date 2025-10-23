from fastapi import APIRouter
router = APIRouter()
@router.get('/Task Manager')
def get():
    return {'message': 'Hello from Task Manager'}