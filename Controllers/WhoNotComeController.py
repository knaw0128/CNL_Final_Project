from fastapi import FastAPI
from Model import *
from Service import *

app = FastAPI()

@app.post("/register/{account}/{password}")
def PostRegister(account:str,password:str):
    AccountService.AccountService().Register(account,password)
    

@app.post("/login/{account}/{password}")
def PostLogin(account:str,password:str):
    AccountService.AccountService().Login(account,password)

@app.get("/logout/{account}")
def GetLogout(account):
    AccountService.AccountService().Logout(account)

@app.get("/getStudentList/{courseKey}")
def GetRollcall(courseKey:str):
    RollcallService.Rollcall().GetStudentList(courseKey)

@app.post("/rollcall/{owner}/{duration}")
def PostRollcall(owner:str,duration:float):
    RollcallService.Rollcall().StartRollcall(duration,owner)


@app.post("/googleoauth/{token}/{courseKey}") # Not sure method
def PostGoogleOAuth(token,courseKey):
    GoogleOAuthService.GoogleOAuthService().InsertStudentInfo(token,courseKey)