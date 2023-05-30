import Repository.BaseRepository as repo
from Model.CoursekeyVerify import CoursekeyVerify
from Model.StudentCheckIn import StudentCheckIn
import random
import string
from datetime import datetime

class RollcallService:
    def __init__(self) -> None:
        pass
    def StartRollcall(self,info:CoursekeyVerify):
        # return CourseKey
        # generate courseKey, startTime, duration
        
        courseKey = info.Coursekey + '_' + ''.join(random.SystemRandom().choice(string.digits) for _ in range(6))
        startTime = datetime.now()
        d = {'Coursekey':courseKey,'Owner':info.Owner,'StartTime':info.StartTime,'EndTime':info.EndTime}
        instance = CoursekeyVerify(**d)
        repo.BaseRepository(CoursekeyVerify).Create(instance)
        return courseKey
    def GetStudentList(self,courseKey:str):
        d = {'Coursekey':courseKey}
        ret:list[StudentCheckIn] = repo.BaseRepository(StudentCheckIn).Read(StudentCheckIn(**d))
        time:CoursekeyVerify = repo.BaseRepository(CoursekeyVerify).Read(CoursekeyVerify(**d))
        ans = []
        if len(time) == 0:
            return ans
        for data in ret:
            if int(data.CheckinTime) >= int(time[0].StartTime) and int(data.CheckinTime) <= int(time[0].EndTime):
                ans.append(data)
        return ans
        
        
    