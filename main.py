# 나는야 서버
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
memos=[]
app = FastAPI()

class Memo(BaseModel):
    id:str
    content:str

#Create
@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return "메모추가성공"

#Read
@app.get('/memos')
def read_memo():
    return memos

#Update
@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return "성공했습니다."
    return "그런 메모는 없습니다."

#Delete
@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    for index, memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(index)
            return "삭제되었습니다."
    return "그런 메모는 없습니다."

app.mount("/", StaticFiles(directory='static', html=True), name='static')