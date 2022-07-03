from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from student_management.models.models import Tutor

tutors = Blueprint('tutors', __name__,url_prefix="/tutors")



# getting all the tutors 
@tutors.route("/", methods=['GET'])
def all_tutors():
    all_tutors = Tutor.query.all() #will return all tutors which match our query
    return jsonify(all_tutors),200 #success




#getting single tutors 
@tutors.route("/<int:tutorId>", methods=['GET'])
def single_tutor(tutorId):
    single_tutor = Tutor.query.filter_by(id=tutorId).first()
    
    #the code below explains that a student  doesnt exist
    if not single_tutor:
        return jsonify({'message': ' tutor is not found'})
    return jsonify(single_tutor),200



#creating tutors using the post method
@tutors.route("/", methods=["POST"])
@jwt_required()
def new_tutors():
    
    if request.method == "POST":
        
        tutor_id = get_jwt_identity()
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
        if Tutor.query.filter_by(firstname=firstname).first():
                return jsonify({
                'error': 'firstname exists'
            }), 409 #conflicts
        
         #checking if lastname exists
        if Tutor.query.filter_by(lastname=lastname).first():
                return jsonify({
                'error': 'lastname exists'
            }), 409 #conflicts
                
         #checking if email exists
        if Tutor.query.filter_by(email=email).first():
                return jsonify({
                'error': 'Email already exists'
            }), 409 #conflicts
                
         #checking if title exists
        if Tutor.query.filter_by(password=password).first():
                return jsonify({
                'error': 'Password exists'
            }), 409 #conflicts
        
        
           

        #inserting values into the questions_list
        new_tutors = Tutor(firstname=firstname,lastname=lastname,user_id=tutor_id,age=age,gender=gender,address=address,email=email,password=password)
        db.session.add(new_tutors)
        db.session.commit()
        
         
  
    return jsonify({'firstname':firstname,'lastname':lastname,'tutorid':tutor_id,'age':age,'gender':gender,'address':address,'email':email,'password':password}),200
    


 

    




