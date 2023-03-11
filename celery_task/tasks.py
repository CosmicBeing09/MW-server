from celery import shared_task
from gaze_info_crud import create_gaze_info
from sqlalchemy.orm import Session
from schemas import CreateAndUpdateGazeInfo
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db


# session: Session = Depends(get_db)
@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='gaze_infos:create_gaze_info_tasks')
def create_gaze_info_tasks(self, gaze_info: List[CreateAndUpdateGazeInfo] , session : Session = next(get_db())) -> str:
    for tempData in gaze_info:
        # print(tempData.dict())
        gaze_data = create_gaze_info(session, tempData)
        # print(str(gaze_data))
    session.commit()
    return "return-task"
