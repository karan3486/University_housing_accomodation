import logging
import random
from flask import Blueprint, jsonify, redirect, render_template, flash, session
from flask_cors import cross_origin
from flask import request, jsonify
from flask_login import LoginManager, login_user, logout_user
from DBConnection.dbconnection import  db
from Service.usersService import UserService
from Service.houserequestService import HousingRequestServices
from Service.complainService import ComplainServices
from Service.studentroomService import StudentRoomServices
from send_mail import *
from Utilities.utilities import Action, ResponseMessage

user_bp = Blueprint('user', __name__)
from Logger.logger import get_logger
logger = get_logger()

@user_bp.route('/signup', methods=['GET'])
@cross_origin()
def SignUpPage():
    return render_template("signup.html")

@user_bp.route('/createuser', methods=['POST'])
@cross_origin()
def CreateUser():
    try:
        if request.method == 'POST':
            username = request.form['UserID']
            password = request.form['Password']
            otp = request.form['Otp']
            user_service = UserService()
            check_student =  None
            if not otp:
                check_student = user_service.check_student(int(username))
                if check_student:
                    otp = generate_otp()
                    session['otp'] = otp
                    SendEmail.send_email(check_student.email,'Otp Verification',f'Your Otp for housing portal registration is: {otp}')
                    flash('Enter OTP send to registered email id.', 'error')
                    return render_template("signup.html",userid =username,password=password,otp='otp' )
                else:
                    flash('Invalid Student ID.', 'error')
                    return redirect('/signup')
            if otp and otp == session['otp']:
                response = user_service.user_registration(username,1,password) 
                if response.Success:
                        flash(response.Message, 'success')
                        return redirect("/login")
                else:
                        flash(response.Message, 'error')
                        return redirect('/signup')
            else:
                flash('Invalid OTP.', 'error')
                return render_template("signup.html",userid =username,password=password,otp='otp' )
                

            
    except Exception as e:
        logger.log(logging.ERROR,e)
        return redirect('/signup')

@user_bp.route('/login', methods=['GET'])
@cross_origin()
def LoginPage():
    return render_template("login.html")

@user_bp.route('/logout')
def logout():
    logout_user()  # Log out the user
    return redirect('/login')

@user_bp.route('/dashboard', methods=['POST','GET'])
@cross_origin()
def Auth():
    try:
        houseReq_count = HousingRequestServices().get_all_houseReqList()
        complain_count = ComplainServices().get_all_complainList()
        room_count = StudentRoomServices().get_all_roomList()
        studentRoom_count = StudentRoomServices().get_all_studentroomList()
        if request.method   == 'GET':
            
            return render_template("dashboard.html",userid = session['userid'],house_count=len(houseReq_count),complain_count = len(complain_count),room_count=len(room_count),studentRoom_count=len(studentRoom_count))

        logger.log(logging.INFO,"Authenticating user...")
        logger.error(request.data)
        logger.exception(Exception('An error occurred'))
        userid = int(request.form['UserName'])
            # user = request.form['email']
        password = request.form['Password']
        user = UserService().user_authenticate(userid,password)
        if user:
            login_user(user) 
            session['logged_in'] = True
            session['userid'] = user.id
            return render_template("dashboard.html",userid = session['userid'],house_count=len(houseReq_count),complain_count = len(complain_count),room_count=len(room_count),studentRoom_count=len(studentRoom_count))
        else:
            flash('Error: Invalid credentials. Please try again.', 'error')
            return redirect('/login')
    except Exception as e:
        print(e)
        flash('Error: Invalid credentials. Please try again.', 'error')
        return redirect('/login')
    
def generate_otp(length=6):
    digits = '0123456789'
    otp = ''
    for i in range(length):
        otp += random.choice(digits)
    return otp
