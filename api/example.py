# !pip install fastapi
# !pip install uvicorn

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from datetime import datetime
import json
import uvicorn
from typing import Union
from DTB_CNTR import db_connector

import HTTPException

app = FastAPI()


db = db_connector.Database()

def mod_df(df):
  df = df.astype({"item_name": str}, errors='raise')
  df = df.astype({"price": int}, errors='raise')
  df = df.astype({"date": str}, errors='raise')

  return df

@app.get("/read/get_prc")
def read_item(item_name: Union[str, None]= None, st: Union[str, None]= None, ed: Union[str, None] = None, entire: Union[bool, None]= None):
  #item id - date - price 열 반환하기

  #그다음 할거 - 크롤러 만들기 - 사실 파라미터 변경해주기
  #그다음 할거 - scheduler 적용한거

  if((st is None) or (ed is None)):
    df = db.getPred(schema='public', table='price', entire=True)

  else:
    try:
      st_date = datetime.strptime(st, "%Y-%m-%d")
      ed_date = datetime.strptime(ed, "%Y-%m-%d")
    except:
      return {"date type error"}

    df = db.getPred(schema='public', table='price', colum='date', st_date=st_date, ed_date=ed_date, entire=False)


  return json.loads(df[[ 'price', 'date','item_name']].to_json(orient='records'))

@app.get("/insert/ins_prc")
def insert_item(item_id: int, st: str, ed:str): #MSA로 갈 경우 API로 통신할것(공통DB 사용하지 않는 경우)

  try:
    st_date = st.strftime("%Y-%m-%D")
    ed_date = ed.strftime("%Y-%m-%D")
  except:
    raise HTTPException(status_code=404, detail="Item not found")

  #그다음 할거 - 크롤러 만들기 - 파라미터 변경해주기
  #그다음 할거 - scheduler 적용한거

  df = pd.DataFrame([db.readDB(schema='schema',table='table',colum='date', st_date = st_date, ed_date = ed_date)], columns=['date', 'item_name', 'price'])

  res = df.to_json(orient='records')
  # res = df.to_json(orient='index')
  ret = json.loads(res)
  return ret

def server_main():
  # uvicorn.run("WEB_SRVR.web_server:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
  uvicorn.run("WEB_SRVR.web_server:app", host="localhost", port=8000, reload=True, log_level="info")

