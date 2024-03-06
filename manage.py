import asyncio

import uvicorn


async def main():
    uvicorn.run(
        "RentikuSearch.api.v1.app:app", host="0.0.0.0", port=8000, reload=True
    )


if __name__ == "__main__":
    asyncio.run(main())
