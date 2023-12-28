from pydantic import BaseModel
from typing import Optional
from enum import Enum

# 쓰레기 분류
class TrashType(str, Enum):
    일반쓰레기 = "일반쓰레기"
    플라스틱 = "플라스틱"
    캔 = "캔"
    유리 = "유리"
    종이 = "종이"

# model이 받아야 하는 데이터 타입 선언
class ModelRequest(BaseModel):
    image: str

# model이 반환해야 하는 데이터 타입 선언
class ModelResponse(BaseModel):
    answer: TrashType

# tts 쿼리를 위해 받아야 하는 데이터 타입 선언
class TTSRequest(BaseModel):
    name: str

# tts 쿼리가 반환해야 하는 데이터 타입 선언
class TTSResponse(BaseModel):
    query: str