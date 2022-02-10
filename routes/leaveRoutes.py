from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.leaveSchema import CreateLeave, GetLeave, GetLeaveReport, GetLeaveReportMonth
from models.leaveModel import Leave
from database import get_db


router = APIRouter(
    prefix='/time_and_attendance/api/leave',
    tags=['leave']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    leave = db.query(Leave).all()
    return {'leave': leave}

@router.get('/')
def all(db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.active_status == 'Active').filter(Leave.employee_id == user.id).all()
    return {'leave': leave}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.id == id).first()
    if not leave:
        raise HTTPException(404, 'Leave not found')
    return {'leave': leave}

@router.post('/')
def store(leave: CreateLeave, db: Session = Depends(get_db)):
    to_store = Leave(
        employee_id = leave.employee_id,
        leave_type_id = leave.leave_type_id,
        leave_sub_type_id = leave.leave_sub_type_id,
        title = leave.title,
        reason = leave.reason,
        start_date = leave.start_date,
        end_date = leave.end_date,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Leave stored successfully.'}

@router.put('/{id}')
def update(id: str, leave: CreateLeave, db: Session = Depends(get_db)): 
    if not db.query(Leave).filter(Leave.id == id).update({
        "employee_id" : leave.employee_id,
        "leave_type_id" : leave.leave_type_id,
        "leave_sub_type_id" : leave.leave_sub_type_id,
        "title" : leave.title,
        "reason" : leave.reason,
        "start_date" : leave.start_date,
        "end_date" : leave.end_date,
        'status': leave.status
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Leave updated successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)):
    if not db.query(Leave).filter(Leave.id == id).delete():
        raise HTTPException(404, 'User to delete is not found')
    db.commit()
    return {'message': 'Leave removed successfully.'}


@router.post('/getApprovedLeave')
def all(leave_req: GetLeave, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.start_date == leave_req.start_date).filter(Leave.status == "Approved").all()
    return {'leave': leave}


@router.get('/userleave/{id}')
def all(id: str, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.employee_id == id).filter(Leave.active_status == "Active").all()
    return {'leave': leave}



@router.post('/reports/{id}')
def all(id: str, report: GetLeaveReport, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.employee_id == id).filter(Leave.start_date >= report.start_date).filter(Leave.start_date <= report.end_date).filter(Leave.active_status == "Active").all()
    return {'leave': leave}


@router.post('/reports_all')
def all(report: GetLeaveReport, db: Session = Depends(get_db)):
    leave = db.query(Leave).filter(Leave.start_date >= report.start_date).filter(Leave.start_date <= report.end_date).filter(Leave.active_status == "Active").all()
    return {'leave': leave}

@router.get('/count/')
def count(db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.active_status == "Active").count()
    return {'count': count}

@router.get('/count/approved/')
def count(db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.active_status == "Active").filter(Leave.status == "Approved").count()
    return {'count': count}

@router.get('/count/denied/')
def count(db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.active_status == "Active").filter(Leave.status == "Declined").count()
    return {'count': count}

@router.post('/count/{id}')
def count(id: str, db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.employee_id == id).filter(Leave.active_status == "Active").count()
    return {'count': count}

@router.post('/count/approved/{id}')
def count(id: str, db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.employee_id == id).filter(Leave.active_status == "Active").filter(Leave.status == "Approved").count()
    return {'count': count}

@router.post('/count/denied/{id}')
def count(id: str, db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.employee_id == id).filter(Leave.active_status == "Active").filter(Leave.status == "Declined").count()
    return {'count': count}

@router.post('/count/approved_month/')
def count(month: GetLeaveReportMonth, db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.start_date >= month.start).filter(Leave.start_date <= month.end).filter(Leave.active_status == "Active").filter(Leave.status == "Approved").count()
    return {'count': count}

@router.post('/count/declined_month/')
def count(month: GetLeaveReportMonth, db: Session = Depends(get_db)):
    count = db.query(Leave).filter(Leave.start_date >= month.start).filter(Leave.start_date <= month.end).filter(Leave.active_status == "Active").filter(Leave.status == "Declined").count()
    return {'count': count}