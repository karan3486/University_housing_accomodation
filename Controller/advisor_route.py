from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
advisor_bp = Blueprint('advisor', __name__)
from Service.advisorService import AdvisorServices

@advisor_bp.route('/advisors', methods=['GET'])
@cross_origin()
@login_required
def AdvisorsPage():
    return render_template("advisor/advisorsListPartial.html",userid = session['userid'])

    
@advisor_bp.route('/advisordetail/<int:advisor_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(advisor_id):
    advisorDetail = AdvisorServices().get_advisor_detail(advisor_id)
    response = jsonify(render_template("advisor/advisorDetailPartial.html",advisor = advisorDetail))
    return response

@cross_origin()
@login_required
@advisor_bp.route('/delete-advisor/<int:advisor_id>',methods=['DELETE'])
def DeleteAdvisorId(advisor_id):
    isdelete = AdvisorServices().delete_advisor(advisor_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(advisor_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(advisor_id)+'. Please Try Again.'})
    

@advisor_bp.route('/get_advisor_list', methods=['GET'])
@cross_origin()
@login_required
def OngetAdvisorList():
    advisorlist = AdvisorServices().get_all_advisorList()
    response = jsonify({'data': advisorlist})
    return response

@advisor_bp.route('/save_advisor', methods=['POST'])
@cross_origin()
@login_required
def SaveAdvisorResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('advisorid',None):
        advisorlist = AdvisorServices().updateAdvisor(data)
    else:
        data['advisorid'] = 0
        advisorlist = AdvisorServices().create(data)
        
    if advisorlist:
       id = advisorlist.get('advisorlid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response


# @advisor_bp.route('/advisors', methods=['GET'])
# @cross_origin()
# @login_required
# def AdvisorsPage():
#     response = jsonify(render_template("advisor/advisorsListPartial.html"))
#     # response.headers["Content-Type"] = "application/json"
#     # return render_template("advisors.html")
#     return render_template("advisor/advisorsListPartial.html",userid = session['userid'])

# @advisor_bp.route('/advisorsdetail', methods=['GET'])
# @cross_origin()
# @login_required
# def AdvisorDetailPage():
#     response = jsonify(render_template("advisor/advisorDetailPartial.html"))
#     # response.headers["Content-Type"] = "application/json"
#     # return render_template("advisors.html")
#     return response
