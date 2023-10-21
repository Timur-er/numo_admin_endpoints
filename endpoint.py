from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union 
from pydantic import BaseModel

from enum

router = APIRouter()

class SegmentCreateRequest(BaseModel):
    name: str
    filters: dict
    
class ChildUserResponse(BaseModel):
    id: int
    username: str
    children_num: int
    
class CreatedAtRangeUserResponse(BaseModel):
    id: int
    username: str
    created_at: str  # You can adjust the data type as needed

class RegionUserResponse(BaseModel):
    id: int
    username: str
    region_id: str

class ViberUserResponse(BaseModel):
    id: int
    username: str
    bot_type: str
    
    
class TelegramUserResponse(BaseModel):
    id: int
    username: str
    bot_type: str
    
class UnhappyUserResponse(BaseModel):
    id: int
    username: str
    is_unhappy: bool
    
class SurveyNotFinishedUserResponse(BaseModel):
    id: int
    username: str
    is_survey_not_finished: bool
    
class ActivityUserResponse(BaseModel):
    id: int
    username: str
    activity: str  # You can adjust the data type as needed

class ActiveUserResponse(BaseModel):
    id: int
    username: str
    is_active: bool
    
class RecommendationFrequencyUserResponse(BaseModel):
    id: int
    username: str
    recommendation_frequency: enum.RecommendationFrequency

    
    
class SegmentService:
    @staticmethod
    def create_segment(request_data: SegmentCreateRequest):
        try:
            # Add your segment creation logic here
            segment_name = request_data.name
            segment_filters = request_data.filters
            # Your segment creation logic here

            # If segment creation is successful, return True
            return True
        except Exception as e:
            # If an error occurs, raise an HTTPException
            raise HTTPException(status_code=500, detail="Error creating segment")

@router.post("/segment/create", response_model=bool)
async def create_segment(request_data: SegmentCreateRequest):
    return SegmentService.create_segment(request_data)

class TelegramUserService:
    @staticmethod
    def get_telegram_users(db: Session):
        return db.query(db.models.User).filter(db.models.User.bot_type == "telegram").all()

class ViberUserService:
    @staticmethod
    def get_viber_users(db: Session):
        return db.query(db.models.User).filter(db.models.User.bot_type == "Viber").all()

class ChildUserService:
    @staticmethod
    def get_child_users(db: Session, age: int):
        return db.query(db.models.User).filter(db.models.Child.age == age).all()

class RegionUserService:
    @staticmethod
    def get_users_by_region(db: Session, region_id: str):
        return db.query(db.models.User).filter(db.models.User.region_id == region_id).all()
    
class CreatedAtRangeUserService:
    @staticmethod
    def get_users_by_created_at_range(db: Session, start_date: str, end_date: str):
        return db.query(db.models.User).filter(db.models.User.created_at >= start_date, db.models.User.created_at <= end_date).all()

class RecommendationFrequencyUserService:
    @staticmethod
    def get_users_by_recommendation_frequency(db: Session, recommendation_frequency: enums.RecommendationFrequency):
        return db.query(db.models.User).filter(db.models.User.recommendation_frequency == recommendation_frequency.value).all()

class ActiveUserService:
    @staticmethod
    def get_active_users(db: Session, is_active: bool):
        return db.query(db.models.User).filter(db.models.User.is_active == is_active).all()

class UnhappyUserService:
    @staticmethod
    def get_unhappy_users(db: Session, is_unhappy: bool):
        return db.query(db.models.User).filter(db.models.User.is_unhappy == is_unhappy).all()

class SurveyNotFinishedUserService:
    @staticmethod
    def get_survey_not_finished_users(db: Session, is_survey_not_finished: bool):
        return db.query(db.models.User).filter(db.models.User.is_survey_not_finished == is_survey_not_finished).all()

class ActivityUserService:
    @staticmethod
    def get_users_by_activity(db: Session, activity: str):
        return db.query(db.models.User).filter(db.models.User.activity == activity).all()
    

@router.get("/telegram_users", response_model=List[TelegramUserResponse])
async def list_telegram_users(db: Session = Depends(get_db)):
    return TelegramUserService.get_telegram_users(db)

@router.get("/viber_users", response_model=List[ViberUserResponse])
async def list_Viber_users(db: Session = Depends(get_db)):
    return ViberUserService.get_viber_users(db)

@router.get("/users_by_age", response_model=List[ChildUserResponse])
async def list_users_by_age(age: int, db: Session = Depends(get_db)):
    return ChildUserService.get_child_users(db, age)

@router.get("/users_by_region", response_model=List[RegionUserResponse])
async def list_users_by_region(region_id: str, db: Session = Depends(get_db)):
    return RegionUserService.get_users_by_region(db, region_id)

@router.get("/users_by_region", response_model=List[RegionUserResponse])
async def list_users_by_region(region_id: str, db: Session = Depends(get_db)):
    return RegionUserService.get_users_by_region(db, region_id)

@router.get("/users_by_created_at_range", response_model=List[CreatedAtRangeUserResponse])
async def list_users_by_created_at_range(start_date: str, end_date: str, db: Session = Depends(get_db)):
    return CreatedAtRangeUserService.get_users_by_created_at_range(db, start_date, end_date)

@router.get("/users_by_recommendation_frequency", response_model=List[RecommendationFrequencyUserResponse])
async def list_users_by_recommendation_frequency(recommendation_frequency: enum.RecommendationFrequency, db: Session = Depends(get_db)):
    return RecommendationFrequencyUserService.get_users_by_recommendation_frequency(db, recommendation_frequency)

@router.get("/active_users", response_model=List[ActiveUserResponse])
async def list_active_users(is_active: bool, db: Session = Depends(get_db)):
    return ActiveUserService.get_active_users(db, is_active)

@router.get("/unhappy_users", response_model=List[UnhappyUserResponse])
async def list_unhappy_users(is_unhappy: bool, db: Session = Depends(get_db)):
    return UnhappyUserService.get_unhappy_users(db, is_unhappy)

@router.get("/survey_not_finished_users", response_model=List[SurveyNotFinishedUserResponse])
async def list_survey_not_finished_users(is_survey_not_finished: bool, db: Session = Depends(get_db)):
    return SurveyNotFinishedUserService.get_survey_not_finished_users(db, is_survey_not_finished)

@router.get("/users_by_activity", response_model=List[ActivityUserResponse])
async def list_users_by_activity(activity: Union[int, str], db: Session = Depends(get_db)):
    return ActivityUserService.get_users_by_activity(db, str(activity))

