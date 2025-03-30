from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
complain_bp = Blueprint('complain', __name__)
from Service.complainService import ComplainServices

@complain_bp.route('/complains', methods=['GET'])
@cross_origin()
@login_required
def ComplainsPage():
    return render_template("complain/complainListPartial.html",userid = session['userid'])

    
@complain_bp.route('/complaindetail/<int:complain_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(complain_id):
    complainDetail = ComplainServices().get_complain_detail(complain_id)
    response = jsonify(render_template("complain/complainDetailPartial.html",request=complainDetail))
    return response

@cross_origin()
@login_required
@complain_bp.route('/delete-complain/<int:complain_id>',methods=['DELETE'])
def DeleteComplainId(complain_id):
    isdelete = ComplainServices().delete_complain(complain_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(complain_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(complain_id)+'. Please Try Again.'})
    

@complain_bp.route('/get_complain_list', methods=['GET'])
@cross_origin()
@login_required
def OngetComplainList():
    complainlist = ComplainServices().get_all_complainList()
    response = jsonify({'data': complainlist})
    return response

@complain_bp.route('/save_complain', methods=['POST'])
@cross_origin()
@login_required
def SaveComplainResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('complainid',None):
        complainlist = ComplainServices().updateComplain(data)
    else:
        data['complainid'] = 0
        complainlist = ComplainServices().create(data)
        
    if complainlist:
       id = complainlist.get('complainlid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response

