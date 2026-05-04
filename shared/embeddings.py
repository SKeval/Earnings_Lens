from huggingface_hub import InferenceClient
from config.settings import settings

client = InferenceClient(token=settings.HUGGINGFACE_API_KEY)

async def get_embedding(text: str) -> list[float]:
    result = client.feature_extraction(
        text,
        model="sentence-transformers/all-MiniLM-L6-v2"
    )
    return result.tolist()