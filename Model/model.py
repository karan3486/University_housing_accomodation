from sqlite3 import Date
from typing import Optional
from DBConnection.dbconnection import db
from flask_login import UserMixin


class UserType(db.Model):
    __tablename__ = 'usertype'

    id: int = db.Column(db.Integer, primary_key=True)
    typename: str = db.Column(db.String(20))

    def __init__(self, id: int, typename: str):
        self.id = id
        self.typename = typename

    def __repr__(self) -> str:
        return f"<UserType id={self.id}, typename={self.typename}>"

class Users(UserMixin,db.Model):
    __tablename__ = 'Users'

    id: int = db.Column(db.Integer,db.ForeignKey('usertype.id'), primary_key=True)
    usertypeid: int = db.Column(db.Integer, db.ForeignKey('usertype.id'))
    password = db.Column(db.String(100))

    def __init__(self, id: int, usertypeid: int, password):
        self.id = id
        self.usertypeid = usertypeid
        self.password = password

    def __repr__(self) -> str:
        return f"<Users id={self.id}, usertypeid={self.usertypeid}, password={self.password}>"
    

class Department(db.Model):
    __tablename__ = 'Department'

    deptno = db.Column(db.Integer, primary_key=True)
    deptname = db.Column(db.String(30))

    def __init__(self, deptno: int, deptname: str):
        self.deptno = deptno
        self.deptname = deptname

    def __repr__(self):
        return f"<Department deptno={self.deptno}, deptname={self.deptname}>"
    
class CourseInfo(db.Model):
    __tablename__ = 'CourseInfo'

    courseid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    deptid = db.Column(db.Integer, db.ForeignKey('Department.deptno'))

    department = db.relationship('Department', backref=db.backref('courses', lazy=True))

    def __init__(self, courseid: int, title: str, deptid: int):
        self.courseid = courseid
        self.title = title
        self.deptid = deptid

    def __repr__(self):
        return f"<CourseInfo courseid={self.courseid}, title={self.title}, deptid={self.deptid}>"
    
class Advisor(db.Model):
    __tablename__ = 'Advisor'

    advisorid: int = db.Column(db.Integer, primary_key=True)
    fname: str = db.Column(db.String(10))
    lname: str = db.Column(db.String(10))
    positionOfAdvisor: str = db.Column(db.String(30))
    deptid: int = db.Column(db.Integer, db.ForeignKey('Department.deptno'))
    mobileNumber: Optional[int] = db.Column(db.BigInteger)
    email: str = db.Column(db.String(50))
    roomNo: Optional[int] = db.Column(db.Integer)
    department = db.relationship('Department', backref='advisor')

    def __init__(self, advisorid: int, fname: str, lname: str, positionOfAdvisor: str, deptid: int, 
                 mobileNumber: Optional[int], email: str, roomNo: Optional[int]):
        self.advisorid = advisorid
        self.fname = fname
        self.lname = lname
        self.positionOfAdvisor = positionOfAdvisor
        self.deptid = deptid
        self.mobileNumber = mobileNumber
        self.email = email
        self.roomNo = roomNo

    def __repr__(self) -> str:
        return f"<Advisor advisorid={self.advisorid}, fname={self.fname}, lname={self.lname}, positionOfAdvisor={self.positionOfAdvisor}, deptid={self.deptid}, mobileNumber={self.mobileNumber}, email={self.email}, roomNo={self.roomNo}>"
    

