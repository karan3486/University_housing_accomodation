from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
student_bp = Blueprint('student', __name__)
from Service.studentService import StudentServices

@student_bp.route('/students', methods=['GET'])
@cross_origin()
@login_required
def StudentsPage():
    return render_template("student/studentsListPartial.html",userid = session['userid'])

    
@student_bp.route('/studentdetail/<int:student_id>', methods=['GET'])
@cross_origin()
@login_required
def StudentDetailPage(student_id):
    studentDetail = StudentServices().get_Student_detail(student_id)
    response = jsonify(render_template("student/studentDetailPartial.html"))
    return response

@cross_origin()
@login_required
@student_bp.route('/delete-student/<int:student_id>',methods=['DELETE'])
def DeleteStudentId(student_id):
    isdelete = StudentServices().delete_Student(student_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(student_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(student_id)+'. Please Try Again.'})
    

@student_bp.route('/get_student_list', methods=['GET'])
@cross_origin()
@login_required
def OngetStudentList():
    studentlist = StudentServices().get_all_StudentList()
    response = jsonify({'data': studentlist})
    return response

@student_bp.route('/save_student', methods=['POST'])
@cross_origin()
@login_required
def SaveStudentResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('studentid',None):
        studentlist = StudentServices().updateStudent(data)
    else:
        data['studentid'] = 0
        studentlist = StudentServices().create(data)
        
    if studentlist:
       id = studentlist.get('studentlid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response
