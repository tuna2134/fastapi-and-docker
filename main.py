from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import mizu

from os.path import exists


app = FastAPI()
templates = Jinja2Templates(directory="templates")


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
    return templates.TemplateResponse("base.html", {"content": parse("{}.md".format(file_path))})