class Student(db.Model):
    __tablename__ = 'Student'

    studentid: int = db.Column(db.Integer, primary_key=True)
    fname: str = db.Column(db.String(10))
    lname: str = db.Column(db.String(10))
    email: str = db.Column(db.String(50))
    trimester: str = db.Column(db.String(20))
    mobile: Optional[int] = db.Column(db.BigInteger)
    addressline: str = db.Column(db.String(100))
    state: str = db.Column(db.String(10))
    city: str = db.Column(db.String(20))
    zipcode: int = db.Column(db.Integer)
    dob: Date = db.Column(db.Date)
    gender: str = db.Column(db.String(10))
    advisorid: Optional[int] = db.Column(db.Integer, db.ForeignKey('Advisor.advisorid'))
    major: str = db.Column(db.String(20))
    minor: str = db.Column(db.String(20))
    nationality: str = db.Column(db.String(10))

    def __init__(self, studentid: int, fname: str, lname: str, mobile: Optional[int], addressline: str,
                 state: str, city: str, zipcode: int, dob: Date, gender: str, advisorid: Optional[int],
                 major: str, minor: str, nationality: str):
        self.studentid = studentid
        self.fname = fname
        self.lname = lname
        self.mobile = mobile
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.dob = dob
        self.gender = gender
        self.advisorid = advisorid
        self.major = major
        self.minor = minor
        self.nationality = nationality

    def __repr__(self) -> str:
        return f"<Student studentid={self.studentid}, fname={self.fname}, lname={self.lname}, mobile={self.mobile}, addressline={self.addressline}, state={self.state}, city={self.city}, zipcode={self.zipcode}, dob={self.dob}, gender={self.gender}, advisorid={self.advisorid}, major={self.major}, minor={self.minor}, nationality={self.nationality}>"
    
class StudentCourseEnrolled(db.Model):
    __tablename__ = 'StudentCourseEnrolled'

    enrollid: int = db.Column(db.Integer, primary_key=True)
    studentid: int = db.Column(db.Integer, db.ForeignKey('Student.studentid'))
    courseid: int = db.Column(db.Integer, db.ForeignKey('CourseInfo.courseid'))

    def __init__(self, enrollid: int, studentid: int, courseid: int):
        self.enrollid = enrollid
        self.studentid = studentid
        self.courseid = courseid

    def __repr__(self) -> str:
        return f"<StudentCourseEnrolled enrollid={self.enrollid}, studentid={self.studentid}, courseid={self.courseid}>"
    
class HousingRequest(db.Model):
    __tablename__ = 'HousingRequest'

    requestid: int = db.Column(db.Integer, primary_key=True)
    studentid: int = db.Column(db.Integer, db.ForeignKey('Student.studentid'))
    currentStatus: str = db.Column(db.Enum('Approved', 'Pending', 'Rejected'))
    residenceType: str = db.Column(db.Enum('Apartment', 'HallOfResidence'))
    dateofRequest: Date = db.Column(db.Date)
    student = db.relationship('Student', backref='Hsousing_request')

    def __init__(self, requestid: int, studentid: int, currentStatus: str, residenceType: str, dateofRequest: Date):
        self.requestid = requestid
        self.studentid = studentid
        self.currentStatus = currentStatus
        self.residenceType = residenceType
        self.dateofRequest = dateofRequest

    def __repr__(self) -> str:
        return f"<HousingRequest requestid={self.requestid}, studentid={self.studentid}, currentStatus={self.currentStatus}, residenceType={self.residenceType}, dateofRequest={self.dateofRequest}>"
    
class Staff(db.Model):
    __tablename__ = 'Staff'

    staffid: int = db.Column(db.Integer, primary_key=True)
    fname: str = db.Column(db.String(10))
    lname: str = db.Column(db.String(10))
    email: str = db.Column(db.String(30))
    mobile: int = db.Column(db.BigInteger)
    gender: str = db.Column(db.String(10))
    addressline: str = db.Column(db.String(100))
    state: str = db.Column(db.String(10))
    city: str = db.Column(db.String(20))
    zipcode: int = db.Column(db.Integer)
    dob: Date = db.Column(db.Date)
    positionOfStaff: str = db.Column(db.Enum('Administrater', 'Manager', 'Housekeeping', 'Security', 'Technician'))

    def __init__(self, staffid: int, fname: str, lname: str, email: str, mobile: int, gender: str, addressline: str,
                 state: str, city: str, zipcode: int, dob: Date, positionOfStaff: str):
        self.staffid = staffid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.mobile = mobile
        self.gender = gender
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.dob = dob
        self.positionOfStaff = positionOfStaff

    def __repr__(self) -> str:
        return f"<Staff staffid={self.staffid}, fname={self.fname}, lname={self.lname}, email={self.email}, mobile={self.mobile}, gender={self.gender}, addressline={self.addressline}, state={self.state}, city={self.city}, zipcode={self.zipcode}, dob={self.dob}, positionOfStaff={self.positionOfStaff}>"
    
