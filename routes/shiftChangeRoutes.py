from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.shiftChangeSchema import CreateShiftChange, UpdateShiftChange, GetShiftChangeReport
from models.shiftChangeModel import ShiftChange
from database import get_db


router = APIRouter(
    prefix='/time_and_attendance/api/shift_change',
    tags=['shift_change']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    shift_change = db.query(ShiftChange).filter(ShiftChange.active_status == 'Active').all()
    return {'shift_change': shift_change}

@router.get('/employee/{id}')
def all_employee(id: str, db: Session = Depends(get_db)):
    shift_change = db.query(ShiftChange).filter(ShiftChange.employee_id == id).filter(ShiftChange.active_status == 'Active').all()
    return {'shift_change': shift_change}


@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    shift_change = db.query(ShiftChange).filter(ShiftChange.id == id).filter(ShiftChange.active_status == 'Active').first()
    if not shift_change:
        raise HTTPException(404, 'Shift Change not found')
    return {'shift_change': shift_change}

@router.get('/datatables/{id}')
def read(id: str, db: Session = Depends(get_db)):
    shift_change = db.query(ShiftChange).filter(ShiftChange.id == id).filter(ShiftChange.active_status == 'Active').all()
    if not shift_change:
        raise HTTPException(404, 'Shift Change not found')
    return {'shift_change': shift_change}

@router.post('/')
def store(shift_change: CreateShiftChange, db: Session = Depends(get_db)):
    to_store = ShiftChange(
        user_id = shift_change.user_id,
        shift_type_id = shift_change.shift_type_id,
        employee_id = shift_change.employee_id,
        employee_type_id = shift_change.employee_type_id,
        monday = shift_change.monday,
        tuesday = shift_change.tuesday,
        wednesday = shift_change.wednesday,
        thursday = shift_change.thursday,
        friday = shift_change.friday,
        saturday = shift_change.saturday,
        sunday = shift_change.sunday,
    )

    db.add(to_store)
    db.commit()
    
    return {'message': 'Shift Change stored successfully.'}

@router.put('/{id}')
def update(id: str, shift_change: CreateShiftChange, db: Session = Depends(get_db)): 
    if not db.query(ShiftChange).filter(ShiftChange.id == id).update({
        'user_id': shift_change.user_id,
        'shift_type_id': shift_change.shift_type_id,
        'employee_type_id': shift_change.employee_type_id,
        'employee_id': shift_change.employee_id,
        'monday': shift_change.monday,
        'tuesday': shift_change.tuesday,
        'wednesday': shift_change.wednesday,
        'thursday': shift_change.thursday,
        'friday': shift_change.friday,
        'saturday': shift_change.saturday,
        'sunday': shift_change.sunday,
    }):
        raise HTTPException(404, 'User to update is not found')
    db.commit()
    return {'message': 'Shift Change updated successfully.'}

@router.put('/delete/{id}')
def remove(id: str,  db: Session = Depends(get_db)):
    if not db.query(ShiftChange).filter(ShiftChange.id == id).update({
        'active_status': "Inactive",
    }):
        raise HTTPException(404, 'Shift Change to delete is not found')
    db.commit()
    return {'message': 'Shift Change removed successfully.'}

@router.put('/update/{id}')
def remove(shift_change: UpdateShiftChange, id: str,  db: Session = Depends(get_db)):
    if not db.query(ShiftChange).filter(ShiftChange.id == id).update({
        'status': shift_change.status,
    }):
        raise HTTPException(404, 'Shift Change to update is not found')
    db.commit()
    return {'message': 'Shift Change update successfully.'}



@router.post('/reports/{id}')
def all(id: str, report: GetShiftChangeReport, db: Session = Depends(get_db)):
    shift_change = db.query(ShiftChange).filter(ShiftChange.employee_id == id).filter(ShiftChange.created_at >= report.start_date).filter(ShiftChange.created_at <= report.end_date).filter(ShiftChange.active_status == "Active").all()
    return {'shift_change': shift_change}


@router.post('/reports_all')
def all(report: GetShiftChangeReport, db: Session = Depends(get_db)):
    shift_change = db.query(ShiftChange).filter(ShiftChange.created_at >= report.start_date).filter(ShiftChange.created_at <= report.end_date).filter(ShiftChange.active_status == "Active").all()
    return {'shift_change': shift_change}