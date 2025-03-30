from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
manager_bp = Blueprint('manager', __name__)
from Service.managerService import ManagerService

@manager_bp.route('/managers', methods=['GET'])
@cross_origin()
@login_required
def ManagersPage():
    return render_template("manager/managersListPartial.html",userid = session['userid'])

    
@manager_bp.route('/managerdetail/<int:manager_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(manager_id):
    try:
        managerDetail = ManagerService().get_manager_detail(manager_id)
        response = jsonify(render_template("manager/managerDetailPartial.html",data = managerDetail,residencetype=['Residence','Commercial']))
        return response
    except Exception as e:
        return jsonify('Error')

@cross_origin()
@login_required
@manager_bp.route('/delete-manager/<int:manager_id>',methods=['DELETE'])
def DeleteManagerId(manager_id):
    isdelete = ManagerService().delete_manager(manager_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(manager_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(manager_id)+'. Please Try Again.'})
    

@manager_bp.route('/get_manager_list', methods=['GET'])
@cross_origin()
@login_required
def OngetManagerList():
    managerlist = ManagerService().get_all_managerList()
    response = jsonify({'data': managerlist})
    return response

@manager_bp.route('/save_manager', methods=['POST'])
@cross_origin()
@login_required
def SaveManagerResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('managerid',None):
        managerlist = ManagerService().updateManager(data)
    else:
        data['managerid'] = 0
        managerlist = ManagerService().create(data)
        
    if managerlist:
       id = managerlist.get('managerid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response


