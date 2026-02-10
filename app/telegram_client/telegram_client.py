import httpx
from app.config import TELEGRAM_BOT_TOKEN
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

transport = httpx.AsyncHTTPTransport(
    local_address="0.0.0.0",
    retries=0
)

timeout = httpx.Timeout(
    connect=10.0,
    read=20.0,
    write=10.0,
    pool=10.0
)

client = httpx.AsyncClient(
    transport=transport,
    timeout=timeout,
    http2=False
)

async def send_message(chat_id: int, text: str):
    resp = await client.post(
        f"{BASE_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text
        }
    )

    if resp.status_code != 200:
        print("❌ ERRO TELEGRAM:", resp.status_code, resp.text)


async def get_file(file_id: str) -> bytes:
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/getFile", params={"file_id": file_id})
        file_path = r.json()["result"]["file_path"]

        file_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}"
        file = await client.get(file_url)
        return file.content
