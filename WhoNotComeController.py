from fastapi import FastAPI, Response
import Model.CoursekeyVerify as CoursekeyVerify
import Model.StudentCheckin as StudentCheckin
import Model.UserAccount as UserAccount
import Service.AccountService as AccountService
import Service.GoogleOAuthService as GoogleOAuthService
import Service.JWTService as JWTService
import Service.RollcallService as RollcallService

app = FastAPI()

@app.post("/register/")
def PostRegister(account:UserAccount.UserAccount):
    AccountService.AccountService().Register(account)
    

@app.post("/login/")
def PostLogin(response: Response, account:UserAccount.UserAccount):
    if AccountService.AccountService().Login(account):
        token = JWTService.JWTService().encode(account.ID)
        response.set_cookie("誰在review我的扣?", token)
    else:
        # TODO: return an error
        pass

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