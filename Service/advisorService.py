from Model.model import Advisor
from Repository.advisorRepository import AdvisorRepository
from Serializer.serializer import  AdvisorSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class AdvisorServices:
    def __init__(self) -> None:
        self.advisor_repository = AdvisorRepository()
        self.logger = get_logger()

    def create(self, advisor):
        try:
            deserializedData = AdvisorSerializer().load(advisor)
            advisorModel = Advisor(**deserializedData)
            id = self.advisor_repository.get_max_id()
            advisorModel.advisorid = id
            new_advisor=self.advisor_repository.save(advisorModel)
            if new_advisor:
                deserializedData['advisorid'] = id
                return AdvisorSerializer().dump(deserializedData)
            else:
                return new_advisor
        except Exception as e:
            self.logger.error("Error while creating a new Advisor : {}".format(e))
            return False
        
    def updateAdvisor(self,advisor):
        try:
            deserializedData = AdvisorSerializer().load(advisor)
            advisornewModel = Advisor(**deserializedData)
            advisoroldModel = self.advisor_repository.get_by_id(advisornewModel.advisorid)
            new_advisor=self.advisor_repository.update(advisoroldModel,advisornewModel)
            if new_advisor:
                return AdvisorSerializer().dump(deserializedData)
            else:
                return new_advisor
        except Exception as e:
            self.logger.error("Error while creating a new advisor : {}".format(e))
            return False

    def get_advisor_detail(self,id:int):
        try:
            advisorDetail = self.advisor_repository.get_by_id(id)
            advisorDetail = AdvisorSerializer().dump(advisorDetail)
            return advisorDetail
        except Exception as e:
            self.logger.info("Error while getting all advisors : ",e)

    def delete_advisor(self,id:int):
        try:
            isdelete = self.advisor_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all advisors : ",e)

    def get_all_advisorList(self):
        try:
            advisorlistdata =  self.advisor_repository.get_all()
            advisorlist = [AdvisorSerializer().dump(data) for data in advisorlistdata]
            return advisorlist
        except Exception as e:
            self.logger.info("Error while getting all advisors : ",e)