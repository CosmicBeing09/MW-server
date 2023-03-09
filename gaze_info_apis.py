from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from gaze_info_crud import create_gaze_info, get_gaze_infos
from database import get_db
from schemas import GazeInfo, PaginatedGazeInfo, CreateAndUpdateGazeInfo
from typing import List

router = APIRouter()

@cbv(router)
class GazeInfo:
    session: Session = Depends(get_db)

    @router.post("/gaze")
    def add_gazeInfo(self, gaze_info: List[CreateAndUpdateGazeInfo]):

        try:
            for tempData in gaze_info:
                # print(tempData.dict())
                gaze_info = create_gaze_info(self.session, tempData)
            return "Created"
        except Exception as cie:
            print(**cie.__dict__)

    
    @router.get("/gaze", response_model=PaginatedGazeInfo)
    def list_gaze_info(self, limit: int = 10, offset: int = 0):

        gaze_list = get_gaze_infos(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": gaze_list}

        return response
