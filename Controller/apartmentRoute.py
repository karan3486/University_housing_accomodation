from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
apartment_bp = Blueprint('apartment', __name__)
from Service.apartmentService import ApartmentServices
from Utilities.utilities import Hall_RESIDENCE_TYPE
import json

@apartment_bp.route('/apartments', methods=['GET'])
@cross_origin()
@login_required
def ApartmentsPage():
    return render_template("apartment/apartmentListPartial.html",userid = session['userid'])

    
@apartment_bp.route('/apartmentdetail/<int:apartment_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(apartment_id):
    apartmentDetail = ApartmentServices().get_apartment_detail(apartment_id)
    response = jsonify(render_template("apartment/apartmentDetailPartial.html",data= apartmentDetail,residencetype = Hall_RESIDENCE_TYPE))
    return response

@cross_origin()
@login_required
@apartment_bp.route('/delete-apartment/<int:apartment_id>',methods=['DELETE'])
def DeleteApartmentId(apartment_id):
    isdelete = ApartmentServices().delete_apartment(apartment_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(apartment_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(apartment_id)+'. Please Try Again.'})
    

@apartment_bp.route('/get_apartment_list', methods=['GET'])
@cross_origin()
@login_required
def OngetApartmentList():
    apartmentlist = ApartmentServices().get_all_apartmentList()
    response = jsonify({'data': apartmentlist})
    return response

@apartment_bp.route('/save_apartment', methods=['POST'])
@cross_origin()
@login_required
def SaveApartmentResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('appartmentid',None):
        apartmentlist = ApartmentServices().updateApartment(data)
    else:
        data['appartmentid'] = 0
        apartmentlist = ApartmentServices().create(data)
        
    if apartmentlist:
       id = apartmentlist.get('apartmentlid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response

