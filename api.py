from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from assistant import KubanGuide

app = FastAPI()

# Настройки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

# Инициализация бота
bot = KubanGuide()

@app.post("/api/assistant")
async def handle_assistant_request(request: QueryRequest):
    try:
        # Передаем запрос в бота и получаем ответ
        bot_response = bot.generate_response(request.query)
        return {"response": bot_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)