class NextOfKin(db.Model):
    __tablename__ = 'NextOfKin'

    studentid: int = db.Column(db.Integer, db.ForeignKey('Student.studentid'), primary_key=True)
    kinid: int = db.Column(db.Integer, primary_key=True)
    fname: str = db.Column(db.String(10))
    lname: str = db.Column(db.String(10))
    relationship: str = db.Column(db.String(15))
    addressline: str = db.Column(db.String(100))
    state: str = db.Column(db.String(10))
    city: str = db.Column(db.String(30))
    zipcode: int = db.Column(db.Integer)
    mobile: int = db.Column(db.BigInteger)

    def __init__(self, studentid: int, kinid: int, fname: str, lname: str, relationship: str, addressline: str,
                 state: str, city: str, zipcode: int, mobile: int):
        self.studentid = studentid
        self.kinid = kinid
        self.fname = fname
        self.lname = lname
        self.relationship = relationship
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.mobile = mobile

    def __repr__(self) -> str:
        return f"<NextOfKin studentid={self.studentid}, kinid={self.kinid}, fname={self.fname}, lname={self.lname}, relationship={self.relationship}, addressline={self.addressline}, state={self.state}, city={self.city}, zipcode={self.zipcode}, mobile={self.mobile}>"
    
class Manager(db.Model):
    __tablename__ = 'Manager'

    managerid: int = db.Column(db.Integer, primary_key=True)
    fname: str = db.Column(db.String(10))
    lname: str = db.Column(db.String(10))
    email: str = db.Column(db.String(50))
    addressline: str = db.Column(db.String(100))
    state: str = db.Column(db.String(10))
    city: str = db.Column(db.String(30))
    zipcode: int = db.Column(db.Integer)
    gender: str = db.Column(db.String(10))
    mobile: int = db.Column(db.BigInteger)
    ManagerType: str = db.Column(db.String(10))

    def __init__(self, managerid: int, fname: str, lname: str, email: str, addressline: str, state: str, city: str,
                 zipcode: int, gender: str, mobile: int, ManagerType: str):
        self.managerid = managerid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.gender = gender
        self.mobile = mobile
        self.ManagerType = ManagerType

    def __repr__(self) -> str:
        return f"<Manager managerid={self.managerid}, fname={self.fname}, lname={self.lname}, email={self.email}, addressline={self.addressline}, state={self.state}, city={self.city}, zipcode={self.zipcode}, gender={self.gender}, mobile={self.mobile}, ManagerType={self.ManagerType}>"
    
class Apartment(db.Model):
    __tablename__ = 'Apartment'

    appartmentid: int = db.Column(db.Integer, primary_key=True)
    capacity: int = db.Column(db.Integer)
    addressline: str = db.Column(db.String(100))
    apartmentname: str = db.Column(db.String(30))
    DormType: str = db.Column(db.String(10))
    telephone: str = db.Column(db.String(30))
    state: str = db.Column(db.String(10))
    city: str = db.Column(db.String(30))
    zipcode: int = db.Column(db.Integer)
    managerid: int = db.Column(db.Integer, db.ForeignKey('Manager.managerid'))

    manager = db.relationship('Manager', backref='apartment')

    def __init__(self, appartmentid: int, numberOfBedroom: int, addressline: str, state: str, city: str, zipcode: int, managerid: int):
        self.appartmentid = appartmentid
        self.numberOfBedroom = numberOfBedroom
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.managerid = managerid

    def __repr__(self) -> str:
        return f"<Apartment appartmentid={self.appartmentid}, numberOfBedroom={self.numberOfBedroom}, addressline={self.addressline}, state={self.state}, city={self.city}, zipcode={self.zipcode}, managerid={self.managerid}>"
    

