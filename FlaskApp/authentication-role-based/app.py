from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
)
from datetime import timedelta
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.before_request
def log_request_info():
    logger.info(f"Endpoint: {request.path}, Method: {request.method}, Data: {request.json}")



# Configuration for JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Replace with a secure secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

# Role-based permissions
ROLES_PERMISSIONS = {
    'admin': ['delete', 'edit', 'view'],
    'developer': ['edit', 'view'],
    'tester': ['view']
}

# In-memory database for demonstration
RESOURCES = [{"id": 1, "name": "Resource 1", "description": "A sample resource"}]


# Helper function to check permissions
def has_permission(required_permission, user_role):
    return required_permission in ROLES_PERMISSIONS.get(user_role, [])


# Mock user database
USERS = {
    "admin_user": {"password": "admin123", "role": "admin"},
    "dev_user": {"password": "dev123", "role": "developer"},
    "tester_user": {"password": "tester123", "role": "tester"}
}


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint to authenticate the user and return a JWT token.
    """
    username = request.json.get('username')
    password = request.json.get('password')

    user = USERS.get(username)
    if user and user['password'] == password:
        # Generate JWT token with role claim
        access_token = create_access_token(identity=username, additional_claims={"role": user['role']})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401


@app.route('/resources', methods=['GET'])
@jwt_required()
def view_resources():
    """
    View all resources. All roles have permission to view resources.
    """
    claims = get_jwt()
    if has_permission("view", claims['role']):
        return jsonify(RESOURCES), 200
    return jsonify({"msg": "Permission denied"}), 403


@app.route('/resources/<int:resource_id>', methods=['PUT'])
@jwt_required()
def edit_resource(resource_id):
    """
    Edit a specific resource. Only developers and admins can edit.
    """
    claims = get_jwt()
    if has_permission("edit", claims['role']):
        data = request.json
        for resource in RESOURCES:
            if resource['id'] == resource_id:
                resource.update(data)
                return jsonify(resource), 200
        return jsonify({"msg": "Resource not found"}), 404

    return jsonify({"msg": "Permission denied"}), 403


@app.route('/resources/<int:resource_id>', methods=['DELETE'])
@jwt_required()
def delete_resource(resource_id):
    """
    Delete a specific resource. Only admins can delete.
    """
    claims = get_jwt()
    if has_permission("delete", claims['role']):
        global RESOURCES
        RESOURCES = [r for r in RESOURCES if r['id'] != resource_id]
        return jsonify({"msg": "Resource deleted"}), 200

    return jsonify({"msg": "Permission denied"}), 403


@app.route('/resources', methods=['POST'])
@jwt_required()
def add_resource():
    """
    Add a new resource. Only developers and admins can add.
    """
    claims = get_jwt()
    if has_permission("edit", claims['role']):
        new_resource = request.json
        new_resource['id'] = len(RESOURCES) + 1
        RESOURCES.append(new_resource)
        return jsonify(new_resource), 201

    return jsonify({"msg": "Permission denied"}), 403


if __name__ == '__main__':
    app.run(debug=True)
