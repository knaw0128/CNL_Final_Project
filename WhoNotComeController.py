from fastapi import FastAPI
import Model.CoursekeyVerify, Model.StudentCheckin, Model.UserAccount
import Service.AccountService, Service.GoogleOAuthService, Service.RollcallService

app = FastAPI()

@app.post("/register/")
def PostRegister(account:Model.UserAccount.UserAccount):
    Model.AccountService.AccountService().Register(account)
    

@app.post("/login/")
def PostLogin(account:Model.UserAccount.UserAccount):
    Model.AccountService.AccountService().Login(account)

@app.get("/logout/")
def GetLogout():
    Model.AccountService.AccountService().Logout()

@app.get("/getStudentList/")
def GetRollcall(courseKey:str):
    Service.RollcallService.Rollcall().GetStudentList(courseKey)

@app.post("/rollcall/")
def PostRollcall(info:Model.CoursekeyVerify.CoursekeyVerify):
    Service.RollcallService.Rollcall().StartRollcall(info)


@app.get("/googleoauth/") # Not sure method
def PostGoogleOAuth(state,access_token):
    Service.GoogleOAuthService.GoogleOAuthService().InsertStudentInfo(access_token,state)