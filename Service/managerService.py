from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from Repository.managerRepository import ManagerRepository
from DBConnection.dbconnection import db
from Model.model import Manager
from Serializer.serializer import ManagerSerializer
from Logger.logger import get_logger

class ManagerService:
    def __init__(self) -> None:
        self.manager_repository = ManagerRepository()
        self.logger = get_logger()

    def create(self, manager):
        try:
            deserializedData = ManagerSerializer().load(manager)
            managerModel = Manager(**deserializedData)
            id = self.manager_repository.get_max_id()
            managerModel.managerid = id
            new_manager=self.manager_repository.save(managerModel)
            if new_manager:
                deserializedData['managerid'] = id
                return ManagerSerializer().dump(deserializedData)
            else:
                return new_manager
        except Exception as e:
            self.logger.error("Error while creating a new Manager : {}".format(e))
            return False    
        
    def updateManager(self,manager):
        try:
            deserializedData = ManagerSerializer().load(manager)
            managernewModel = Manager(**deserializedData)
            manageroldModel = self.manager_repository.get_by_id(managernewModel.managerid)
            new_manager=self.manager_repository.update(manageroldModel,managernewModel)
            if new_manager:
                return ManagerSerializer().dump(deserializedData)
            else:
                return new_manager
        except Exception as e:
            self.logger.error("Error while creating a new manager : {}".format(e))
            return False
    def delete_manager(self,id:int):
        try:
            isdelete = self.manager_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all managers : ",e)

    def get_manager_detail(self,id:int):
        try:
            managerDetail = self.manager_repository.get_by_id(id)
            managerDetail = ManagerSerializer().dump(managerDetail)
            return managerDetail
        except Exception as e:
            self.logger.info("Error while getting all halls : ",e)

    def get_all_managerList(self):
        try:
            managerlistdata = self.manager_repository.get_all()
            managerList = [ManagerSerializer().dump(data) for data in managerlistdata]
            return managerList
        except Exception as e:
            self.logger.info("Error while getting all halls : ",e)


