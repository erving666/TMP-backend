from flask import Blueprint
import datetime
import inject
import hashlib
from app.services import InfoService
from flask import jsonify, request
from app.models import User,Info
import jwt
from flask import current_app
from app.api.authenticate_require import login_required

info_service = inject.instance(InfoService)

# 个人信息查询
# 请求路径: /api/info/all
# 请求方式: GET
# 返回值: msg
info = Blueprint('info', __name__)

@info.route('/info/all', methods=['GET'])
@login_required
def get_info():
    phone = request.args.get('phone')
    user = info_service.info_persist(phone)  #获取登录的用户信息


# 个人信息修改
# 请求路径: /api/info/<user_id>
# 请求方式: POST
# 返回值: 200
@info.route('/info/<user_id>', methods=['POST'])
@login_required
def modify_info(user_id):
    pass
