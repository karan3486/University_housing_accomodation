from Model.model import Staff
from Repository.staffRepository import StaffRepository
from Serializer.serializer import  StaffSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class StaffServices:
    def __init__(self) -> None:
        self.staff_repository = StaffRepository()
        self.logger = get_logger()

    def create(self, staff):
        try:
            deserializedData = StaffSerializer().load(staff)
            staffModel = Staff(**deserializedData)
            id = self.staff_repository.get_max_id()
            staffModel.staffid = id
            new_staff=self.staff_repository.save(staffModel)
            if new_staff:
                deserializedData['staffid'] = id
                return StaffSerializer().dump(deserializedData)
            else:
                return new_staff
        except Exception as e:
            self.logger.error("Error while creating a new Staff : {}".format(e))
            return False
        
    def updateStaff(self,staff):
        try:
            deserializedData = StaffSerializer().load(staff)
            staffnewModel = Staff(**deserializedData)
            staffoldModel = self.staff_repository.get_by_id(staffnewModel.staffid)
            new_staff=self.staff_repository.update(staffoldModel,staffnewModel)
            if new_staff:
                return StaffSerializer().dump(deserializedData)
            else:
                return new_staff
        except Exception as e:
            self.logger.error("Error while creating a new staff : {}".format(e))
            return False

    def get_staff_detail(self,id:int):
        try:
            staffDetail = self.staff_repository.get_by_id(id)
            staffDetail = StaffSerializer().dump(staffDetail)
            return staffDetail
        except Exception as e:
            self.logger.info("Error while getting all staffs : ",e)

    def delete_staff(self,id:int):
        try:
            isdelete = self.staff_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all staffs : ",e)

    def get_all_staffList(self):
        try:
            stafflistdata =  self.staff_repository.get_all()
            stafflist = [StaffSerializer().dump(data) for data in stafflistdata]
            return stafflist
        except Exception as e:
            self.logger.info("Error while getting all staffs : ",e)