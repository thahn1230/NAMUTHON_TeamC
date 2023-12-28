from pydantic import BaseModel
from typing import Optional
from enum import Enum


class TrashType(str, Enum):
    일반쓰레기 = "일반쓰레기"
    플라스틱 = "플라스틱"
    캔 = "캔"
    유리 = "유리"
    종이 = "종이"


class ModelRequest(BaseModel):
    image: str

class ModelResponse(BaseModel):
    answer: TrashType

class TTSRequest(BaseModel):
    name: str

class TTSResponse(BaseModel):
    query: str