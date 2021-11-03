from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from routes import shiftChangeRoutes, userRoutes, userTypeRoutes, employeeTypeRoutes, employeeRoutes, shiftTypeRoutes, timeInRoutes, timeOutRoutes, attendanceRoutes, leaveTypeRoutes, leaveSubTypeRoutes, leaveRoutes, authRoutes, missedTimeRoutes
from database import get_db
# from models.postModel import Post

# Register template folder
template = Jinja2Templates('templates')

app = FastAPI(debug=True)
# Mount static folder
app.mount('/static', StaticFiles(directory='static'), name='static')

# Register Routes
app.include_router(authRoutes.router)
app.include_router(userRoutes.router)
app.include_router(userTypeRoutes.router)
app.include_router(employeeTypeRoutes.router)
app.include_router(employeeRoutes.router)
app.include_router(shiftTypeRoutes.router)
app.include_router(timeInRoutes.router)
app.include_router(timeOutRoutes.router)
app.include_router(attendanceRoutes.router)
app.include_router(leaveTypeRoutes.router)
app.include_router(leaveSubTypeRoutes.router)
app.include_router(leaveRoutes.router)
app.include_router(missedTimeRoutes.router)
app.include_router(shiftChangeRoutes.router)
# app.include_router(postRoutes.router)


@app.get('/home', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/home.html', {
        'request': request,
    })

@app.get('/homedashboard', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/homedashboard.html', {
        'request': request,
    })

@app.get('/time_and_attendance/login', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/login.html', {
        'request': request,
    })

@app.get('/time_and_attendance/logout', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/logout.html', {
        'request': request,
    })

# ADMIN SIDE

# USER MANAGEMENT
@app.get('/time_and_attendance/admin/user', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/admin/user.html', {
        'request': request,
})
    
@app.get('/time_and_attendance/admin/user_type', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/admin/user_type.html', {
        'request': request,
})

# SYSTEM CONFIG
@app.get('/time_and_attendance/admin/employee_type', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/admin/employee_type.html', {
        'request': request,
})
    
@app.get('/time_and_attendance/admin/shift_type', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/admin/shift_type.html', {
        'request': request,
})

@app.get('/time_and_attendance/admin/leave_type', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/admin/leave_type.html', {
        'request': request,
})
  

@app.get('/time_and_attendance/admin/leave_sub_type', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/admin/leave_sub_type.html', {
        'request': request,
})
  
# END OF ADMIN SIDE

# HR SIDE

@app.get('/time_and_attendance/hr/employee', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/employee.html', {
        'request': request,
})

@app.get('/time_and_attendance/hr/custom_time_in_out', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/custom_time_in_out.html', {
        'request': request,
})
    

@app.get('/time_and_attendance/hr/leave_application', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/leave_application.html', {
        'request': request,
})

@app.get('/time_and_attendance/hr/leave_approved', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/leave_approved.html', {
        'request': request,
})

    
@app.get('/time_and_attendance/hr/time_logging', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/time_logging.html', {
        'request': request,
})
    
@app.get('/time_and_attendance/hr/missed_time_application', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/missed_time_application.html', {
        'request': request,
})
    
@app.get('/time_and_attendance/hr/shift_and_schedule_application', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/shift_and_schedule_application.html', {
        'request': request,
})
    
@app.get('/time_and_attendance/hr/leave_reports', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/leave_reports.html', {
        'request': request,
})


@app.get('/time_and_attendance/hr/shift_and_schedule_reports', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/shift_and_schedule_reports.html', {
        'request': request,
})


@app.get('/time_and_attendance/hr/attendance_reports', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/hr/attendance_reports.html', {
        'request': request,
})
    
# END OF HR SIDE

# EMPLOYEE SIDE

@app.get('/time_and_attendance/employee/employee', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/employee/employee.html', {
        'request': request,
})


@app.get('/time_and_attendance/employee/leave_application', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/employee/leave_application.html', {
        'request': request,
})

@app.get('/time_and_attendance/employee/missed_time_application', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/employee/missed_time_application.html', {
        'request': request,
})
    
    
@app.get('/time_and_attendance/employee/shift_and_schedule_application', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/employee/shift_and_schedule_application.html', {
        'request': request,
})
    
@app.get('/time_and_attendance/employee/leave_reports', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/employee/leave_reports.html', {
        'request': request,
})
    
    
@app.get('/time_and_attendance/employee/shift_and_schedule_reports', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/employee/shift_and_schedule_reports.html', {
        'request': request,
})
    
@app.get('/time_and_attendance/employee/attendance_reports', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    return template.TemplateResponse('time_and_attendance/employee/attendance_reports.html', {
        'request': request,
})
    

    

# END OF EMPLOYEE SIDE

