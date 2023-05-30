import Repository.BaseRepository as repo
from Model.CoursekeyVerify import CoursekeyVerify
from Model.StudentCheckin import StudentCheckin
import random
import string
from datetime import datetime

class Rollcall:
    def __init__(self) -> None:
        pass
    def StartRollcall(self,info:CoursekeyVerify):
        # return CourseKey
        # generate courseKey, startTime, duration
        
        courseKey = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
        startTime = datetime.now()
        d = {'Coursekey':courseKey,'Owner':info.Owner,'StartTime':startTime,'EndTime':info.EndTime}
        instance = CoursekeyVerify(**d)
        repo.BaseRepository(CoursekeyVerify()).Create(instance)
        return courseKey
    def GetStudentList(self,courseKey:str):
        d = {'CourseKey':courseKey}
        ret:list[StudentCheckin] = repo.BaseRepository(StudentCheckin).Read(StudentCheckin(**d))
        return ret
        
        
    