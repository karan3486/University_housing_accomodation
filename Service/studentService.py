from Model.model import Student
from Repository.studentRepository import StudentRepository
from Serializer.serializer import  StudentSerializer
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE

class StudentServices:
    def __init__(self) -> None:
        self.Student_repository = StudentRepository()
        self.logger = get_logger()

    def create(self, Student):
        try:
            deserializedData = StudentSerializer().load(Student)
            StudentModel = Student(**deserializedData)
            id = self.Student_repository.get_max_id()
            StudentModel.Studentid = id
            new_Student=self.Student_repository.save(StudentModel)
            if new_Student:
                deserializedData['Studentid'] = id
                return StudentSerializer().dump(deserializedData)
            else:
                return new_Student
        except Exception as e:
            self.logger.error("Error while creating a new Student : {}".format(e))
            return False
        
    def updateStudent(self,Student):
        try:
            deserializedData = StudentSerializer().load(Student)
            StudentnewModel = Student(**deserializedData)
            StudentoldModel = self.Student_repository.get_by_id(StudentnewModel.Studentid)
            new_Student=self.Student_repository.update(StudentoldModel,StudentnewModel)
            if new_Student:
                return StudentSerializer().dump(deserializedData)
            else:
                return new_Student
        except Exception as e:
            self.logger.error("Error while creating a new Student : {}".format(e))
            return False

    def get_Student_detail(self,id:int):
        try:
            StudentDetail = self.Student_repository.get_by_id(id)
            StudentDetail = StudentSerializer().dump(StudentDetail)
            return StudentDetail
        except Exception as e:
            self.logger.info("Error while getting all Students : ",e)

    def delete_Student(self,id:int):
        try:
            isdelete = self.Student_repository.delete(id)
            return isdelete
        except Exception as e:
            self.logger.info("Error while getting all Students : ",e)

    def get_all_StudentList(self):
        try:
            Studentlistdata =  self.Student_repository.get_all()
            Studentlist = [StudentSerializer().dump(data) for data in Studentlistdata]
            return Studentlist
        except Exception as e:
            self.logger.info("Error while getting all Students : ",e)