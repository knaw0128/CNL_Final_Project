import Repository.BaseRepository as repo
from Model.CoursekeyVerify import CoursekeyVerify
from Model.StudentCheckin import StudentCheckin
import random
import string
from datetime import datetime

class Rollcall:
    def __init__(self) -> None:
        self.repo =  repo.BaseRepository(CoursekeyVerify)
    def StartRollcall(self,duration,owner):
        # return CourseKey
        # generate courseKey, startTime, duration
        courseKey = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
        startTime = datetime.timestamp(datetime.now())
        instance = CoursekeyVerify(courseKey,str(startTime),str(startTime+duration),owner)
        self.repo.Create(instance)
        return courseKey
    def GetStudentList(self,courseKey:str):
        ret:list[StudentCheckin] = repo.BaseRepository(StudentCheckin).Read(courseKey)
        return ret
        
        
    