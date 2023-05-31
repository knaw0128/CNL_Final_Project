import os

from authlib.integrations.starlette_client import OAuth
from authlib.integrations.starlette_client import OAuthError
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

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID') or None
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or None
if GOOGLE_CLIENT_ID is None or GOOGLE_CLIENT_SECRET is None:
    raise BaseException('Missing env variables')

# Set up OAuth
config_data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
starlette_config = Config(environ=config_data)
oauth = OAuth(starlette_config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

# Set up the middleware to read the request session
SECRET_KEY = os.environ.get('SECRET_KEY') or None
if SECRET_KEY is None:
    raise 'Missing SECRET_KEY'
auth_app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Frontend URL:
FRONTEND_URL = os.environ.get('FRONTEND_URL') or 'http://127.0.0.1:7000/token'

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


# @app.get("/googleoauth/") # Not sure method
# async def PostGoogleOAuth(state,access_token):
#     GoogleOAuthService().InsertStudentInfo(access_token,state)

@app.route('/googleauth')
async def PostGoogleOAuth(request: Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        return RedirectResponse(url='/')
    user_data = await oauth.google.parse_id_token(request, access_token)
    print(user_data)
    request.session['user'] = dict(user_data)
    return RedirectResponse(url='/')