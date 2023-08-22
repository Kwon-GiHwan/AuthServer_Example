
from pydantic import BaseModel
from typing import Optional
class Response(BaseModel):
    meta: dict
    data: dict

class Meta(BaseModel):
    code: int
    message: str

class Data(BaseModel):
    data: Optional[dict] = None


def response_builder(code: int, message: str, input_data = None):

    meta = Meta()
    meta.code = code
    meta.message = message

    data = Data()
    data.data = input_data

    response = Response()
    response.meta = meta
    response.data = data

    return response