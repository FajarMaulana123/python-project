from flask import Blueprint
from controllers.UserController import createUser, deleteUser, index, updateUser, user_

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(index)
user_bp.route('/user_', methods=["POST","GET"])(user_)
user_bp.route('/create_user', methods=["POST"])(createUser)
user_bp.route('/update_user', methods=["POST"])(updateUser)
user_bp.route('/delete_user', methods=["POST"])(deleteUser)
# user_bp.route('/create', methods=['POST'])(store)
# user_bp.route('/<int:user_id>', methods=['GET'])(show)
# user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
# user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)