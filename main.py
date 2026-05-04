import asyncio
from agents.ingestion_agent import run_ingestion

def main():
    asyncio.run(run_ingestion("0000320193"))#


if __name__ == "__main__":
    main()