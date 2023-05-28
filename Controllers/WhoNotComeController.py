from fastapi import FastAPI
from Model import *
from Service import *

app = FastAPI()

@app.post("/register/")
def PostRegister(account:UserAccount.UserAccount):
    AccountService.AccountService().Register(account)
    

@app.post("/login/")
def PostLogin(account:UserAccount.UserAccount):
    AccountService.AccountService().Login(account)

@app.get("/logout/")
def GetLogout(account:UserAccount.UserAccount):
    AccountService.AccountService().Logout(account)

@app.get("/getStudentList/")
def GetRollcall(courseKey:StudentCheckin.StudentCheckin):
    RollcallService.Rollcall().GetStudentList(courseKey)

@app.post("/rollcall/")
def PostRollcall(info:CoursekeyVerify.CoursekeyVerify):
    RollcallService.Rollcall().StartRollcall(info)


@app.get("/googleoauth/") # Not sure method
def PostGoogleOAuth(state,access_token):
    GoogleOAuthService.GoogleOAuthService().InsertStudentInfo(access_token,state)