from fastapi import FastAPI, Response, Request, Body, Depends
from Model.CoursekeyVerify import *
from Model.StudentCheckIn import *
from Model.UserAccount import *
from Service.AccountService import *
from Service.BaseOAuthService import *
from Service.GoogleOAuthService import *
from Service.JWTService import *
from Service.RollcallService import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_methods=['*']
)

@app.post("/register/")
async def PostRegister(request: Request):
    a = await request.json()
    account = UserAccount(**a)
    AccountService().Register(account)
    token = JWTService().encode(account.ID)
    return token
    

@app.post("/login/", status_code=200)
async def PostLogin(response: Response, request: Request):
    tmp = await request.json()
    account = UserAccount(**tmp)
    if AccountService().Login(account):
        token = JWTService().encode(account.ID)
        return token
    else:
        response.status_code=401

@app.get("/logout/")
async def GetLogout():
    AccountService().Logout()

@app.get("/rollcall/")
async def GetRollcall(courseKey:str):
    print(RollcallService().GetStudentList(courseKey))
    return RollcallService().GetStudentList(courseKey)

@app.post("/rollcall/")
async def PostRollcall(request: Request):
    tmp = await request.json()
    tmp['Owner'] = JWTService().decode(request.headers['authorization'])['username']
    info = CoursekeyVerify(**tmp)
    return RollcallService().StartRollcall(info)


@app.get("/googleoauth/") # Not sure method
async def PostGoogleOAuth(state,access_token):
    GoogleOAuthService().InsertStudentInfo(access_token,state)