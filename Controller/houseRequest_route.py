from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
from Utilities.utilities import RESIDENCE_TYPE
from send_mail import *
logger = get_logger()
houserequest_bp = Blueprint('houserequest', __name__)
from Service.houserequestService import HousingRequestServices

@houserequest_bp.route('/houserequest', methods=['GET'])
@cross_origin()
@login_required
def HouseRequestsPage():
    return render_template("houserequest/houserequestsListPartial.html",userid = session['userid'])

    
@houserequest_bp.route('/houserequestdetail/<int:houserequest_id>', methods=['GET'])
@cross_origin()
@login_required
def HouseRequestDetailPage(houserequest_id):
    try:
        houserequestDetail = HousingRequestServices().get_houseReq_detail(houserequest_id)
        response = jsonify(render_template("houserequest/houserequestDetailPartial.html",request = houserequestDetail,residencetype = RESIDENCE_TYPE))
        return response
    except Exception as e:
        logger.error(f"Error in getting house request detail : {e}")
        return jsonify({'message': 'Internal Server Error'})

@cross_origin()
@login_required
@houserequest_bp.route('/delete-houserequest/<int:houserequest_id>',methods=['DELETE'])
def DeleteHouseRequestId(houserequest_id):
    isdelete = HousingRequestServices().delete_houseReq(houserequest_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(houserequest_id)})
    else:
        return jsonify({'success': False,'message':'Failed to delete Hall Id: '+ str(houserequest_id)+'. Please Try Again.'})
    
@cross_origin()
@login_required
@houserequest_bp.route('/approve-houserequest/<int:houserequest_id>/<command>',methods=['GET'])
def ApproveHouseRequestId(houserequest_id,command):
    isApproved = HousingRequestServices().approve_houseReq(houserequest_id,command)
    houserequestDetail = HousingRequestServices().get_houseReq_detail(houserequest_id)
    student = houserequestDetail.get('student')
    email = student['email']
    if isApproved:
        subject = 'House Request Approved!'
        html_content = f"""
    <html>
    <body>
        <h3>Dear,{student['fname']}</h3>
        <p>Congratulations!!<p>
        <p>Your House Request has been Approved.<p>
        <p>Please login to your account to view your house request.</p>
        <p>Regards,</p>
        <p>Housing Admin</p>
    </body>
    </html>
    """
        SendEmail.send_email(email, subject, html_content)
        return jsonify({'success':True, 'message':'House Request '+ str(command).capitalize()+'ed for id: '+str(houserequest_id)})
    else:
        subject = 'House Request Rejected!'
        html_content = f"""
    <html>
    <body>
        <h3>Dear, {student['fname']}</h3>
        <p>Unfortunately!!<p>
        <p>Your House Request has been Rejected.<p>
        <p>Please Contact your admin.</p>
        <p>Regards,</p>
        <p>Housing Admin</p>
    </body>
    </html>
    """
        SendEmail.send_email(email, subject, html_content)
        return jsonify({'success': True,'message':'House Request'+ str(command).capitalize()+'ed for Id: '+ str(houserequest_id)+'.'})

@houserequest_bp.route('/get_houserequest_list', methods=['GET'])
@cross_origin()
@login_required
def OngetHouseRequestList():
    houserequestlist = HousingRequestServices().get_all_houseReqList()
    response = jsonify({'data': houserequestlist})
    return response

@houserequest_bp.route('/save_houserequest', methods=['POST'])
@cross_origin()
@login_required
def SaveHouseRequestResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('houserequestid',None):
        houserequestlist = HousingRequestServices().updatehouseReq(data)
    else:
        data['houserequestid'] = 0
        houserequestlist = HousingRequestServices().create(data)
        
    if houserequestlist:
       id = houserequestlist.get('requestid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response

