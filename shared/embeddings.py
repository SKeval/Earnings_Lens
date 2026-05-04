from config import settings
import httpx

async def get_embedding(text: str) -> list[float]:
    url = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    headers = {
        "Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"
        }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json={"inputs": text})
        return response.json()  