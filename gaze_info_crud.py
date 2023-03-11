from typing import List
from sqlalchemy.orm import Session
from exceptions import StudentInfoNotFoundError, StudentInfoInfoAlreadyExistError
from models import GazeInfo
from schemas import CreateAndUpdateGazeInfo
from fastapi import APIRouter, Depends, HTTPException
from database import get_db


def create_gaze_info(session : Session ,gaze_info: CreateAndUpdateGazeInfo) -> str:
    try:
        new_gaze_info = GazeInfo(**gaze_info.dict())
        print("aashche dada")
        print(new_gaze_info.__dict__)
        session.add(new_gaze_info)
        # session.commit()
        # session.refresh(new_gaze_info)
        print(gaze_info)
    except Exception as e:
        print(e)
    # print(new_gaze_info)
    
    return "Created create crud info"


def get_gaze_infos(session: Session, limit: int, offset: int) -> List[GazeInfo]:
    return session.query(GazeInfo).offset(offset).limit(limit).all()