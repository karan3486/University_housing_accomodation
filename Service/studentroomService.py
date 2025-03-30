from Model.model import StudentRoom
from Repository.studentroomRepository import studentroomRepository
from Serializer.serializer import  RoomSerializer, StudentRoomSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class StudentRoomServices:
    def __init__(self) -> None:
        self.studentroom_repository = studentroomRepository()
        self.logger = get_logger()

    def create(self, studentroom):
        try:
            deserializedData = StudentRoomSerializer().load(studentroom)
            studentroomModel = StudentRoom(**deserializedData)
            id = self.studentroom_repository.get_max_id()
            studentroomModel.id = id
            new_studentroom=self.studentroom_repository.save(studentroomModel)
            if new_studentroom:
                deserializedData['studentroomid'] = id
                return StudentRoomSerializer().dump(deserializedData)
            else:
                return new_studentroom
        except Exception as e:
            self.logger.error("Error while creating a new StudentRoom : {}".format(e))
            return False
        
    def updateStudentRoom(self,studentroom):
        try:
            deserializedData = StudentRoomSerializer().load(studentroom)
            studentroomnewModel = StudentRoom(**deserializedData)
            studentroomoldModel = self.studentroom_repository.get_by_id(studentroomnewModel.id)
            new_studentroom=self.studentroom_repository.update(studentroomoldModel,studentroomnewModel)
            if new_studentroom:
                return StudentRoomSerializer().dump(deserializedData)
            else:
                return new_studentroom
        except Exception as e:
            self.logger.error("Error while creating a new studentroom : {}".format(e))
            return False

    def get_studentroom_detail(self,id:int):
        try:
            studentroomDetail = self.studentroom_repository.get_by_id(id)
            studentroomDetail = StudentRoomSerializer().dump(studentroomDetail)
            return studentroomDetail
        except Exception as e:
            self.logger.info("Error while getting all studentrooms : ",e)

    def delete_studentroom(self,id:int):
        try:
            isdelete = self.studentroom_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all studentrooms : ",e)

    def get_all_studentroomList(self):
        try:
            studentroomlistdata =  self.studentroom_repository.get_all()
            studentroomlist = [StudentRoomSerializer().dump(data) for data in studentroomlistdata]
            return studentroomlist
        except Exception as e:
            self.logger.info("Error while getting all studentrooms : ",e)
    
    def get_all_roomList(self):
        try:
            studentroomlistdata =  self.studentroom_repository.get_all_roomlist()
            studentroomlist = [RoomSerializer().dump(data) for data in studentroomlistdata]
            return studentroomlist
        except Exception as e:
            self.logger.info("Error while getting all studentrooms : ",e)