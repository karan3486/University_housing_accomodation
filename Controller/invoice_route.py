from flask import Blueprint, jsonify, render_template, request, session
from flask_cors import cross_origin
from flask_login import login_required
from Logger.logger import get_logger
logger = get_logger()
invoice_bp = Blueprint('invoice', __name__)
from Service.invoiceService import InvoiceServices

@invoice_bp.route('/invoices', methods=['GET'])
@cross_origin()
@login_required
def InvoicesPage():
    return render_template("invoice/invoicesListPartial.html",userid = session['userid'])

    
@invoice_bp.route('/invoicedetail/<int:invoice_id>', methods=['GET'])
@cross_origin()
@login_required
def HallDetailPage(invoice_id):
    invoiceDetail = InvoiceServices().get_invoice_detail(invoice_id)
    response = jsonify(render_template("invoice/invoiceDetailPartial.html"))
    return response

@cross_origin()
@login_required
@invoice_bp.route('/delete-invoice/<int:invoice_id>',methods=['DELETE'])
def DeleteInvoiceId(invoice_id):
    isdelete = InvoiceServices().delete_invoice(invoice_id)
    if isdelete:
        return jsonify({'success':True, 'message':'Successfully Deleted Hall id: '+str(invoice_id)})
    else:
        return jsonify({'success': True,'message':'Failed to delete Hall Id: '+ str(invoice_id)+'. Please Try Again.'})
    

@invoice_bp.route('/get_invoice_list', methods=['GET'])
@cross_origin()
@login_required
def OngetInvoiceList():
    invoicelist = InvoiceServices().get_all_invoiceList()
    response = jsonify({'data': invoicelist})
    return response

@invoice_bp.route('/save_invoice', methods=['POST'])
@cross_origin()
@login_required
def SaveInvoiceResidence():
    data = request.form.to_dict()
    # return render_template('notification.html')
    if data.get('invoiceid',None):
        invoicelist = InvoiceServices().updateInvoice(data)
    else:
        data['invoiceid'] = 0
        invoicelist = InvoiceServices().create(data)
        
    if invoicelist:
       id = invoicelist.get('invoicelid',0)
       return jsonify({'success':True, 'message':'Successfully Saved.','id':id})
    else:
        return jsonify({'success': False,'message':'Failed to save.'}) 
    roomTable = json.loads(data.get('gridJsonData'))
    
    
    return response


