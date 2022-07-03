from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()


# @dataclass
# class User(db.Model):  
#    __tablename__ = 'users'
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True, nullable=False)
#    email = db.Column(db.String(120), unique=True, nullable=False)
#    password = db.Column(db.Text(), nullable=False)
#    created_at = db.Column(db.DateTime, default=datetime.now())
   


#    def __repr__(self):
#         return "<User %r>" % self.email

@dataclass
class Student(db.Model):  
   __tablename__ = 'students'
   id = db.Column(db.Integer, primary_key=True)
   firstname = db.Column(db.String(255), unique=True, nullable=False)
   lastname = db.Column(db.String(255), unique=True, nullable=False)
   gender = db.Column(db.String(11), unique=True, nullable=False)
   age = db.Column(db.Int(120), unique=True, nullable=False)
   address = db.Column(db.String(11), unique=True, nullable=False)
   email = db.Column(db.String(255), unique=True, nullable=False)
   password = db.Column(db.Text(), nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, default=datetime.now())
   deleted_at = db.Column(db.DateTime, default=datetime.now())
   image = db.Column(db.String(255), unique=True, nullable=False)
   token = db.Column(db.String(255),unique=True, nullable=False)
   course_units = db.relationship("Course_Unit", backref="course_units")
   


   def __repr__(self):
        return "<User %r>" % self.email


@dataclass
class Admin(db.Model):  
   __tablename__ = 'admins'
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(255), unique=True, nullable=False)
   password = db.Column(db.Text(), nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, default=datetime.now())
   deleted_at = db.Column(db.DateTime, default=datetime.now())
   image = db.Column(db.String(255), unique=True, nullable=False)
   token = db.Column(db.String(255),unique=True, nullable=False)
   


   def __repr__(self):
        return "<User %r>" % self.email


@dataclass
class Tutor(db.Model):  
   __tablename__ = 'tutors'
   id = db.Column(db.Integer, primary_key=True)
   firstname = db.Column(db.String(255), unique=True, nullable=False)
   lastname = db.Column(db.String(255), unique=True, nullable=False)
   gender = db.Column(db.String(11), unique=True, nullable=False)
   address = db.Column(db.String(11), unique=True, nullable=False)
   email = db.Column(db.String(255), unique=True, nullable=False)
   password = db.Column(db.Text(), nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, default=datetime.now())
   deleted_at = db.Column(db.DateTime, default=datetime.now())
   image = db.Column(db.String(255), unique=True, nullable=False)
   token = db.Column(db.String(255),unique=True, nullable=False)
   course_units = db.relationship("Course_Unit", backref="course_units")
   


   def __repr__(self):
        return "<User %r>" % self.email


@dataclass
class Course_Unit(db.Model):
    id: int
    title:str
    body:str
    user_id:int
    __tablename__ = 'course_units'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,unique=True,nullable=False)
    description = db.Column(db.Text,unique=True, nullable=False)
    posted_date = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    deleted_at = db.Column(db.DateTime, default=datetime.now())
    students = db.relationship("Student", backref="students")
    students_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    tutors_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))
    tutors = db.relationship("Tutor", backref="tutors")
    time_tables = db.relationship("Time_Table", backref="time_tables")
    time_tables_id = db.Column(db.Integer, db.ForeignKey('time_tables.id'))
    
    
    def __repr__(self):
        return "<Course_Unit %r>" % self.title
    
    
@dataclass
class Time_Table(db.Model):
    id: int
    title:str
    body:str
    user_id:int
    __tablename__ = 'time_tables'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,unique=True,nullable=False)
    description = db.Column(db.Text,unique=True, nullable=False)
    #course_unit_id = db.Column(db.Integer,unique=True, nullable=False)
    day = db.Column(db.Date)
    start_time = db.Column(db.DateTime, default=datetime.now())
    end_time = db.Column(db.DateTime, default=datetime.now())
    duration = db.Column(db.DateTime, default=datetime.now())
    students_id = db.Column(db.Integer, db.ForeignKey('students.id',ondelete='CASCADE'))
    posted_date = db.Column(db.DateTime, default=datetime.now())
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    deleted_at = db.Column(db.DateTime, default=datetime.now())
    course_units = db.relationship("Course_Unit", backref="course_units")
    course_units_id = db.Column(db.Integer, db.ForeignKey('course_units.id'))
    
    
    def __repr__(self):
        return "<Time_Table %r>" % self.title
    
    
    
    
@dataclass
class Enrollment(db.Model):
    id: int
    user_id:int
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    is_enrolled = db.Column(db.Text,unique=True, nullable=False)
    students_id = db.Column(db.Integer, db.ForeignKey('students.id',ondelete='CASCADE'))
    date_of_enrollment = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    deleted_at = db.Column(db.DateTime, default=datetime.now())
    
    
    def __repr__(self):
        return "<Course_Unit %r>" % self.id
    
    
@dataclass
class School_fees_payment(db.Model):
    id: int
    user_id:int
    __tablename__ = 'school_fees_payments'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id',ondelete='CASCADE'))
    mode = db.Column(db.String(11), unique=True, nullable=False)
    amount= db.Column(db.String(11), unique=True, nullable=False)
    is_enrolled = db.Column(db.Text,unique=True, nullable=False)
    status = db.Column(db.Boolean,unique=True, nullable=False)
    balance = db.Column(db.Text,unique=True, nullable=False)
    is_confirmed = db.Column(db.Boolean,unique=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id',ondelete='CASCADE'))
    date = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    deleted_at = db.Column(db.DateTime, default=datetime.now())
    
    
    def __repr__(self):
        return "<Course_Unit %r>" % self.id
    
    

@dataclass
class Assignment(db.Model):
    id: int
    user_id:int
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    file = db.Column(db.File(255), unique=True, nullable=False)
    status = db.Column(db.Boolean,unique=True, nullable=False)
    is_submited = db.Column(db.Boolean,unique=True, nullable=False)
    students_id = db.Column(db.Integer, db.ForeignKey('students.id',ondelete='CASCADE'))
    #tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id',ondelete='CASCADE'))
    updated_at = db.Column(db.DateTime, default=datetime.now())
    deadline = db.Column(db.DateTime, default=datetime.now())
    deleted_at = db.Column(db.DateTime, default=datetime.now())
    students = db.relationship("Student", backref="students")
    tutors_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))
    tutors = db.relationship("Tutor", backref="tutors")
    
    
    def __repr__(self):
        return "<Course_Unit %r>" % self.id
    
    

# @dataclass
# class Question(db.Model):
#     id: int
#     title:str
#     body:str
#     user_id:int
#     answers: list
#     __tablename__ = 'questions'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String,unique=True,nullable=False)
#     body = db.Column(db.Text,unique=True, nullable=False)
#     answers = db.relationship('Answer', backref="question")
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'))
#     posted_date = db.Column(db.DateTime, default=datetime.now())
    

    
#     def __repr__(self):
#         return "<Question %r>" % self.title
# @dataclass
# class Answer(db.Model):
#     id: int
#     body:str
#     user_id:int
#     __tablename__ = 'answers'
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'))
#     question_id = db.Column(db.Integer, db.ForeignKey('questions.id',ondelete='CASCADE'))
#     posted_date = db.Column(db.DateTime, default=datetime.now())
    
      
#     def __repr__(self):
#         return "<Answers %r>" % self.id

    
    



 