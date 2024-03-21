import asyncio
import sys

import uvicorn

import argparse

argparser = argparse.ArgumentParser(description="RentikuSearch Argparser")

argparser.add_argument(
    'instance',
    choices=['api', 'web'],
    help="instance to run [web, api]",
)
argparser.add_argument('-H', "--host", help="host to serve")
argparser.add_argument('-p', "--port", type=int, help="port to serve")
argparser.add_argument("-r",
                       "--reload",
                       action="store_true",
                       help="reload server (for dev)")


def run_api(host="0.0.0.0", port=5050, reload=False):
    uvicorn.run("RentikuSearch.api.v1.app:app",
                host=host,
                port=port,
                reload=reload)


def run_web(host="0.0.0.0", port=8000, reload=False):
    uvicorn.run("RentikuSearch.web_fastapi.app:app",
                host=host,
                port=port,
                reload=reload)


def main():
    args = argparser.parse_args()
    host, port, reload, instance = args.host, args.port, args.reload, args.instance

    if instance == "api":
        run_api(host, port, reload)
    elif instance == "web":
        run_web(host, port, reload)


if __name__ == "__main__":
    main()
