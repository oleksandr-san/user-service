from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, List

from app import crud
from app.api import deps
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[User])
def get_users(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Get a multiple users
    """
    result = crud.user.get_multi(db=db, skip=skip, limit=limit)

    return result


@router.get("/{user_id}", status_code=200, response_model=User)
def get_user(
    *,
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a single user by ID
    """
    result = crud.user.get(db=db, id=user_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )

    return result


@router.delete("/{user_id}", status_code=204)
def delete_user(
    *,
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single user by ID
    """
    result = crud.user.remove(db=db, id=user_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )


@router.post("/", status_code=201, response_model=User)
def create_user(
    *, user_in: UserCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new user in the database.
    """
    user = crud.user.create(db=db, obj_in=user_in)

    return user


@router.put("/{user_id}", status_code=200, response_model=User)
def update_user(
    *, 
    user_id: int,
    user_in: UserUpdate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new user in the database.
    """
    user = crud.user.update(db=db, obj_in=user_in)

    return user