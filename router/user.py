from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserBase, UserDisplay
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_user
from db.models import DbUser, DbProject
from sqlalchemy import func


router=APIRouter(
    prefix="/user",
    tags=['Users'],
    responses={404: {"description": "Not found"}},
)

# CREATE USER 
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=UserDisplay,summary="Create a new user",)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    return db_user.create_user(db,request)


# GET ALL USERS
@router.get('/',status_code=status.HTTP_200_OK,response_model=list[UserDisplay],summary="Get all users",)
def get_all_users(db:Session=Depends(get_db)):
    return db_user.get_all_users(db)
