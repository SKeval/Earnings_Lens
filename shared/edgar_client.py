import httpx


async def get_filings(cik: str) -> dict:
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    headers = {
        "User-Agent": "EarningsLens contact@earningslens.com"
        }
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=headers)
        return response.json()  