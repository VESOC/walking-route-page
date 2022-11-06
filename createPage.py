header = '''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta viewport="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
    <meta name="robots" content="noindex,nofollow" />
</head>
<body>'''

footer = '''<footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <p class="col-md-4 mb-0 text-muted">© 2022 걷기 앱</p>

    <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
      <svg class="bi me-2" width="40" height="32">TODO use icon</svg>
    </a>
  </footer>
</body>
</html>'''

content = '''<div class="container-fluid">
    <div id="imageCarousel" class="carousel slide" data-bs-ride="true">
        <div class="carousel-indicators">
            REP:CarouselBtn
        </div>
        <div class="carousel-inner">
            REP:CarouselItem
        </button>
      </div>
    </div>
      <nav>
        <div class="nav nav-tabs" id="nav-tab" role="tablist">
          <button class="nav-link active" id="nav-route-tab" data-bs-toggle="tab" data-bs-target="#nav-route" type="button" role="tab" aria-controls="nav-route" aria-selected="true">산책로 설명</button>
            REP:TabBtn
        </div>
      </nav>
      <div class="tab-content" id="nav-tabContent">
        REP:TabDiv
        </div>
</div>'''

from base64 import b64encode

async def createPage(data):
    carouselBtn, carouselItems = getCarosel(data['routeImages'], len(data['routeImages']))
    tabBtns, tabItems = getTabs(data['routeDescription'], data['waypoints'])
    pageData = header + content.replace('REP:CarouselBtn', carouselBtn).replace('REP:CarouselItem', carouselItems).replace('REP:TabBtn', '\n'.join(tabBtns)).replace('REP:TabDiv', '\n'.join(tabItems)) + footer
    page_bytes = pageData.encode('utf-8')
    return page_bytes


def getCarosel(img, n):
    return createCarouselBtn(n), createCarouselItems(img, n)

def createCarouselBtn(n: int):
    base = '''
    <button type="button"
    data-bs-target="#imageCarousel"
    data-bs-slide-to"N"
    class="CLS"
    aria-current="true"
    aria-label="Image N">
    </button>'''
    res = ''
    for i in range(1, n+1):
        res += base.replace('N', str(i)).replace('CLS', 'active' if i == 1 else '') + '\n'
    return res

def createCarouselItems(img, n: int):
    base = '''
    <div class="carousel-item CLS">
        <img src="IMG" class="d-block w-100">
    </div>'''
    res = ''
    for i in range(1, n+1):
        res += base.replace('IMG', img[i-1]).replace('CLS', 'active' if i == 1 else '') + '\n'
    return res

def getTabs(routeDescription, waypoints):
    tabBtns, tabItems = [], []
    tabItems.append(createTabItem(0, routeDescription))
    for i, waypoint in enumerate(waypoints):
        tabBtns.append(createWaypointTabBtn(i+1, waypoint['waypointName']))
        tabItems.append(createTabItem(i+1, waypoint['waypointDescription']))
    return tabBtns, tabItems

def createWaypointTabBtn(i, waypointName):
    return f'<button class="nav-link" id="nav-{i}-tab" data-bs-toggle="tab" data-bs-target="#nav-{i}" type="button" role="tab" aria-controls="nav-{i}" aria-selected="true">{waypointName}</button>'

def createTabItem(i, description):
    if i:
        return f'<div class="tab-pane" id="nav-{i}" role="tabpanel" aria-labelledby="nav-{i}-tab" tabindex="0">{description}</div>'
    return f'<div class="tab-pane fade show active" id="nav-route" role="tabpanel" aria-labelledby="nav-route-tab" tabindex="0">{description}</div>'