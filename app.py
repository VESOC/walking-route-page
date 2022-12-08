from typing import List
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from github import Github
from createPage import createPage
from dotenv import load_dotenv
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/templates', StaticFiles(directory='templates'))

class WayPoint:
    pointName = ''
    pointDescription = ''
    pointCoord = [0.0, 0.0]
    pointImage = ''

class Route:
    routeName = ''
    routeDescription = ''
    routeImages = ['']
    routeWayPoints = []


@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@app.post('/upload/{user_id}/create/{route_id}')
async def route(user_id: str, route_id: str, route: dict):
    page_encoded = await createPage(route)
    g = Github(os.environ['GTOKEN'])
    repo = g.get_repo('vesoc/walking-route-page')
    re = repo.create_file(path=f'pages/{route_id}.html', message=f'Create {route_id}.html', content=page_encoded, branch='main')

from requests_toolbelt import MultipartEncoder
import requests
import base64
@app.post('/images')
async def images(images: list[UploadFile] = File(...)):
    resp = {}
    for i, file in enumerate(images):
        url = f"https://api.imgbb.com/1/upload?key={os.environ['IMGBB_API']}"
        payload = {
                "image": base64.b64encode(file.file.read()),
            }
        m = MultipartEncoder(fields=payload)
        res = requests.post(url, payload)
        print(res.json()['medium']['url'])
        resp[i] = res.json()
    return resp