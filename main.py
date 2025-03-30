# from database.db import DB
# from Model.User import User
import datetime
import logging
from Utilities.utilities import ExcludeWerkzeugStaticRequests
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, make_response
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
from werkzeug.utils import secure_filename, send_file
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template
from logging.handlers import RotatingFileHandler
from sqlalchemy.ext.automap import automap_base
from Controller.hallofresidence_route import hallofresidence_bp
from Controller.advisor_route import advisor_bp
from Controller.inspection_route import inspection_bp
from Controller.user_route import user_bp
from Controller.houseRequest_route import houserequest_bp
from Controller.manager_route import manager_bp
from Controller.apartmentRoute import apartment_bp
from Controller.complain_route import complain_bp
from Controller.staff_route import staff_bp
from Controller.student_route import student_bp
from Controller.studentroom_route import studentroom_bp
from Controller.invoice_route import invoice_bp
from DBConnection.dbconnection import  db
from config import PASSWORD,HOST,PORT,FROM_MAIL

app = Flask(__name__,static_folder='static')
app.config.from_pyfile('config.py')

log_file_name = f'Logger/Logging/Log_{datetime.datetime.now().strftime("%Y-%m-%d")}.txt'
logging.basicConfig(filename=log_file_name,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.disabled = True
app.logger.info('App started')

# from DBConnection.dbconnection import DB
# dbInstance = DB(app)
db.init_app(app)
# Base = automap_base()
# with app.app_context():
#     engine = db.get_engine()
# Base.prepare(engine, reflect=True)
# with app.app_context():
#     db.reflect()
login_manager = LoginManager()
login_manager.init_app(app)


CORS(app)

@app.before_request
def before_request():
    pass


# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('errors/404.html'), 404

# @app.errorhandler(500)
# def server_error(error):
#     return render_template('errors/500.html'), 500

@login_manager.user_loader
def load_user(user_id):
    from Model.model import Users
    # Implement your own logic to load a user object based on user_id
    # This is just a placeholder function, replace it with your own logic
    return Users.query.get(int(user_id))

# Example user authentication function
def authenticate_user(username, password):
    # Check if username and password are valid
    # This is just a placeholder function, replace it with your own authentication logic
    return True  # Placeholder logic, replace with your authentication logic
@app.context_processor
def inject_user():
    userData=session.get("loggedIn")
    if userData:
        return {"isLoggedIn": True,"data":userData}
    else:
        return{"isLoggedIn": False}
    
@login_manager.unauthorized_handler
def unauthorized():
    # Redirect to the login page if user tries to access protected routes without login
    return redirect('/login')
    
# with app.app_context():
#     dbInstance.initDB()

app.register_blueprint(hallofresidence_bp)
app.register_blueprint(advisor_bp)
app.register_blueprint(inspection_bp)
app.register_blueprint(user_bp)
app.register_blueprint(houserequest_bp)
app.register_blueprint(manager_bp)
app.register_blueprint(apartment_bp)
app.register_blueprint(complain_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(student_bp)
app.register_blueprint(studentroom_bp)
app.register_blueprint(invoice_bp)

@app.route('/', methods=['GET'])
@cross_origin()
def MainPage():

    response = jsonify(render_template("mainpage.html"))
    # response.headers["Content-Type"] = "application/json"
    # return render_template("advisors.html")
    return render_template("mainpage.html")

def send_email(receiver_email, subject, html_content):
    # Create a MIMEMultipart message
    message = MIMEMultipart()
    message['From'] = FROM_MAIL
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach HTML content to the message
    message.attach(MIMEText(html_content, 'html'))

    # Set up the SMTP server
    with smtplib.SMTP(HOST, PORT) as server:
        server.starttls()
        server.login(FROM_MAIL, PASSWORD)
        server.sendmail(FROM_MAIL, receiver_email, message.as_string())



if __name__ == "__main__":
    app.run(port=4080)