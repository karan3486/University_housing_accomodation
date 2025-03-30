import logging
from enum import Enum

class ExcludeWerkzeugStaticRequests(logging.Filter):
    def filter(self, record):
        return not ("GET /static/" in record.getMessage() and record.levelname == 'INFO')
    
class Action(Enum):
    SAVE = 1
    DELETE = 2
    UPDATE = 3
    SEND = 4
    NEW = 5
class ResponseMessage:
    def __init__(self) -> None:
        self.Success = True
        self.Message = ''
        self.ActionType = Action.SAVE

# class RESIDENCE_TYPE:
#     Mixed_Dorm = 'Mixed Dorm'
#     Girls_Dorm = 'Girls Dorm'
#     Boys_Dorm = 'Boys Dorm'


Hall_RESIDENCE_TYPE = ['Mixed','Girls','Boys']
RESIDENCE_TYPE = ['Apartment','HallOfResidence']