from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from app.middleware_config import add_middleware
from .models.models import ModelResponse, TrashType, TTSResponse
import json

from services.classify_picture import classify_image
from services.process_img import img_to_np_array
from app.models.models import TrashType

app = FastAPI()

add_middleware(app)


@app.get("/")
def root():
    return {"status": 200, "message": "hello from server"}

# 학습된 모델에게 사진 주고 어떤 종류의 쓰레기인지 예측하게 하기
@app.post("/get_response_from_model", response_model=ModelResponse)
async def get_response_from_model(file: UploadFile = File(...)):
    img_np = await img_to_np_array(file)
    prediction_index = await classify_image(img_np)
    
    trash_types = list(TrashType)
    predicted_trash_type = trash_types[prediction_index].value
    
    print(predicted_trash_type)
    return ModelResponse(answer=predicted_trash_type)

# tts로 읽어야 하는 쿼리문을 frontend로 전송
@app.post("/get_tts_query", response_model=TTSResponse)
async def get_tts_query(name: str = Form(...)):
    print(name)
    # 미리 json으로 저장해놓은 tts 쿼리문을 파일로 열기
    with open("./data/recycle_time.json", 'r', encoding='utf-8') as file:
        data_json = json.load(file)
        
    # 전달받은 name 인자와 같은 json의 query 데이터를 반환
    for entry in data_json:
        if entry["name"] == name:
            query = entry["query"]
            print(query)
            return TTSResponse(query=query)
        
    # 실패시 쿼리문이 존재하지 않는다는 것을 명시
    print(f"No matching name found for: {name}")
    return TTSResponse(query="No query found for the given name.")
