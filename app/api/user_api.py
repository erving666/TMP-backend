from flask import Blueprint
import datetime
import inject
import hashlib
from app.services import UserService
from flask import jsonify, request
from app.models import User
import jwt
from flask import current_app
from app.api.authenticate_require import login_required

user_service = inject.instance(UserService)

# 用户注册
# 请求路径: /user/register/
# 请求方式: POST
# 请求参数:username password
# 返回值: msg
user = Blueprint('user', __name__)


@user.route('/register/', methods=['POST'])
def register():
    username = request.args.get('username')
    psw = request.args.get('psw')

    strPsw = psw

    m5encrypt = hashlib.md5()

    encodePsw = strPsw.encode(encoding='utf-8')
    m5encrypt.update(encodePsw)

    psw_md5 = m5encrypt.hexdigest()  # md5加密
    user = User(username=username, password=psw_md5)  # 创建用户实体
    user_service.user_persist(entity=user)  # 添加用户到数据库
    return jsonify(msg="注册成功")


# 用户注册
# 请求路径: /user/login/
# 请求方式: POST
# 请求参数:username psw
# 返回值: {'status':'1','token':token}
#        {'status':'0','errmsg':'用户不存在'}
@user.route('/login/', methods=['POST'])
def login():
    username = request.args.get('username')
    psw = request.args.get('psw')
    strPsw = psw
    m5encrypt = hashlib.md5()
    encodePsw = strPsw.encode(encoding='utf-8')
    m5encrypt.update(encodePsw)
    psw_md5 = m5encrypt.hexdigest()  # md5加密
    user = user_service.login(username=username, password=psw_md5)

    if user:
        payload = {
            'id': user.id,
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        }
        token = jwt.encode(payload=payload, key=current_app.config['SECRET_KEY'], algorithm="HS256")
        response = {
            'status': '1',
            'token': token
        }
        return jsonify(response)
    else:
        response = {
            'status': '0',
            'errmsg': '用户不存在'
        }
        return jsonify(response)

# 用户注册
# 请求路径: /user/test/
# 请求方式: POST GET
# 请求参数:请求头的Authorization
# 返回值: {'id':user.id,'username':user.username}
@user.route('/test', methods=['POST', 'GET'])  # 测试登录验证的装饰器
@login_required
def test(user):
    return jsonify(user.to_token_json())
