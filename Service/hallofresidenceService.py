from Model.model import HallOfResidence
from Repository.hallofresidenceRepository import HallOfResidenceRepository
from Serializer.serializer import  HallOfResidenceSerializer, HallLinkRoomSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class HallOfResidenceService:
    def __init__(self) -> None:
        self.hall_repository = HallOfResidenceRepository()
        self.logger = get_logger()

    def create(self, hall):
        try:
            deserializedData = HallOfResidenceSerializer().load(hall)
            hallModel = HallOfResidence(**deserializedData)
            id = self.hall_repository.get_max_id()
            hallModel.hallid = id
            new_hall=self.hall_repository.save(hallModel)
            if new_hall:
                deserializedData['hallid'] = id
                return HallOfResidenceSerializer().dump(deserializedData)
            else:
                return new_hall
        except Exception as e:
            self.logger.error("Error while creating a new hall of residence : {}".format(e))
            return False
        
    def updateHall(self,hall):
        try:
            deserializedData = HallOfResidenceSerializer().load(hall)
            hallnewModel = HallOfResidence(**deserializedData)
            halloldModel = self.hall_repository.get_by_id(hallnewModel.hallid)
            new_hall=self.hall_repository.update(halloldModel,hallnewModel)
            if new_hall:
                return HallOfResidenceSerializer().dump(deserializedData)
            else:
                return new_hall
        except Exception as e:
            self.logger.error("Error while creating a new hall of residence : {}".format(e))
            return False

    def get_hall_detail(self,id:int):
        try:
            hallDetail = self.hall_repository.get_by_id(id)
            hallDetail = HallOfResidenceSerializer().dump(hallDetail)
            return hallDetail
        except Exception as e:
            self.logger.info("Error while getting all halls : ",e)

    def delete_hall(self,id:int):
        try:
            isdelete = self.hall_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all halls : ",e)

    def get_all_hallList(self):
        try:
            halllistdata =   self.hall_repository.get_all()
            halllist = [HallOfResidenceSerializer().dump(data) for data in halllistdata]
            return halllist
        except Exception as e:
            self.logger.info("Error while getting all halls : ",e)

    def get_all_rooms(self,hallId:int):
        try:
            roomlistdata =  self.hall_repository.get_linked_rooms(hallId)
            roomlist = [HallLinkRoomSerializer().dump(data) for data in roomlistdata]
            return roomlist
        except Exception as e:
            self.logger.info("Error while getting all halls : ",e)