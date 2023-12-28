from fastapi import FastAPI, HTTPException
from app.middleware_config import add_middleware
from .models.models import ModelRequest, ModelResponse, TrashType

app = FastAPI()

add_middleware(app)


@app.get("/")
def root():
    return {"status": 200, "message": "hello from server"}


@app.post("/get_response_from_model", response_model=ModelResponse)
async def get_response_from_model(item: ModelRequest):
    answer = TrashType.일반쓰레기
    return ModelResponse(answer=answer)
