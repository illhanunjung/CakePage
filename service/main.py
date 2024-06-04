import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from service.api.cci_get import get_value, get_history

# CORS 설정
origins = [
    "http://localhost:3001", 
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def read_data():
    data = get_value()
    return {"data": data}
  
@app.get("/graph")
def get_graph(tag: str = Query(...)):
    hist = get_history(tag)
    print(hist)
    return hist

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
