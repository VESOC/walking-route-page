from fastapi import FastAPI, File, UploadFile, Request
from github import Github
from createPage import createPage
from dotenv import load_dotenv
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
app = FastAPI()

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
async def root():
    return {"message": "Hello World"}

@app.post('/route/{user_id}/create/{route_id}')
async def route(user_id: str, route_id: str, route: dict):
    page_encoded = await createPage(route)
    g = Github(os.environ['GTOKEN'])
    repo = g.get_repo('vesoc/walking-route-page')
    re = repo.create_file(path=f'pages/{route_id}.html', message=f'Create {route_id}.html', content=page_encoded, branch='main')


import requests
import base64
@app.post('/images')
async def images(file: UploadFile = File(...)):
    url = "https://api.imgbb.com/1/upload"
    payload = {
            "key": os.environ['IMGBB_API'],
            "image": base64.b64encode(file.file.read()),
        }
    res = requests.post(url, payload)
    print(res.json()['medium']['url'])