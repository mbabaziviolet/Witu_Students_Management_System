from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from student_management.models.models import Student

students = Blueprint('students', __name__,url_prefix="/students")



# getting all the students 
@students.route("/", methods=['GET'])
def all_students():
    all_students = Student.query.all() #will return all students which match our query
    return jsonify(all_students),200 #success




#getting single students 
@students.route("/<int:studentId>", methods=['GET'])
def single_student(studentId):
    single_student = Student.query.filter_by(id=studentId).first()
    
    #the code below explains that a student  doesnt exist
    if not single_student:
        return jsonify({'message': '  student is not found'})
    return jsonify(single_student),200



#creating students using the post method
@students.route("/", methods=["POST"])
@jwt_required()
def new_student():
    
    if request.method == "POST":
        
        user_id = get_jwt_identity()
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        gender = request.json['gender']
        age = request.json['age']
        address = request.json['address']
        email = request.json['email']
        password = request.json['password']
        created_at = request.json['created_at']
        deleted_at = request.json['deleted_at']
        updated_at = request.json['updated_at']
        image = request.json['image']
        token = request.json['token']
     
       
    
      
        if not firstname:
                 
          return jsonify({'error': 'First name is required '}), 400 #bad request
          
        if not lastname:
                return jsonify({'error': 'Last name is required'}), 400
            
        if not gender:
                return jsonify({'error': 'gender is required'}), 400
            
        if not age:
                return jsonify({'error': 'age is required'}), 400
            
        if not address:
                return jsonify({'error': 'address is required'}), 400
        
        if not email:
                return jsonify({'error': 'email is required'}), 400
        
        if not password:
                return jsonify({'error': 'password is required'}), 400
        #empty fields
    
        
        #checking if firstname exists
        if Student.query.filter_by(firstname=firstname).first():
                return jsonify({
                'error': 'firstname exists'
            }), 409 #conflicts
        
         #checking if lastname exists
        if Student.query.filter_by(lastname=lastname).first():
                return jsonify({
                'error': 'lastname exists'
            }), 409 #conflicts
                
         #checking if email exists
        if Student.query.filter_by(email=email).first():
                return jsonify({
                'error': 'Email already exists'
            }), 409 #conflicts
                
         #checking if title exists
        if Student.query.filter_by(password=password).first():
                return jsonify({
                'error': 'Password exists'
            }), 409 #conflicts
        
        
           

        #inserting values into the students_list
        new_student = Student(firstname=firstname,lastname=lastname,user_id=user_id,age=age,gender=gender,address=address,email=email,password=password)
        db.session.add(new_student)
        db.session.commit()
        
         
  
    return jsonify({'firstname':firstname,'lastname':lastname,'userid':user_id,'age':age,'gender':gender,'address':address,'email':email,'password':password}),200
    


 

    




