import Repository.BaseRepository as repo
from Model.UserAccount import UserAccount

class AccountService:
    def __init__(self) -> None:
        self.repo = repo.BaseRepository(UserAccount)

    def Register(self, username, password):
        # input: username, password
        # output: baserepo create
        instance = UserAccount(username, password)
        self.repo.Create(instance)

    def Login(self, username, password):
        # input: username, password
        # send username to baserepo read
        # it returns the correct password
        # this function checks it's correct or not
        instance = self.repo.Read(username)
        if instance.password == password:
            return True
        else:
            return False 

    def Logout(self, username):
        # input: username
        # clean the cookie
        pass

    