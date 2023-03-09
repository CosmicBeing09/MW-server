from fastapi import FastAPI
import student_apis, gaze_info_apis
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(student_apis.router)
app.include_router(gaze_info_apis.router)