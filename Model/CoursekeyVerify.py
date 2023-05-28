class CoursekeyVerify:
    def __init__(self,courseKey=None,startTime=None,endTime=None,owner=None) -> None:
        self.CourseKey: str = courseKey
        self.StartTime: str = startTime
        self.EndTime: str = endTime
        self.Owner: str = owner
