from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import mizu


app = FastAPI()


def parse(filename: str) -> str:
    with open("contents/{}".format(filename), "r") as f:
        return mizu.parse(f.read())

@app.get("/", response_class=HTMLResponse)
async def main():
    return HTMLResponse(parse("index.md"))

@app.get("/{file_path:path}", response_class=HTMLRespons)
async def file(file_path: str):
    return HTMLResponse(parse("{}.md".format(file_path)))
