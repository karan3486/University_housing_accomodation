from Model.model import Complains
from Repository.complainRepository import ComplainRepository
from Serializer.serializer import  ComplainSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class ComplainServices:
    def __init__(self) -> None:
        self.complain_repository = ComplainRepository()
        self.logger = get_logger()

    def create(self, complain):
        try:
            deserializedData = ComplainSerializer().load(complain)
            complainModel = Complains(**deserializedData)
            id = self.complain_repository.get_max_id()
            complainModel.complainid = id
            new_complain=self.complain_repository.save(complainModel)
            if new_complain:
                deserializedData['complainid'] = id
                return ComplainSerializer().dump(deserializedData)
            else:
                return new_complain
        except Exception as e:
            self.logger.error("Error while creating a new Complain : {}".format(e))
            return False
        
    def updateComplain(self,complain):
        try:
            deserializedData = ComplainSerializer().load(complain)
            complainnewModel = Complains(**deserializedData)
            complainoldModel = self.complain_repository.get_by_id(complainnewModel.complainid)
            new_complain=self.complain_repository.update(complainoldModel,complainnewModel)
            if new_complain:
                return ComplainSerializer().dump(deserializedData)
            else:
                return new_complain
        except Exception as e:
            self.logger.error("Error while creating a new complain : {}".format(e))
            return False

    def get_complain_detail(self,id:int):
        try:
            complainDetail = self.complain_repository.get_by_id(id)
            complainDetail = ComplainSerializer().dump(complainDetail)
            return complainDetail
        except Exception as e:
            self.logger.info("Error while getting all complains : ",e)

    def delete_complain(self,id:int):
        try:
            isdelete = self.complain_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all complains : ",e)

    def get_all_complainList(self):
        try:
            complainlistdata =  self.complain_repository.get_all()
            complainlist = [ComplainSerializer().dump(data) for data in complainlistdata]
            return complainlist
        except Exception as e:
            self.logger.info("Error while getting all complains : ",e)