class HallOfResidence(db.Model):
    __tablename__ = 'HallOfResidence'

    hallid: int = db.Column(db.Integer, primary_key=True)
    hallName: str = db.Column(db.String(20))
    typeOfResidence: str = db.Column(db.String(10))
    addressline: str = db.Column(db.String(100))
    state: str = db.Column(db.String(10))
    city: str = db.Column(db.String(30))
    zipcode: int = db.Column(db.Integer)
    phoneNumber: int = db.Column(db.BigInteger)
    managerid = db.Column(db.Integer, db.ForeignKey('Manager.managerid'))
    manager = db.relationship('Manager', backref='hall_of_residence')

    def __init__(self, hallid: int, hallName: str, typeOfResidence: str, addressline: str, state: str, city: str,
                 zipcode: int, phoneNumber: int, managerid: int):
        self.hallid = hallid
        self.hallName = hallName
        self.typeOfResidence = typeOfResidence
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber
        self.managerid = managerid

    def __repr__(self) -> str:
        return f"<HallOfResidence hallid={self.hallid}, hallName={self.hallName}, typeOfResidence={self.typeOfResidence}, addressline={self.addressline}, state={self.state}, city={self.city}, zipcode={self.zipcode}, phoneNumber={self.phoneNumber}, managerid={self.managerid}>"
    

class Room(db.Model):
    __tablename__ = 'Room'

    placenumber: int = db.Column(db.Integer, primary_key=True)
    roomnumber: int = db.Column(db.Integer)
    residencetype: str = db.Column(db.Enum('Apartment', 'HallOfResidence'))
    monthlyRent: int = db.Column(db.Integer)
    DormType:  str = db.Column(db.Enum('Boys','Girls','Mixed'))

    def __init__(self, placenumber: int, roomnumber: int, residencetype: str, monthlyRent: int,DormType: str):
        self.placenumber = placenumber
        self.roomnumber = roomnumber
        self.residencetype = residencetype
        self.monthlyRent = monthlyRent
        self.DormType = DormType

class Inspection(db.Model):
    __tablename__ = 'Inspection'

    inspectionid: int = db.Column(db.Integer, primary_key=True)
    staffid: int = db.Column(db.Integer, db.ForeignKey('Staff.staffid'))
    fname: str = db.Column(db.String(10))
    lname: str = db.Column(db.String(10))
    dateOfInspection: Date = db.Column(db.Date)

    def __init__(self, inspectionid: int, staffid: int, fname: str, lname: str, dateOfInspection: Date):
        self.inspectionid = inspectionid
        self.staffid = staffid
        self.fname = fname
        self.lname = lname
        self.dateOfInspection = dateOfInspection

    def __repr__(self) -> str:
        return f"<Inspection inspectionid={self.inspectionid}, staffid={self.staffid}, fname={self.fname}, lname={self.lname}, dateOfInspection={self.dateOfInspection}, conditionOfRoom={self.conditionOfRoom}, comments={self.comments}>"
    
class LeaseAgreement(db.Model):
    __tablename__ = 'LeaseAgreement'

    leaseid: int = db.Column(db.Integer, primary_key=True)
    duration: int = db.Column(db.Integer)
    placenumber: int = db.Column(db.Integer, db.ForeignKey('Room.placenumber'))
    roomnumber: int = db.Column(db.Integer)
    addressline: str = db.Column(db.String(100))
    state: str = db.Column(db.String(10))
    city: str = db.Column(db.String(30))
    zipcode: int = db.Column(db.Integer)
    entryDate: Date = db.Column(db.Date)
    exitDate: Date = db.Column(db.Date)

    def __init__(self, leaseid: int, duration: int, placenumber: int, roomnumber: int, addressline: str, state: str,
                 city: str, zipcode: int, entryDate: Date, exitDate:Date):
        self.leaseid = leaseid
        self.duration = duration
        self.placenumber = placenumber
        self.roomnumber = roomnumber
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.entryDate = entryDate
        self.exitDate = exitDate

    def __repr__(self) -> str:
        return f"<LeaseAgreement leaseid={self.leaseid}, duration={self.duration}, placenumber={self.placenumber}, roomnumber={self.roomnumber}, addressline={self.addressline}, state={self.state}, city={self.city}, zipcode={self.zipcode}, entryDate={self.entryDate}, exitDate={self.exitDate}>"
    

