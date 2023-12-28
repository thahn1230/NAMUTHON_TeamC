from fastapi import FastAPI, HTTPException, UploadFile, File
from app.middleware_config import add_middleware
from .models.models import ModelRequest, ModelResponse, TrashType, TTSRequest, TTSResponse
import json

from services.classify_picture import classify_image
from services.process_img import img_to_np_array
from app.models.models import TrashType

app = FastAPI()

add_middleware(app)


@app.get("/")
def root():
    return {"status": 200, "message": "hello from server"}


@app.post("/get_response_from_model", response_model=ModelResponse)
async def get_response_from_model(file: UploadFile = File(...)):
    img_np = await img_to_np_array(file)
    prediction_index = await classify_image(img_np)
    
    trash_types = list(TrashType)
    predicted_trash_type = trash_types[prediction_index].value
    
    print(predicted_trash_type)
    return ModelResponse(answer=predicted_trash_type)

@app.post("/get_tts_query", response_model=TTSResponse)
async def get_tts_query(item: TTSRequest):
    with open("./data/recycle_time.json", 'r') as file:
        data_json = json.load(file)
    return data_json[item.query]
