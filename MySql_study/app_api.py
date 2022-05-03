#! /usr/bin/python
# -*- coding: UTF-8 -*-
import functools

from flask import Flask, jsonify, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from gevent import pywsgi

from MySql import exec_mysql_cmd
from v_token import create_token

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloword'


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token2(*args, **kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers["z-token"]
        except Exception as e:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            print(e)
            return jsonify(code=4103, msg='缺少参数token')

        s = Serializer(app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception as e:
            print(e)
            return jsonify(code=4101, msg="登录已过期")

        return view_func(*args, **kwargs)

    return verify_token2


@app.route('/')
def index():
    return jsonify(code=200, data='root')


@app.route('/api/', methods=['POST', 'GET'])
def hello_world():
    print(request.data)
    return jsonify(code=200, data='root')


@app.route('/api/create_usr', methods=['POST'])
def create_usr():
    name = request.form['name']
    passwd = request.form['passwd']
    cmd_o = 'INSERT INTO 用户管理  ' \
            '(name, passwd)  ' \
            'VALUES  ' \
            '("%s","%s")' % (name, passwd)
    cmd_q = "SELECT id FROM 用户管理 WHERE name='%s';" % name
    info = exec_mysql_cmd(cmd_q)
    if info:
        return jsonify(code=4102, date='用户已注册')
    else:
        exec_mysql_cmd(cmd_o)
        info = exec_mysql_cmd(cmd_q)
        if info:
            return jsonify(code=200, date='注册成功')
        else:
            return jsonify(code=4104, date='无法注册')


@app.route('/api/login_usr', methods=['POST'])
def login_usr():
    name = request.form['name']
    passwd = request.form['passwd']
    cmd_q = "SELECT (id,passwd) FROM 用户管理 WHERE name='%s';" % name
    info = exec_mysql_cmd(cmd_q)
    q_id = info[0][0]
    q_passwd = info[0][1]
    if q_passwd == passwd:
        token = create_token(app, q_id)
        return jsonify(code=200, token=token)
    else:
        return jsonify(code=4105, data='密码错误')


if __name__ == '__main__':
    app.run()
