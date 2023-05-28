from fastapi import FastAPI, Response
from Model import *
from Service import *

app = FastAPI()

@app.post("/register/")
def PostRegister(account:UserAccount.UserAccount):
    AccountService.AccountService().Register(account)
    

@app.post("/login/")
def PostLogin(response: Response, account:UserAccount.UserAccount):
    if AccountService.AccountService().Login(account):
        token = JWTService.JWTService().de

@app.get("/logout/")
def GetLogout():
    AccountService.AccountService().Logout()

@app.get("/getStudentList/")
def GetRollcall(courseKey:str):
    RollcallService.Rollcall().GetStudentList(courseKey)

@app.post("/rollcall/")
def PostRollcall(info:CoursekeyVerify.CoursekeyVerify):
    RollcallService.Rollcall().StartRollcall(info)


@app.get("/googleoauth/") # Not sure method
def PostGoogleOAuth(state,access_token):
    GoogleOAuthService.GoogleOAuthService().InsertStudentInfo(access_token,state)