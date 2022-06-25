from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app import oauth2
from ..database import get_db
from .. import models, schemas, utils

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut) 
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    u = db.query(models.User).filter(models.User.email==user.email)
    print('u: ', u)
    print('user: ', user)
    if u.first() == None:
        # hash 
        hashed_password = utils.hash(user.password)
        user.password = hashed_password  
        new_user =models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'user already exists.')


@router.get('/{id}', response_model=schemas.UserOut)
def getUser(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user {id} doesnot exists.')
    return user