# 导入依赖包
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from MySql import exec_mysql_cmd





def create_token(APP, api_user):
    """
    生成token
    :param APP: 
    :param api_user:用户id
    :return: token
    """

    # 第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    # 第二个参数是有效期(秒)
    s = Serializer(APP.config["SECRET_KEY"], expires_in=3600)
    # 接收用户id转换与编码
    token = s.dumps({"id": api_user}).decode("ascii")
    return token


def verify_token(APP, token):
    """
    校验token
    :param APP: 
    :param token:
    :return: 用户信息 or None
    """

    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(APP.config["SECRET_KEY"])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception as e:
        print(e)
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    cmd = "SELECT * FROM 用户管理 WHERE id=%s;" % data['id']
    user = exec_mysql_cmd(cmd)
    return user
