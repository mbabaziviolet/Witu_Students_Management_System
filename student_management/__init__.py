import os
from flask import Flask
from flask_jwt_extended import JWTManager
# from student_management.models.models import db



#Application Factory Function
def create_app(test_config=None):
    # creating  and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    

    if test_config is None:
  
       app.config.from_mapping(

        CORS_HEADERS= 'Content-Type',
        SQLALCHEMY_DATABASE_URI = "sqlite:///witu_students_management_system",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
 
    )
    else:
      
        app.config.from_mapping(test_config)
   

   
    JWTManager(app)
    
    
   
    # from student_management.questions.question import questions
    # from student_management.auth.routes import auth
    from student_management.student.students import student
    from student_management.tutor.tutors import tutor
    from student_management.admin.admins import admin
    from student_management.time_table.time_tables import time_table
 
    #registering blueprints    
  
    # app.register_blueprint(questions)
    # app.register_blueprint(auth)
    app.register_blueprint(student)
    app.register_blueprint(tutor)
    app.register_blueprint(admin)
    app.register_blueprint(time_table)
    
    JWTManager(app)
   
    # db.app = app
    # db.init_app(app)
    # db.create_all()
   
    return app

