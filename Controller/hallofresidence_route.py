from flask import Blueprint, jsonify, render_template, session, request
from flask_cors import cross_origin
from flask_login import login_required
from Service.hallofresidenceService import HallOfResidenceService
from Service.managerService import ManagerService
from Utilities.utilities import Hall_RESIDENCE_TYPE
import json

hallofresidence_bp = Blueprint('hallofresidence', __name__)
hallResidenceService = HallOfResidenceService()
managerService = ManagerService()

@hallofresidence_bp.route('/halls',methods=['GET'])
@cross_origin()
@login_required
def HallsPage():
    try:
        return render_template("hallresidence/hallListPartial.html",userid = session['userid'])
    except Exception as e:
        return jsonify('Error')

    
@hallofresidence_bp.route('/halldetail/<int:hall_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(hall_id):
    hallDetail = hallResidenceService.get_hall_detail(hall_id)
    # response = jsonify({'data': halllist})
    managerList = managerService.get_all_managerList()
    response = jsonify(render_template("hallresidence/hallDetailPartial.html", data=hallDetail,managers = managerList,residencetype = Hall_RESIDENCE_TYPE))
    return response

@cross_origin()
@login_required
@hallofresidence_bp.route('/delete-halls/<int:hall_id>',methods=['DELETE'])
def DeleteHallId(hall_id):
    isdelete = hallResidenceService.delete_hall(hall_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(hall_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(hall_id)+'. Please Try Again.'})
    

@hallofresidence_bp.route('/get_hall_list', methods=['GET'])
@cross_origin()
@login_required
def OngetHallResidenceList():
    halllist = hallResidenceService.get_all_hallList()
    response = jsonify({'data': halllist})
    return response

@hallofresidence_bp.route('/save_hall', methods=['POST'])
@cross_origin()
@login_required
def SaveHallResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('hallid',None):
        halllist = hallResidenceService.updateHall(data)
    else:
        data['hallid'] = 0
        halllist = hallResidenceService.create(data)
        
    if halllist:
       id = halllist.get('hallid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response

@hallofresidence_bp.route('/get-rooms/<int:hall_id>', methods=['GET'])
@cross_origin()
@login_required
def OngetHallRoomList(hall_id):
    hallroomlist = hallResidenceService.get_all_rooms(hall_id)
    response = jsonify({'data': hallroomlist})
    return response



