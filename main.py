from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import mizu

from os.path import exists


app = FastAPI()
with open("templates/base.html", "r") as f:
    BASE_HTML = f.read()


def parse(filename: str) -> str:
    PATH = "contents/{}".format(filename)
    if not exists(PATH):
        raise HTTPException(
            status_code=404,
            detail="存在しないページへようこそ(?)"
        )
    with open(PATH, "r") as f:
        return BASE_HTML.format(content=mizu.parse(f.read()))

@app.get("/", response_class=HTMLResponse)
async def main():
    return parse("index.md")

@app.get("/{file_path:path}", response_class=HTMLResponse)
async def file(request: Request, file_path: str):
    return parse("{}.md".format(file_path))
