from flask import jsonify, request, abort
from app import mongo
from bson.objectid import ObjectId
from app.schemas import user_schema, users_schema

@main.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return users_schema.dump(users)

@main.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one_or_404({"_id": ObjectId(id)})
    return user_schema.dump(user)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    result = mongo.db.users.insert_one(data)
    user = mongo.db.users.find_one({"_id": result.inserted_id})
    return user_schema.dump(user), 201

@main.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    return user_schema.dump(user)

@main.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({"message": "User deleted"})
    else:
        abort(404, description="User not found")
