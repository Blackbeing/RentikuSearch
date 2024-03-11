from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from RentikuSearch import dependancies as dp
from RentikuSearch.models import crud
from RentikuSearch.models.database import get_db

router = APIRouter()

templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@router.get("/login")
async def login(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("login.html", context=context)


@router.post("/login")
async def login_post(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
):
    errors = []
    if not form_data.username:
        errors.append("Enter valid email")
    if not form_data.password:
        errors.append("Wrong password")
    try:
        db_user = crud.get_user_by_username(db, username=form_data.username)
        if not db_user:
            errors.append("User does not exist")
            return templates.TemplateResponse(
                "login.html", {"request": request, "errors": errors}
            )
        else:
            if not dp.verify_password(form_data.password, db_user.password):
                errors.append("Wrong username or password")
                return templates.TemplateResponse(
                    "login.html", {"request": request, "errors": errors}
                )

            else:
                token = dp.create_access_token(
                    data={"sub": form_data.username}
                )
                print(token)
                response = templates.TemplateResponse(
                    "login.html",
                    {"request": request, "msg": "Login Successfully"},
                )
                response.set_cookie(
                    key="access_token",
                    value="Bearer {}".format(token),
                    httponly=True,
                )
                # response = templates.TemplateResponse("index.html", {"request": Request, "msg": "Login Successfully"})
                return response
    except Exception as e:
        errors.append("Something went wrong\n\t {}\n\n".format(e))
        return templates.TemplateResponse(
            "login.html", {"request": request, "errors": errors}
        )
