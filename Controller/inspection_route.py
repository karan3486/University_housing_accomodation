from flask import Blueprint, jsonify, render_template, session
from flask_cors import cross_origin
from flask_login import login_required

inspection_bp = Blueprint('inspection', __name__)

@inspection_bp.route('/inspection', methods=['GET'])
@cross_origin()
@login_required
def InspectionsPage():
    response = jsonify(render_template("inspection/inspectionListPartial.html"))
    return render_template("inspection/inspectionListPartial.html",userid = session['userid'])

@inspection_bp.route('/inspectiondetail', methods=['GET'])
@cross_origin()
@login_required
def InspectionsDetailPage():
    response = jsonify(render_template("inspection/inspectionDetailPartial.html"))
    return response