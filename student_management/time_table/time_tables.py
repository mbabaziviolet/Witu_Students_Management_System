from flask import  jsonify, request, Blueprint
from flask_jwt_extended import jwt_required,get_jwt_identity
from student_management.models.models import Time_Table

time_tables = Blueprint('time_tables', __name__,url_prefix="/time_tables")



# getting all the time_tables 
@time_tables.route("/", methods=['GET'])
def all_time_tables():
    all_time_tables = Time_Table.query.all() #will return all time_tables which match our query
    return jsonify(all_time_tables),200 #success




#getting single time_tables 
@time_tables.route("/<int:time_tableId>", methods=['GET'])
def single_time_table(time_tableId):
    single_time_table = Time_Table.query.filter_by(id=time_tableId).first()
    
    #the code below explains that a time_table  doesnt exist
    if not single_time_table:
        return jsonify({'message': '  time_table is not found'})
    return jsonify(single_time_table),200



#creating time_tables using the post method
@time_tables.route("/", methods=["POST"])
@jwt_required()
def new_time_table():
    
    if request.method == "POST":
        
        time_table_id = get_jwt_identity()
        title = request.json['title']
        description = request.json['description']
        day = request.json['day']
        start_time = request.json['start_time']
        end_time = request.json['end_time']
        duration = request.json['duration']
        posted_date = request.json['posted_date']
        created_at = request.json['created_at']
        updated_at = request.json['updated_at']
        deleted_at = request.json['deleted_at']
        
     
       
    
      
        if not title:
                 
          return jsonify({'error': 'title is not found '}), 400 #bad request
          
        if not description:
                return jsonify({'error': 'description is required'}), 400
            
       
            
        #empty fields
    
        
        #checking if title exists
        if Time_Table.query.filter_by(title=title).first():
                return jsonify({
                'error': 'title exists'
            }), 409 #conflicts
        
         #checking if description exists
        if Time_Table.query.filter_by(description=description).first():
                return jsonify({
                'error': 'description exists'
            }), 409 #conflicts
                
        
        
        
           

        #inserting values into the time_tables_list
        new_time_table = Time_Table(title=title,description=description,time_table_id=time_table_id)
        db.session.add(new_time_table)
        db.session.commit()
        
         
  
    return jsonify({'title':title,'description':description,'time_table_id':time_table_id}),200
    


 

    




