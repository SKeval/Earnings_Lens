from shared.db import get_connection, init_db
from shared.embeddings import get_embedding
from shared.edgar_client import get_filings
from shared.chunker import chunk_text
import json


async def run_ingestion(cik: str) -> None:
    await init_db()
    data = await get_filings(cik)
    text = str(data)
    chunks = chunk_text(text)
    conn = await get_connection()
    for chunk in chunks:
        embedding = await get_embedding(chunk)
        sql = "INSERT INTO embeddings (content, metadata, embedding) VALUES ($1, $2, $3)"
        await conn.execute(sql, chunk, json.dumps({}), json.dumps(embedding))