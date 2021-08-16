from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from routes import userRoutes, userTypeRoutes, userProfileRoutes, employeeRoutes, shiftTypeRoutes, timeInRoutes, timeOutRoutes, attendanceRoutes, leaveTypeRoutes, leaveRoutes
from database import get_db
# from models.postModel import Post

# Register template folder
template = Jinja2Templates('templates')

app = FastAPI(debug=True)
# Mount static folder
app.mount('/static', StaticFiles(directory='static'), name='static')

# Register Routes
app.include_router(userRoutes.router)
app.include_router(userTypeRoutes.router)
app.include_router(userProfileRoutes.router)
app.include_router(employeeRoutes.router)
app.include_router(shiftTypeRoutes.router)
app.include_router(timeInRoutes.router)
app.include_router(timeOutRoutes.router)
app.include_router(attendanceRoutes.router)
app.include_router(leaveTypeRoutes.router)
app.include_router(leaveRoutes.router)
# app.include_router(postRoutes.router)


@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    # posts = db.query(Post).all()
    return template.TemplateResponse('index.html', {
        'request': request,
        # 'posts': posts
    })


