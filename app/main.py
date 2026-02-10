# app/main.py
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from app.telegram_client.telegram_client import send_message, get_file
from app.agent.agent import run_agent

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()

        message = data.get("message")
        if not message:
            return {"ok": True}

        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        if text.startswith("/"):
            await send_message(chat_id, "👋 Hello! Let's practice English 🇺🇸")
            return {"ok": True}
        
        if "text" in message:
            user_text = message["text"]
        else:
            return {"ok": True}

        try:
            response = run_agent(
                chat_id=str(chat_id),
                user_message=text
            )
        except Exception:
            response = (
                "⚠️ Estou um pouco sobrecarregado agora.\n"
                "Tente novamente em alguns segundos 😊"
            )

        await send_message(chat_id, response)

        return {"ok": True}

    except Exception as e:
        print("🔥 ERRO NO WEBHOOK:", e)
        return {"ok": False}
    