class Complains(db.Model):
    __tablename__ = 'Complains'

    complainid = db.Column(db.Integer, primary_key=True)
    studentid = db.Column(db.Integer, db.ForeignKey('Student.studentid'))
    dateofComplain = db.Column(db.Date)
    statusOfCompalin = db.Column(db.Enum('Resolved', 'Pending', 'Inprogress'))
    resolvedbyStaff = db.Column(db.Integer, db.ForeignKey('Staff.staffid'))
    dateofResolved = db.Column(db.Date)
    comments = db.Column(db.String(50))

    # Define relationships
    student = db.relationship('Student', backref=db.backref('complains', lazy=True))
    staff = db.relationship('Staff', backref=db.backref('resolved_complains', lazy=True))

    def __repr__(self):
        return f"<Complain complainid={self.complainid}, status={self.statusOfCompalin}>"
    
class HallLinkedRoom(db.Model):
    __tablename__ = 'Halllinkedroom'

    linkid = db.Column(db.Integer, primary_key=True)
    hallid = db.Column(db.Integer, db.ForeignKey('HallOfResidence.hallid', ondelete='SET NULL'))
    placenumber = db.Column(db.Integer, db.ForeignKey('Room.placenumber'))

    hall = db.relationship('HallOfResidence', backref='linked_rooms')
    room = db.relationship('Room', backref='linked_halls')

class AppartmentLinkedRoom(db.Model):
    __tablename__ = 'Appartmentlinkedroom'

    linkid = db.Column(db.Integer, primary_key=True)
    appartmentid = db.Column(db.Integer, db.ForeignKey('Apartment.appartmentid'))
    placenumber = db.Column(db.Integer, db.ForeignKey('Room.placenumber'))

    apartment = db.relationship('Apartment', backref='linked_rooms')
    room = db.relationship('Room', backref='linked_apartments')

class StudentRoom(db.Model):
    __tablename__ = 'Studentroom'

    id = db.Column(db.Integer, primary_key=True)
    placenumber = db.Column(db.Integer, db.ForeignKey('Room.placenumber'))
    roomnumber = db.Column(db.Integer)
    studentid = db.Column(db.Integer, db.ForeignKey('Student.studentid'))

    student = db.relationship('Student', backref='rooms')
    room = db.relationship('Room', backref='students')

class InspectedRoom(db.Model):
    __tablename__ = 'Inspectedroom'

    inspectedid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inspectionid = db.Column(db.Integer, db.ForeignKey('Inspection.inspectionid'))
    placenumber = db.Column(db.Integer, db.ForeignKey('Room.placenumber'))
    conditionOfRoom: str = db.Column(db.Enum('Good', 'Average', 'Bad'))
    comments: str = db.Column(db.String(90))

    inspection = db.relationship('Inspection', backref='inspected_rooms')
    room = db.relationship('Room', backref='inspections')


class Invoice(db.Model):
    invoiceid = db.Column(db.Integer, primary_key=True)
    studentid = db.Column(db.Integer, db.ForeignKey('Student.studentid'))
    placenumber = db.Column(db.Integer, db.ForeignKey('Room.placenumber'))
    addressline = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    paymentDate = db.Column(db.Date)
    methodOfPayment = db.Column(db.Enum('Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Online'))
    semester = db.Column(db.Enum('Winter', 'Spring', 'Summer'))
    paymentDueDate = db.Column(db.Date)
    totalamount = db.Column(db.Integer)
    student = db.relationship('Student', backref='studentroom')
    room = db.relationship('Room', backref='studentroom')

    def __init__(self, studentid, placenumber, addressline, state, city, zipcode, paymentDate, methodOfPayment, semester, paymentDueDate, totalamount):
        self.studentid = studentid
        self.placenumber = placenumber
        self.addressline = addressline
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.paymentDate = paymentDate
        self.methodOfPayment = methodOfPayment
        self.semester = semester
        self.paymentDueDate = paymentDueDate
        self.totalamount = totalamount






























































































































































































































































































































































