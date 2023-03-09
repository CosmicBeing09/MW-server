from typing import List
from sqlalchemy.orm import Session
from exceptions import StudentInfoNotFoundError, StudentInfoInfoAlreadyExistError
from models import StudnetInfo
from schemas import CreateAndUpdateStudent

def get_all_student(session: Session, limit: int, offset: int) -> List[StudnetInfo]:
    return session.query(StudnetInfo).offset(offset).limit(limit).all()


def get_student_info_by_id(session: Session, _id: int) -> StudnetInfo:
    student_info = session.query(StudnetInfo).get(_id)

    if student_info is None:
        raise StudentInfoNotFoundError

    return student_info

def get_student_info_by_email(session: Session, _email : str) -> StudnetInfo:
    student_info = session.query(StudnetInfo).filter(StudnetInfo.email == _email).first()

    if student_info is None:
        raise StudentInfoNotFoundError
    
    return student_info


def create_student(session: Session, student_info: CreateAndUpdateStudent) -> StudnetInfo:
    student_details = session.query(StudnetInfo).filter(StudnetInfo.email == student_info.email).first()
    if student_details is not None:
        return student_details

    new_Student_info = StudnetInfo(**student_info.dict())
    session.add(new_Student_info)
    session.commit()
    session.refresh(new_Student_info)
    return new_Student_info