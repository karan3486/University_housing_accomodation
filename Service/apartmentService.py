from Model.model import Apartment
from Repository.apartmentRepository import ApartmentRepository
from Serializer.serializer import  ApartmentSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class ApartmentServices:
    def __init__(self) -> None:
        self.apartment_repository = ApartmentRepository()
        self.logger = get_logger()

    def create(self, apartment):
        try:
            deserializedData = ApartmentSerializer().load(apartment)
            apartmentModel = Apartment(**deserializedData)
            id = self.apartment_repository.get_max_id()
            apartmentModel.appartmentid = id
            new_apartment=self.apartment_repository.save(apartmentModel)
            if new_apartment:
                deserializedData['appartmentid'] = id
                return ApartmentSerializer().dump(deserializedData)
            else:
                return new_apartment
        except Exception as e:
            self.logger.error("Error while creating a new Apartment : {}".format(e))
            return False
        
    def updateApartment(self,apartment):
        try:
            deserializedData = ApartmentSerializer().load(apartment)
            apartmentnewModel = Apartment(**deserializedData)
            apartmentoldModel = self.apartment_repository.get_by_id(apartmentnewModel.appartmentid)
            new_apartment=self.apartment_repository.update(apartmentoldModel,apartmentnewModel)
            if new_apartment:
                return ApartmentSerializer().dump(deserializedData)
            else:
                return new_apartment
        except Exception as e:
            self.logger.error("Error while creating a new apartment : {}".format(e))
            return False

    def get_apartment_detail(self,id:int):
        try:
            apartmentDetail = self.apartment_repository.get_by_id(id)
            apartmentDetail = ApartmentSerializer().dump(apartmentDetail)
            return apartmentDetail
        except Exception as e:
            self.logger.info("Error while getting all apartments : ",e)

    def delete_apartment(self,id:int):
        try:
            isdelete = self.apartment_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all apartments : ",e)

    def get_all_apartmentList(self):
        try:
            apartmentlistdata =  self.apartment_repository.get_all()
            apartmentlist = [ApartmentSerializer().dump(data) for data in apartmentlistdata]
            return apartmentlist
        except Exception as e:
            self.logger.info("Error while getting all apartments : ",e)