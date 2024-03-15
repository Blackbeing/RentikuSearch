
from fastapi import APIRouter, Depends, Form, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from RentikuSearch.models import crud, models
from RentikuSearch.models.database import get_db

router = APIRouter()

templates = Jinja2Templates(directory="RentikuSearch/web_fastapi/templates")


@router.get("/signup")
async def signup(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("signup.html", context=context)


@router.post("/signup")
async def signup_post(
    response: Response,
    request: Request,
    email: str = Form(),
    username: str = Form(),
    password: str = Form(),
    db: Session = Depends(get_db),
):
    errors = []

    if not email:
        errors.append("Enter valid email")
    if not password:
        errors.append("Password Required")
    try:
        db_user_email = crud.get_user_by_email(db, email=email)
        if db_user_email:
            errors.append("Email is already in use")
            return templates.TemplateResponse(
                "signup.html", {"request": request, "errors": errors}
            )

        db_user_username = crud.get_user_by_username(db, username=username)
        if db_user_username:
            errors.append("Username is already in use")
            return templates.TemplateResponse(
                "signup.html", {"request": request, "errors": errors}
            )

        try:
            user = models.User(
                email=email, username=username, password=password
            )
            create_user = crud.create_user(db, user)
            if create_user:
                response = RedirectResponse("/login", status_code=302)
        except Exception as e:
            errors.append(e)
            return templates.TemplateResponse(
                "signup.html", {"request": request, "errors": errors}
            )

        return response

    except Exception as e:
        errors.append(e)
        return templates.TemplateResponse(
            "signup.html", {"request": request, "errors": errors}
        )


#     except Exception as e:
#         errors.append("Something went wrong\n\t {}\n\n".format(e))
#         return templates.TemplateResponse(
#             "login.html", {"request": request, "errors": errors}
#         )
