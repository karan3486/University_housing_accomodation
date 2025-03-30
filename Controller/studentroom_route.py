from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
studentroom_bp = Blueprint('studentroom', __name__)
from Service.studentroomService import StudentRoomServices

@studentroom_bp.route('/studentrooms', methods=['GET'])
@cross_origin()
@login_required
def StudentroomsPage():
    return render_template("studentroom/studentroomListPartial.html",userid = session['userid'])

    
@studentroom_bp.route('/studentroomdetail/<int:studentroom_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(studentroom_id):
    studentroomDetail = StudentRoomServices().get_studentroom_detail(studentroom_id)
    response = jsonify(render_template("studentroom/studentroomDetailPartial.html"))
    return response

@cross_origin()
@login_required
@studentroom_bp.route('/delete-studentroom/<int:studentroom_id>',methods=['DELETE'])
def DeleteStudentroomId(studentroom_id):
    isdelete = StudentRoomServices().delete_studentroom(studentroom_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(studentroom_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(studentroom_id)+'. Please Try Again.'})
    

@studentroom_bp.route('/get_studentroom_list', methods=['GET'])
@cross_origin()
@login_required
def OngetStudentroomList():
    studentroomlist = StudentRoomServices().get_all_studentroomList()
    response = jsonify({'data': studentroomlist})
    return response

@studentroom_bp.route('/save_studentroom', methods=['POST'])
@cross_origin()
@login_required
def SaveStudentroomResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('studentroomid',None):
        studentroomlist = StudentRoomServices().updateStudentRoom(data)
    else:
        data['id'] = 0
        studentroomlist = StudentRoomServices().create(data)
        
    if studentroomlist:
       id = studentroomlist.get('studentroomlid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response

