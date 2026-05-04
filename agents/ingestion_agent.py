from shared.db import get_connection, init_db
from shared.embeddings import get_embedding
from shared.edgar_client import get_filings


async def run_ingestion(cik: str) -> None:
    await init_db()
    data = await get_filings(cik)
    print(data)