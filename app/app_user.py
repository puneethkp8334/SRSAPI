from flask import Flask, jsonify, request
from db import MySQL
#from db import mysql
from flask_restful import Resource, Api

#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)
app.config['DATABASE_URI'] = 'mysql://srs:Core8967#@db/srs'

#Set database credentials in config.
#app.config['MYSQL_DATABASE_USER'] = 'user_name'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
#app.config['MYSQL_DATABASE_DB'] = 'database_name'
#app.config['MYSQL_DATABASE_HOST'] = 'server_name'

#Initialize the MySQL extension
mysql.init_app(app)


#Get All Users, or Create a new user
class UserList(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from address_book""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = request.form['name']
            _age = request.form['pin']
            _city = request.form['city']
            insert_user_cmd = """INSERT INTO address_book(name, pin, city) 
                                VALUES(%s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_name, _age, _city))
            conn.commit()
            response = jsonify(message='User added successfully.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add user.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)
            
#Get a user by id, update or delete user
class User(Resource):
    def get(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from  address_book where id = %s',user_id)
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = request.form['name']
            _age = request.form['pin']
            _city = request.form['city']
            update_user_cmd = """update address_book 
                                 set name=%s, pin=%s, city=%s
                                 where id=%s"""
            cursor.execute(update_user_cmd, (_name, _age, _city, user_id))
            conn.commit()
            response = jsonify('User updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update user.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

    def delete(self, user_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from address_book where id = %s',user_id)
            conn.commit()
            response = jsonify('User deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete user.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

#API resource routes
api.add_resource(UserList, '/users', endpoint='users')
api.add_resource(User, '/user/<int:user_id>', endpoint='user')

if __name__ == "__main__":
    app.run(debug=True)
