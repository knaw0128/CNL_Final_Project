from fastapi import FastAPI
from Model import *
from Service import *

app = FastAPI()

@app.post("/register")
def PostRegister():
    raise NotImplementedError

@app.post("/login/{account}/{password}")
def PostLogin():
    raise NotImplementedError

@app.get("/logout")
def GetLogout():
    raise NotImplementedError

@app.get("/rollcall/{courseKey}")
def GetRollcall(courseKey:str):
    RollcallService.Rollcall().GetStudentList(courseKey)

@app.post("/rollcall/{owner}/{duration}")
def PostRollcall(owner:str,duration:float):
    RollcallService.Rollcall().StartRollcall(duration,owner)


@app.post("/googleoauth") # Not sure method
def PostGoogleOAuth():
    raise NotImplementedError