from pydantic import BaseModel
from models import Gender
from typing import Optional, List

class CreateAndUpdateStudent(BaseModel):
    name : str
    email : str
    gender : Gender
    useGlass : bool
    displayWidth : int
    displayHeight : int

class Student(CreateAndUpdateStudent):
    id : int
    
    class Config:
        orm_mode = True

class CreateAndUpdateGazeInfo(BaseModel):
    Timestamp : str
    GazeLeftx : float
    GazeLefty : float
    GazeRightx : float
    GazeRighty : float
    PupilLeft : float
    PupilRight : float
    FixationSeq : float
    SaccadeSeq : float
    Blink : float
    GazeAOI : float
    student_id : int
    batchNo : int


class GazeInfo(CreateAndUpdateGazeInfo):
    id : int

    class Config:
        orm_mode = True


class PaginatedStudentInfo(BaseModel):
    limit: int
    offset: int
    data: List[Student]


class PaginatedGazeInfo(BaseModel):
    limit: int
    offset: int
    data: List[GazeInfo]


class CreateAndUpdateGazeInfoDerived(BaseModel):
    time_to_peak_pupil : int
    peak_pupil : float
    pupil_mean : float
    pupil_slope : float
    pupil_area_curve : float
    blink_rate : float
    peak_blink_duration : int
    avg_blink_duration : int
    fixation_count : int
    max_fixation_duration : int
    avg_fixation_duration : float
    sacc_count : int
    sacc_duration : int
    sacc_vel : float
    sacc_amplitude : float
    micro_sacc_count : int
    first_pass_duration : int
    second_pass_duration : int
    batchNo : int

class GazeInfoDerived(CreateAndUpdateGazeInfoDerived):
    id : int

    class Config:
        orm_mode = True