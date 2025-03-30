from Model.model import HousingRequest
from Repository.houserequestRepository import HouseRequestRepository
from Serializer.serializer import  HouseRequestSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class HousingRequestServices:
    def __init__(self) -> None:
        self.houseReq_repository = HouseRequestRepository()
        self.logger = get_logger()

    def create(self, houseReq):
        try:
            deserializedData = HouseRequestSerializer().load(houseReq)
            houseReqModel = HousingRequest(**deserializedData)
            id = self.houseReq_repository.get_max_id()
            houseReqModel.requestid = id
            new_houseReq=self.houseReq_repository.save(houseReqModel)
            if new_houseReq:
                deserializedData['houseReqid'] = id
                return HouseRequestSerializer().dump(deserializedData)
            else:
                return new_houseReq
        except Exception as e:
            self.logger.error("Error while creating a new Advisor : {}".format(e))
            return False
        
    def updatehouseReq(self,houseReq):
        try:
            deserializedData = HouseRequestSerializer().load(houseReq)
            houseReqnewModel = HousingRequest(**deserializedData)
            houseReqoldModel = self.houseReq_repository.get_by_id(houseReqnewModel.requestid)
            new_houseReq=self.houseReq_repository.update(houseReqoldModel,houseReqnewModel)
            if new_houseReq:
                return HouseRequestSerializer().dump(deserializedData)
            else:
                return new_houseReq
        except Exception as e:
            self.logger.error("Error while creating a new houseReq : {}".format(e))
            return False

    def get_houseReq_detail(self,id:int):
        try:
            houseReqDetail = self.houseReq_repository.get_by_id(id)
            houseReqDetail = HouseRequestSerializer().dump(houseReqDetail)
            return houseReqDetail
        except Exception as e:
            self.logger.info("Error while getting all houseReqs : ",e)

    def delete_houseReq(self,id:int):
        try:
            isdelete = self.houseReq_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all houseReqs : ",e)

    def approve_houseReq(self,id:int,command: str):
        try:
            isApproved = self.houseReq_repository.approve(id,command)
            return isApproved
        except Exception as e:
            self.logger.info("Error while getting all houseReqs : ",e)

    def get_all_houseReqList(self):
        try:
            houseReqlistdata =  self.houseReq_repository.get_all()
            houseReqlist = [HouseRequestSerializer().dump(data) for data in houseReqlistdata]
            return houseReqlist
        except Exception as e:
            self.logger.info("Error while getting all houseReqs : ",e)