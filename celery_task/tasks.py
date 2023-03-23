from celery import shared_task
from gaze_info_crud import create_gaze_info
from sqlalchemy.orm import Session
from schemas import CreateAndUpdateGazeInfo
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models import GazeInfo


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='gaze_infos:create_gaze_info_tasks')
def create_gaze_info_tasks(self, gaze_info: List[CreateAndUpdateGazeInfo], session : Session = next(get_db())) -> str:
    for tempData in gaze_info:
        # gaze_data = create_gaze_info(session, tempData)
        new_gaze_info = GazeInfo(**tempData.dict())
        session.add(new_gaze_info)
    # session : Session =  get_db()
    # session.bulk_save_objects(gaze_info)
    session.commit()
    return "task executed in db"
