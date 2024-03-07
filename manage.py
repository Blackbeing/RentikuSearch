import asyncio
import sys

import uvicorn


async def run_api():
    uvicorn.run("RentikuSearch.api.v1.app:app",
                host="0.0.0.0",
                port=5050,
                reload=True)


async def run_web():
    uvicorn.run(
        "RentikuSearch.web_fastapi.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    choice = sys.argv[1]
    if choice == "api":
        asyncio.run(run_api())
    elif choice == "web":
        asyncio.run(run_web())
