from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from Repository.userRepository import UserRepository
from Repository.studentRepository import StudentRepository
from DBConnection.dbconnection import db
from Utilities.utilities import ResponseMessage

class UserService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.student_repository = StudentRepository()


    def user_registration(self,userid: str,usertype: int, password: str)->ResponseMessage:
        return self.user_repository.register_user(userid, usertype, password)

    def user_authenticate(self,userid: int, password: str):
        try:
            return self.user_repository.authenticate_user(userid, password)
        except Exception as e:
            print("Error in authentication : ",e)
            return None
        
    def check_student(self,id):
        return self.student_repository.get_by_id(id)


