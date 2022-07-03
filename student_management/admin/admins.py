from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from student_management.models.models import Admin

admins = Blueprint('admins', __name__,url_prefix="/admins")



# getting all the admins 
@admins.route("/", methods=['GET'])
def all_admins():
    all_admins = Admin.query.all() #will return all admins which match our query
    return jsonify(all_admins),200 #success




#getting single admins 
@admins.route("/<int:adminId>", methods=['GET'])
def single_admin(adminId):
    single_admin = Admin.query.filter_by(id=adminId).first()
    
    #the code below explains that admin  doesnt exist
    if not single_admin:
        return jsonify({'message': '  admin is not found'})
    return jsonify(single_admin),200



#creating admins using the post method
@admins.route("/", methods=["POST"])
@jwt_required()
def new_admin():
    
    if request.method == "POST":
        
        admin_id = get_jwt_identity()
        email = request.json['email']
        password = request.json['password']
        created_at = request.json['created_at']
        deleted_at = request.json['deleted_at']
        updated_at = request.json['updated_at']
        image = request.json['image']
        token = request.json['token']
     
       
    

            
        if not email:
                return jsonify({'error': 'email is required'}), 400
        
        if not password:
                return jsonify({'error': 'password is required'}), 400
        #empty fields
    
        

                
         #checking if email exists
        if Admin.query.filter_by(email=email).first():
                return jsonify({
                'error': 'Email already exists'
            }), 409 #conflicts
                
         #checking if title exists
        if Admin.query.filter_by(password=password).first():
                return jsonify({
                'error': 'Password exists'
            }), 409 #conflicts
        
        
           

        #inserting values into the questions_list
        new_admin = Admin(email=email,password=password,admin_id=admin_id)
        db.session.add(new_admin)
        db.session.commit()
        
         
  
    return jsonify({'email':email,'password':password,'adminid':admin_id}),200
    


 

    




