from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

import mizu

from os.path import exists


app = FastAPI()


def parse(filename: str) -> str:
    PATH = "contents/{}".format(filename)
    if not exists(PATH):
        raise HTTPException(
            status_code=404,
            detail="存在しないページへようこそ(?)"
        )
    with open(PATH, "r") as f:
        return mizu.parse(f.read())

@app.get("/", response_class=HTMLResponse)
async def main():
    return parse("index.md")

@app.get("/{file_path:path}", response_class=HTMLResponse)
async def file(file_path: str):
    return parse("{}.md".format(file_path))
