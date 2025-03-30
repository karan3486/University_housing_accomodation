from __future__ import annotations
from Model.model import *
from marshmallow_sqlalchemy import schema, SQLAlchemyAutoSchema, fields
from marshmallow import Schema, fields, EXCLUDE


class UserSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Users

class ManagerSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Manager

class DepartmentSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Department

class StudentSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Student

class HallOfResidenceSerializer(SQLAlchemyAutoSchema):
    managerid = fields.Integer()
    class Meta:
        model = HallOfResidence
        include_relationships = True
        unknown = EXCLUDE
    manager = fields.Nested(ManagerSerializer)

class AdvisorSerializer(SQLAlchemyAutoSchema):
    deptid = fields.Integer()
    class Meta:
        model = Advisor
        include_relationships = True
        unknown = EXCLUDE
    department = fields.Nested(DepartmentSerializer)

class HouseRequestSerializer(SQLAlchemyAutoSchema):
    studentid = fields.Integer()
    class Meta:
        model = HousingRequest
        include_relationships = True
        unknown = EXCLUDE
    student = fields.Nested(StudentSerializer)

class ApartmentSerializer(SQLAlchemyAutoSchema):
    managerid = fields.Integer()
    class Meta:
        model = Apartment
        include_relationships = True
        unknown = EXCLUDE
    manager = fields.Nested(ManagerSerializer)

class StaffSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Staff

class RoomSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Room

class ComplainSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Complains
        include_relationships = True
        unknown = EXCLUDE
    staff = fields.Nested(StaffSerializer)
    student = fields.Nested(StudentSerializer)

class HallLinkRoomSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = HallLinkedRoom
        include_relationships = True
        unknown = EXCLUDE
    hall = fields.Nested(HallOfResidenceSerializer)
    room = fields.Nested(RoomSerializer)

class StudentRoomSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = StudentRoom
        include_relationships = True
        unknown = EXCLUDE
    student = fields.Nested(StudentSerializer)
    room = fields.Nested(RoomSerializer)

class InvoiceSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice
        include_relationships = True
        unknown = EXCLUDE
    student = fields.Nested(StudentSerializer)
    room = fields.Nested(RoomSerializer)