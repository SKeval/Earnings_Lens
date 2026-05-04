import asyncpg
from config.settings import settings


async def get_connection():
    return await asyncpg.connect(settings.SUPABASE_URL)

    
async def init_db():
        conn = await get_connection()
        await conn.execute(
            '''
            CREATE EXTENSION IF NOT EXISTS vector
            '''
        )
        await conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS embeddings (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            content TEXT,
            metadata JSONB,
            embedding vector(384)
)
            '''
        )
    
    
