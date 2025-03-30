from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
staff_bp = Blueprint('staff', __name__)
from Service.staffService import StaffServices

@staff_bp.route('/staffs', methods=['GET'])
@cross_origin()
@login_required
def StaffsPage():
    return render_template("staff/staffListPartial.html",userid = session['userid'])

    
@staff_bp.route('/staffdetail/<int:staff_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(staff_id):
    staffDetail = StaffServices().get_staff_detail(staff_id)
    response = jsonify(render_template("staff/staffDetailPartial.html",staff = staffDetail))
    return response

@cross_origin()
@login_required
@staff_bp.route('/delete-staff/<int:staff_id>',methods=['DELETE'])
def DeleteStaffId(staff_id):
    isdelete = StaffServices().delete_staff(staff_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(staff_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(staff_id)+'. Please Try Again.'})
    

@staff_bp.route('/get_staff_list', methods=['GET'])
@cross_origin()
@login_required
def OngetStaffList():
    stafflist = StaffServices().get_all_staffList()
    response = jsonify({'data': stafflist})
    return response

@staff_bp.route('/save_staff', methods=['POST'])
@cross_origin()
@login_required
def SaveStaffResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('staffid',None):
        stafflist = StaffServices().updateStaff(data)
    else:
        data['staffid'] = 0
        stafflist = StaffServices().create(data)
        
    if stafflist:
       id = stafflist.get('stafflid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response


# @staff_bp.route('/staffs', methods=['GET'])
# @cross_origin()
# @login_required
# def StaffsPage():
#     response = jsonify(render_template("staff/staffsListPartial.html"))
#     # response.headers["Content-Type"] = "application/json"
#     # return render_template("staffs.html")
#     return render_template("staff/staffsListPartial.html",userid = session['userid'])

# @staff_bp.route('/staffsdetail', methods=['GET'])
# @cross_origin()
# @login_required
# def StaffDetailPage():
#     response = jsonify(render_template("staff/staffDetailPartial.html"))
#     # response.headers["Content-Type"] = "application/json"
#     # return render_template("staffs.html")
#     return response
