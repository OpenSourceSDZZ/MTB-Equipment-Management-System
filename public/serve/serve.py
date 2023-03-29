import os
import time
import traceback
import flask
from flask import request
import pymysql
import hashlib
from pymysql.converters import escape_string

# mysql config
mysql_config = {
    'host': '127.0.0.1',
    'user': 'mtb',
    'password': 'admin@sdzz_mtb_mysql2109',
    'db': 'mtb'
}

# 维护模式
maintain_enable = 0
maintain_reason = "正在进行借出调查，暂不开放"

# 图标
logo_start = """<div style="display:flex;flex-direction: column-reverse;">"""

logo_end = {"大疆": """<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDIiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCA0MiAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMzIuNTQ4NDE2MyA0Ljg4MTM1NTFjLS43MDM0MjIxIDIuNjEzNzk5Ny0xLjQwMzY4MzEgNS4yMjgzNDMyLTIuMDg5NjI2NiA3Ljg0Njc5MTUtLjM0MzA2NDcgMS4zMDkwMzgzLS42Nzk4MDczIDIuNjE5MDA2Mi0xLjA3NDc1MDEgMy45MTQyODQ2LS4zODM2MDAzIDEuMjU4NDYxNy0uODU0Nzc5NyAyLjYwMTcxMzQtMS41NDE0NjY5IDMuNzQ0NzA0Ni0uNzE2MjUyMSAxLjE5MjgyMzktMS42NDM3MzU1IDIuMTI0MjEyLTIuOTI3Mjk5NSAyLjcyMDUzMS0uNTEzMjAyNS4yMzgxOTI5LTEuMDM5MDQ5MS40MDE2MzY3LTEuNTkwNzQxNy41MTg1OTQ4LS43ODI4MTk4LjE2NTg2MTEtMS41NjkxNzI0LjIzNDEwMjEtMi4zNjQ2MzYyLjI3OTEwMDMtMS45Njk4Nzk0LjExMTAwOC02LjE0ODc2MDcuMDk0NDU5LTguMTE4MDgyMy4wOTQ0NTlsMS4yMDczMjc0LTQuNDc0NTMwNmMuOTEzOTA5NSAwIDEuODI3NjMzMS4wMDMxNjExIDIuNzQxMzU2Ni0uMDIyMTI3Mi44ODE3NDE0LS4wMjQ1NDQ0IDEuODUxOTkxNi0uMDcxNzczOSAyLjcyMDM0NS0uMjc3MDU0OS45NTA5MTIyLS4yMjQ5OTEgMS42Njg0NjU5LS42MTEwMDg1IDIuMjk2OTUzLTEuMzg0NzE3LjU3MjUxODMtLjcwNDcyMzcuOTU3NDIwMS0xLjU4NDA0NzggMS4yNzI3Nzk0LTIuNDEzMzUzMy41NzYwNTExLTEuNTE0NTA1MSAxLjE2NTg2MjEtMy42ODI5NzE1IDEuNTgxNjMwNS01LjI0MjQ3NDguNDcwMjQ5Ny0xLjc2NTM0MjIuOTIyMjc2OS0zLjUzNTE0NyAxLjM3NzgzNzEtNS4zMDQyMDh6bTguMTM1NTQyMy0uMDAwMDM3MmwtMy41MTIwOSAxMy4wMTY5MzQ2aC02LjUwODE4ODRsMy41MTE5MDQxLTEzLjAxNjkzNDZoNi41MDgzNzQzek0xOS4yMjExODAxIDBoNi41MDgzNzQ0Yy0uNjgxODUyNyAyLjU0MDkxMDEtMS4zNjI3NzU3IDUuMDgyMDA2MS0yLjA1MjQzOCA3LjYyMDg3MDktLjQ4MDY2MjUgMS43Njg2ODktLjk1Nzk3OCAzLjUzODEyMi0xLjQ3OTczMzkgNS4yOTU0Njg2LS4yMjc1OTQxLjc2NjA4NDgtLjQ1NDgxNjQgMS41Mjk5Mzg0LS43NTMwNjg4IDIuMjczNzEwMS0uMjM5NjgwNS41OTc0MzQ2LS41MDc2MjQyIDEuMTI5MDQ1NS0xLjAwMjk3NjIgMS41NzU0OTQ0LS4zNzAwMjY0LjMzMzM5NTctLjc3MzUyMjUuNTQwNzIyLTEuMjQzNDAwMy42ODg1NDY3LS42MDQ1MDA1LjE5MDIxOTYtMS4yMTU1MDg5LjI1OTk0ODItMS44NDAwOTEyLjMxMTA4MjUtLjg5ODI5MDMuMDczNjMzNC0xLjc5Njc2NjUuMDkyNDEzNi0yLjY5NjU0NDQuMTA2OTE3Mi0yLjA2OTM1ODguMDMzMjgzOC01LjgyNzI2NTMuMDI4NjM1Mi03Ljg5NjYyNDIuMDE5NzA5OS0uNzQzNTg1OC0uMDAzMzQ2OS0xLjQ4NzE3MTUtLjAwNzgwOTYtMi4yMzA3NTczLS4wMjEzODM0LS41MzkwNDg1LS4wMDk2NjktMS4wNzc1MzkyLS4wMjMwNTY5LTEuNjE1ODQ0LS4wNTY3MTI2LS4zNTk0Mjc3LS4wMjI2ODUtLjcxNjA2NjItLjA1MjgwNzgtMS4wNzEyMTcyLS4xMTgyNTk3LS4yNDA5ODItLjA0NDI1NDQtLjQ3MzAzODgtLjEwMzc1NjItLjY5OTE0NTQtLjIwMjQ5MTktLjc0NDcwMTQtLjMyNTQwMDEtMS4xMjQyMTEtLjk3NTgyODQtMS4xNDYzMzgyLTEuNzY3OTQ1My0uMDEyODMtLjQ1MzMyODkuMDY2MDA5OC0uODg1MDg4My4xNTY3NS0xLjMyMzU0MTguMTI4ODU4NC0uNjIxMDQ5My4yODkzMjcxLTEuMjMzNTQ1My40NDgzMDgzLTEuODQ2Nzg1MS4zMDM0NTg5LTEuMTcxNjI2NC44NTg4NzA0LTMuMzMzMzk4OSAxLjI5MTc0NTUtNC40NzEzNjk2LjMzOTE2LS44OTE3ODIzLjc4NzA5NjQtMS43NzkyODc4IDEuNjM4MTU3Mi0yLjM0MzgxMDYuNDc1ODI4LS4zMTU1NDUxLjk3NTgyODUtLjQ4MzI2NTYgMS41MjcxNDkzLS41OTQyNzM2LjQwODcwMjUtLjA4MjE4NjcuODE5NDUwNS0uMTI1Njk3NCAxLjIzMzkxNzItLjE1NjU2NC42OTQxMjUtLjA1MTUwNjEgMS4zODg4MDc4LS4wNjc2ODMxIDIuMDg0MjM0My0uMDc5OTU1NC45ODgyODY3LS4wMTcyOTI3IDEuOTc2NTczMy0uMDIxMDExNSAyLjk2NDg2LS4wMjM5ODY2bDIuNDY1MzAxLS4wMDMzNDdoMi40NjUxNjE2bC0uODc4MDIyNSAzLjI1NDE4NzJjLTEuNDY1MjMwMiAwLTIuOTMwMDg4Ni0uMDA0MDkwOC00LjM5NTMxODkuMDA0NDYyNi0uNDI3NjY4Ny4wMDI2MDMyLS44NTQ3Nzk2LS4wMDA1NTc4LTEuMjgyMDc2NC4wMjczMzM2LS4xNTE3Mjk1LjAwOTg1NS0uMjk5OTI2LjAxOTcxLS40NDY2MzUuMDcxMDMwMi0uMTkzMDA4Ny4wNjY5Mzk1LS4yODgzOTc1LjE4ODE3NDMtLjM3MzE4NzQuMzYyMjE2OS0uMTI0MDI0LjI1NDc0MTgtLjE5NTYxMi41MjM0MjkzLS4yNzQ2Mzc3Ljc5MjMwMjgtLjEyMDY3Ny40MTA1NjItLjIzMjQyODcuODIzNTQxMi0uMzQ0MzY2MyAxLjIzNjcwNjQtLjE3MjM2OTEuNjM2NDgyNi0uMzQ0NzM4MiAxLjI3Mjk2NTItLjUwODM2OCAxLjkxMTg2NTEtLjA2MDQzMTQuMjM2NTE5NC0uMTE5NzQ3Mi40NzMwMzg5LS4xNzA2OTU2LjcxMTc4OTYtLjAzNTg4Ny4xNjczNDg2LS4wNjgyNDEuMzM0MTM5NC0uMDg0MjMyMS41MDQ4MzUtLjAxNzQ3ODcuMTg2Njg2Ny0uMDIyODcxLjQxMDkzMzkuMDkwMTgyMy41ODQyMzI3LjExNDkxMjcuMTc1OTAyLjMwOTIyMy4yMTY4MDk0LjQ5MDUxNzQuMjQzMDI3NC4yMDQ5MDkxLjAyOTkzNjguNDEwMTkwMS4wMzY0NDQ4LjYxNjIxNDkuMDQyNTgwOS4zMzczMDA0LjAxMDIyNjkuNjc0NjAxLjAxMTcxNDQgMS4wMTE5MDE0LjAxMzM4NzkuOTIyODM0Ny4wMDQ0NjI2IDEuODQ1NjY5NS4wMDQ2NDg2IDIuNzY4NTA0Mi0uMDAxMTE1Ni40MjUyNTE1LS4wMDI2MDMyLjg1MDEzMTEtLjAwNTU3ODMgMS4yNzUwMTA3LS4wMjI2ODUxLjI5MjY3NDEtLjAxMTcxNDQuNTgxNjI5NS0uMDIxNzU1My44Njk4NDEtLjA5MTQ4MzkuMjE5MDQwOC0uMDUyOTkzNy4zOTAyOTQyLS4xMzYyOTYyLjUzODQ5MDctLjMxNTM1OTIuMTAwMjIzMi0uMTIxMjM0OC4xNjU2NzUyLS4yNTU2NzE1LjIyNTU0ODgtLjM5ODQ3NTcuMTQ4NzU0My0uMzU0MDM1My4yNTI2OTY0LS43MjA1Mjg4LjM2MTEwMTEtMS4wODY4MzY0LjQxNTk1NDQtMS40MDUxNzA3Ljc5MDYyOTQtMi44MjExMjYgMS4xNzM0ODU5LTQuMjM1NDA4bDEuMTQzNDA5NS00LjI0NDE0NzNMMTkuMjIxMTgwMSAwaDYuNTA4Mzc0NHoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZmlsbC1vcGFjaXR5PSIuODUiLz48L3N2Zz4=" style="max-height: 20px;max-width: 20px;"></div>""",
            "索尼": """<img src="/static/sony-logo.png" style="max-height: 15px;max-width:70px;"></div>""",
            "绿联": """<img src="/static/ugreen.png" style="max-height: 15px;max-width:80px;"></div>""",
            "尼康": """<img src="/static/nikon.png" style="max-height: 15px;max-width:70px;"></div>""",
            "农夫山泉": """<img src="/static/nfsqlogo.png" style="max-height: 15px;max-width:70px;"></div>"""}

# 侧边栏
left_drawer = """
<ul class="mdui-list" mdui-collapse="{accordion: true}" style="text-align: left;">
			<li class="mdui-list-item mdui-ripple">
				<i class="mdui-list-item-icon mdui-icon material-icons mdui-text-color-indigo">track_changes</i>
				<a href="./" class="mdui-list-item-content">借出显示面板</a>
			</li>
			<li class="mdui-list-item mdui-ripple">
				<i class="mdui-list-item-icon mdui-icon material-icons mdui-text-color-indigo">search</i>
				<a href="./record" class="mdui-list-item-content">借出查询</a>
			</li>
            <li class="mdui-list-item mdui-ripple">
				<i class="mdui-list-item-icon mdui-icon material-icons mdui-text-color-indigo">thumb_up</i>
				<a href="./panel" class="mdui-list-item-content">设备借出归还系统<sup>Online</sup></a>
			</li>
            <li class="mdui-list-item mdui-ripple">
				<i class="mdui-list-item-icon mdui-icon material-icons mdui-text-color-indigo">dashboard</i>
				<a href="./panel?type=dashboard" class="mdui-list-item-content">仪表板</a>
			</li>
		</ul>
"""

# 名字加logo
def logo_add(text: str):
    for i in logo_end.keys():
        text_list = text.split(i)
        if len(text_list) >= 2:
            text_out = logo_start + text + logo_end[i]
            return text_out
    return text

# 名字防火墙
def name_waf(name:str,id):
    waf_list = ["script","<",">","'",'"',"style"]
    name_new = ""
    for i in name.split(" "):
        name_new += i.lower()
    for i in waf_list:
        i = i.lower()
        if len(name.split(i)) >= 2:
            return f"< 安全拦截 ID-{id} >"
    return name

# 登陆数据存储
login_key = {}

# 获取当前时间
start_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
start_time = int(time.time())

def get_time():
    return int(round(time.time()))

def get_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_dayofweek():
    return time.strftime("%w")

def get_weekofyear():
    return time.strftime("%W")

# 写日志
def log_add(log: str):
    log = f"[{get_time_str()}] {log}"
    try:
        with open(f'server-{time.strftime("%Y-%m-%d", time.localtime())}.log', 'a') as file:
            file.write(f"{log}\n")
    except:
        print("Error:日志系统工作异常，无法完成写入！")
    print("Log:", log)

def log(type:int=0,event:str="None",msg:str="None",url:str="None",ip:str="None",username:str="None"):
    if not os.path.exists("./log/user_event"):
        os.makedirs("./log/user_event")
    if not os.path.exists("./log/sys_event"):
        os.makedirs("./log/sys_event")
    if not os.path.exists("./log/request_event"):
        os.makedirs("./log/request_event")
    try:
        prefix = f"[{get_time_str()}] "
        if type == 1:
            # 用户事件Log
            write_log = prefix + f"User:{username} IP:{ip} Event:{event} Log:{msg}"
            with open(f'./log/user_event/{time.strftime("%Y-%m-%d", time.localtime())}.log', 'a') as file:
                file.write(f"{write_log}\n")
        elif type == 2:
            # 请求事件Log
            write_log = prefix + f"IP:{ip} Event:{event} Log:{msg} Url:{url}"
            with open(f'./log/request_event/{time.strftime("%Y-%m-%d", time.localtime())}.log', 'a') as file:
                file.write(f"{write_log}\n")
        else:
            # 系统事件Log
            write_log = prefix + f"Event:{event} Log:{msg} Url:{url} IP:{ip} User:{username}"
            with open(f'./log/sys_event/{time.strftime("%Y-%m-%d", time.localtime())}.log', 'a') as file:
                file.write(f"{write_log}\n")
        print(write_log)
    except:
        log(type=0,event="日志服务-运行错误",msg=traceback.format_exc())

log(event="服务器启动",msg="日志服务初始化正常")

# 哈希加密
def hash_256(data: str):
    hash256 = hashlib.sha256()
    hash256.update(data.encode('utf-8'))
    return(hash256.hexdigest())

# 获取用户IP
def get_ip(request):
    try:
        ip = request.headers["X-Real-IP"]
        if ip == "" or ip == None:
            ip = request.remote_addr
    except:
        ip = request.remote_addr
    return ip


# 登陆密钥分配函数
def key_check_username(username: str):
    # log(event="登陆密钥管理组件-key_check_username",msg=f"查询用户名对应的Key {username}")
    global login_key
    key_clean_timeout()
    for key in list(login_key.keys()):
        if login_key[key]["username"] == username:
            return key
    return ""


def key_check_key(key: str):
    # log(event="登陆密钥管理组件-key_check_key",msg=f"检查Key是否有效 {key}")
    global login_key
    key_clean_timeout()
    if key in login_key:
        return True
    return False


def key_login(username: str, password: str, name: str, class_str: str, admin: int,login_from:str ):
    global login_key
    key_clean_timeout()
    if not key_logout_username(username):
        log(event="登陆密钥管理组件-key_login",msg=f"Error: 无法完成新key的注册",username=username)
        return ""
    if maintain_enable == 1:
        log(event="登陆密钥管理组件-key_login",msg=f"Error: 维护模式下无法完成Key注册",username=username)
        return ""
    key_str = f"serverSTART{start_date} loginTIME{get_time()} username{username} passowrd{password}"
    key = hash_256(key_str)
    login_key[key] = {
        "login_time": get_time(),
        "timeout": get_time(),
        "username": username,
        "password": password,
        "name": name,
        "class": class_str,
        "admin": admin,
        "login_from": login_from
    }
    key_timeadd(key)
    # log_add(f"登陆key管理系统 - 用户登陆 {username}, {name}, {admin} 分配秘钥：{key}")
    log(event="登陆密钥管理组件-key_login",msg=f"用户登陆成功 {username}")
    log(type=1,event="用户登陆",msg=f"{name} 权限：{admin} 分配秘钥：{key}",username=username)
    return key

def key_logout_username(username: str):
    global login_key
    key_clean_timeout()
    key = key_check_username(username)
    if key != "":
        del(login_key[key])
    if key_check_key(key):
        # log_add("Error:LoginKey-无法删除key (username)")
        log(event="登陆密钥管理组件-key_logout_username",msg=f"Error: 无法删除key {key}",username=username)
        return False
    else:
        # log_add(f"登陆key管理系统 - 用户登出 {username}")
        log(type=1,event="用户登出",msg=f"UserKey:{key}",username=username)
        return True


def key_logout_key(key: str):
    global login_key
    key_clean_timeout()
    if key_check_key(key):
        username = login_key[key]["username"]
        del(login_key[key])

    if key_check_key(key):
        log(event="登陆密钥管理组件-key_logout_key",msg=f"Error: 无法删除key {key}",username=username)
        return False
    else:
        log(type=1,event="用户登出",msg=f"UserKey:{key}",username=username)
        # log_add(f"登陆key管理系统 - 秘钥登出 {key}")
        return True


def key_clean_timeout():
    global login_key
    try:
        for key in list(login_key.keys()):
            if login_key[key]["timeout"] < get_time():
                username = login_key[key]["username"]
                del(login_key[key])
                # log_add(f"登陆key管理系统 - 清理超时秘钥 {key}")
                log(type=1,event="清理在线用户",msg=f"UserKey:{key}",username=username)
    except:
        # log_add("Error:LoginKey-清理超时key失败")
        log(event="登陆密钥管理组件-key_clean_timeout",msg=f"Error: 清理超时key失败 {traceback.format_exc()}")


def key_timeadd(key):
    global login_key
    try:
        if key_check_key(key):
            login_from = login_key[key]["login_from"]
            if login_from == "json":
                login_key[key]["timeout"] = get_time() + 600
            else:
                login_key[key]["timeout"] = get_time() + 120
            username = login_key[key]["username"]
            # log_add(f"登陆key管理系统 - 秘钥续期 {key} {login_key[key]['login_time']}")
            log(type=1,event="秘钥续期",msg=f"UserKey:{key}",username=username)
    except:
        # log_add("Error:LoginKey-秘钥续期失败")
        log(event="登陆密钥管理组件-key_timeadd",msg=f"Error: 秘钥续期失败 {traceback.format_exc()}")


def key_online_int():
    return len(login_key)

# 防SQL注入
def escape(s):
    return pymysql.escape_string(s)


# 初始化
app = flask.Flask(__name__)

log(event="服务器启动",msg="所有函数初始化正常")

# 默认路径
@app.route('/')
def index():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        key_clean_timeout()
        if maintain_enable == 1:
            int_1 = "维护"
            int_2 = "维护"
            int_3 = "维护"
            int_4 = "维护"
            table_list = maintain_reason
            error_1 = ""
            error_2 = ""
        else:
            int_4 = key_online_int()
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = 'select count(id) from equipment'
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    int_1 = str(result[0])
                    sql = 'select count(id) from record'
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    int_2 = str(result[0])
                    sql = 'select count(id) from record where status = 1'
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    int_3 = str(result[0])
                    sql = 'select * from record where status = 1 ORDER BY id'
                    #ASC 表示升序，DESC表示降序 不填写默认升序
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    table_list = ""
                    if result != None:
                        for i in result:
                            user_code = i[1]
                            eq_code = i[2]
                            sql = 'select * from user where code = %s'
                            cursor.execute(sql, escape_string(user_code))
                            result_s = cursor.fetchone()
                            if result_s != None:
                                user_name = result_s[3]
                                user_name = name_waf(user_name,user_code)
                            else:
                                user_name = "Error:UserCode不存在"

                            sql = 'select * from equipment where code = %s'
                            cursor.execute(sql, escape_string(eq_code))
                            result_s = cursor.fetchone()
                            if result_s != None:
                                eq_name = result_s[3]
                                eq_name = name_waf(eq_name,eq_code)
                                eq_name = logo_add(eq_name)
                                try:
                                    # 你被骗了
                                    if len(eq_name.split("ricky"))>=2:
                                        with pymysql.connect(**mysql_config) as conn:
                                            with conn.cursor() as cursor:
                                                sql = 'select * from record where equipment_code = %s and status = 1'
                                                cursor.execute(sql, (escape_string(eq_code)))
                                                result = cursor.fetchone()
                                                if not result:
                                                    log_add(
                                                        f"接口拒绝 /return/{eq_code}/{user_code}/<程序自动> 设备已经登记归还 IP({get_ip(flask.request)})")

                                            with conn.cursor() as cursor:
                                                sql = 'UPDATE record SET status = 0,return_date = %s,return_user_code = %s WHERE equipment_code = %s and status = 1'
                                                cursor.execute(
                                                    sql, (get_time_str(), user_code, escape_string(eq_code)))
                                                sql = 'UPDATE equipment SET status = NULL WHERE code = %s'
                                                cursor.execute(sql, (escape_string(eq_code)))
                                        table_list = """<video autoplay src="//10.3.146.100/admin/" style="width: 100%;">"""
                                        int_1 = "你"
                                        int_2 = "被"
                                        int_3 = "骗"
                                        int_4 = "了"
                                        break
                                except:
                                    pass
                            else:
                                eq_name = "Error:设备Code不存在"
                            table_list += f"<tr><td>{i[0]}</td><td>{user_name}</td><td>{eq_name}</td><td>{eq_code}</td><td>{i[3]}</td><td>未归还</td></tr>"
            
            error_1 = "<!-- "
            error_2 = " -->"
    except Exception as err:
        int_1 = "ERROR"
        int_2 = "ERROR"
        int_3 = "ERROR"
        int_4 = "ERROR"
        table_list = "ERROR"
        error_1 = ""
        error_2 = ""
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
    return flask.render_template("index.html", int_1=int_1, int_2=int_2, int_3=int_3, int_4=int_4, table_list=table_list, error_1=error_1, error_2=error_2, left_drawer=left_drawer)

# 设备管理系统未还列表
@app.route('/cl')
def index_cl():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        key_clean_timeout()
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select count(id) from equipment'
                cursor.execute(sql)
                result = cursor.fetchone()
                int_1 = str(result[0])
                sql = 'select count(id) from record'
                cursor.execute(sql)
                result = cursor.fetchone()
                int_2 = str(result[0])
                sql = 'select count(id) from record where status = 1'
                cursor.execute(sql)
                result = cursor.fetchone()
                int_3 = str(result[0])
                sql = 'select * from record where status = 1'
                cursor.execute(sql)
                result = cursor.fetchall()
                table_list = ""
                if result != None:
                    for i in result:
                        user_code = i[1]
                        eq_code = i[2]
                        sql = 'select * from user where code = %s'
                        cursor.execute(sql, escape_string(user_code))
                        result_s = cursor.fetchone()
                        if result_s != None:
                            user_name = result_s[3]
                        else:
                            user_name = "Error:UserCode不存在"

                        sql = 'select * from equipment where code = %s'
                        cursor.execute(sql, escape_string(eq_code))
                        result_s = cursor.fetchone()
                        if result_s != None:
                            eq_name = result_s[3]
                        else:
                            eq_name = "Error:设备Code不存在"
                        table_list += f"<tr><td>{i[0]}</td><td>{user_name}</td><td>{eq_name}</td><td>{eq_code}</td><td>{i[3]}</td></tr>"
        int_4 = key_online_int()
        error_1 = "<!-- "
        error_2 = " -->"
    except Exception as err:
        int_1 = "ERROR"
        int_2 = "ERROR"
        int_3 = "ERROR"
        int_4 = "ERROR"
        table_list = "ERROR"
        error_1 = ""
        error_2 = ""
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
    return flask.render_template("index-cl.html", int_1=int_1, int_2=int_2, int_3=int_3, int_4=int_4, table_list=table_list, error_1=error_1, error_2=error_2)

# 借出记录查询
@app.route('/record', methods=["GET","POST"])
def index_record():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    error_1 = "<!-- "
    error_2 = " -->"
    table_list = ""
    try:
        query_date=request.form["date"]
        input_value=f'value="{query_date}"'
        try:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = 'select * from record where date like %s"%%" or return_date like %s"%%"'
                    cursor.execute(sql, (escape_string(query_date),escape_string(query_date)))
                    result = cursor.fetchall()
                    table_list = ""
                    if result != None:
                        for i in result:
                            user_code = i[1]
                            eq_code = i[2]
                            sql = 'select * from user where code = %s'
                            cursor.execute(sql, escape_string(user_code))
                            result_s = cursor.fetchone()
                            if result_s != None:
                                user_name = result_s[3]
                                user_name = name_waf(user_name,user_code)
                            else:
                                user_name = "Error:UserCode不存在"
                            
                            return_user_code = i[6]
                            if return_user_code != None:
                                sql = 'select * from user where code = %s'
                                cursor.execute(sql, escape_string(return_user_code))
                                result_s = cursor.fetchone()
                                if result_s != None:
                                    return_user_name = result_s[3]
                                    return_user_name = name_waf(user_name,return_user_code)
                                else:
                                    return_user_name = "Error:UserCode不存在"
                            else:
                                return_user_name = "None"
                            
                            sql = 'select * from equipment where code = %s'
                            cursor.execute(sql, escape_string(eq_code))
                            result_s = cursor.fetchone()
                            if result_s != None:
                                eq_name = result_s[3]
                                eq_name = name_waf(eq_name,eq_code)
                                eq_name = logo_add(eq_name)
                            else:
                                eq_name = "Error:设备Code不存在"
                            table_list += f"<tr><td>{i[0]}</td><td>{user_name}</td><td>{eq_name}</td><td>{eq_code}</td><td>{i[3]}</td><td>{i[5]}</td><td>{return_user_name}</td></tr>"
            error_1 = "<!-- "
            error_2 = " -->"
        except Exception as err:
            table_list = "ERROR"
            error_1 = ""
            error_2 = ""
            log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
    except:
        input_value=""
    return flask.render_template("record.html", table_list=table_list, error_1=error_1, error_2=error_2, left_drawer=left_drawer, input_value=input_value)

@app.route('/panel')
def dashboardpage():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    return flask.render_template("panel.html")

@app.route('/panel.html')
def dashboardpage2():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    return flask.render_template("panel.html")

# 404
@app.errorhandler(404)
def not_found(error):
    # log_add(f"触发404 {flask.request.url} IP({get_ip(flask.request)})")
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method,msg="404")
    url_list = ["/user/","/equipment/","/lending/","/return/"]
    url:str = str(flask.request.url)
    for i in url_list:
        try:
            if len(url.split(i)) > 1:
                return "404",404
        except:
            pass
    return flask.render_template("404.html"), 404

# 500
@app.errorhandler(500)
def serve_error(error):
    # log_add(f"触发404 {flask.request.url} IP({get_ip(flask.request)})")
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method,msg="500")
    url_list = ["/user/","/equipment/","/lending/","/return/"]
    url:str = str(flask.request.url)
    for i in url_list:
        try:
            if len(url.split(i)) > 1:
                return "500",500
        except:
            pass
    return flask.render_template("500.html"), 500

# 数据查询 user
@app.route('/user/<code>')
def user(code):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from user where code = %s'
                cursor.execute(sql, escape_string(code))
                result = cursor.fetchone()
                back = f"编号:{result[0]} Code:{result[1]} 班级:{result[2]} \n姓名:{result[3]} 管理员:{result[4]}"
                # log_add(f"查询数据 /user/{code} IP({get_ip(flask.request)})")
                log(event="查询数据-user",ip=get_ip(flask.request),url=flask.request.url)
                return back
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        return("Error:查询失败", 500)


def get_user_name(code):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from user where code = %s'
                cursor.execute(sql, escape_string(code))
                result = cursor.fetchone()
                back = result[3]
                # log_add(f"查询数据 /user/{code} IP({get_ip(flask.request)})")
                log(event="查询数据-get_user_name",ip=get_ip(flask.request),url=flask.request.url)
                return back
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        return("Unknown", 500)

# 数据查询 equipment
@app.route('/equipment/<code>')
def equipment(code):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from equipment where code = %s'
                cursor.execute(sql, escape_string(code))
                result = cursor.fetchone()
                if (len(result)!=0):
                    back = f"编号:{result[0]} Code:{result[1]} 设备名称:{result[3]} 型号:{result[4]} 归属:{result[2]} SN码:{result[5]} 设备类型:{result[6]}"
                else:
                    back = "Error:找不到数据"
                log(event="查询数据-equipment",ip=get_ip(flask.request),url=flask.request.url)
                return back
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        return ("Error:查询失败",200)

# 登陆验证
@app.route('/login/<code>/<password>')
def login(code, password):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        if maintain_enable == 1:
            return f"NoKey,{maintain_reason}"
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from user where code = %s and password = %s'
                cursor.execute(sql, (escape_string(code),
                               escape_string(hash_256(password))))
                result = cursor.fetchone()
                if result:
                    key = key_login(username=code, password=password,
                                    class_str=result[2], name=result[3], admin=result[4], login_from="c")
                    # log_add(f"用户登录 user:{code} IP({get_ip(flask.request)})")
                    log(type=1,event="客户端登陆",ip=get_ip(flask.request),url=flask.request.url,username=code)
                    with conn.cursor() as cursor:
                        sql = "INSERT INTO dashboardDATA2 (name, code, date, week, day, timestramp) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (escape_string(result[3]), escape_string(code), escape_string(get_time_str()), get_weekofyear(),get_dayofweek(), get_time()))
                        log(type=1,event="客户端登陆-储存",ip=get_ip(flask.request),msg=traceback.format_exc())
                    return f"{key},{code}"
                else:
                    log(type=1,event="客户端登陆-密码错误",ip=get_ip(flask.request),url=flask.request.url,username=code,msg=f"错误的密码：{password}")
                    return "密码错误"

    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        return("Error:查询失败", 500)

# 注销key
@app.route('/logout/<key>')
def logout(key):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        if key_check_key(key):
            username = login_key[key]["username"]
            key_logout_key(key)
            # log_add(f"用户登出 user:{key} IP({get_ip(flask.request)})")
        log(type=1,event="客户端登出",ip=get_ip(flask.request),url=flask.request.url,username=username)
        return "登出成功"
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        return ("Error:登出失败", 500)

# 检查key
@app.route('/check/<key>')
def check(key):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        if key_check_key(key):
            return "Online"
        else:
            return "Offline"
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        return ("Error:检测失败", 500)

# 借出登记
@app.route("/lending/<code>/<user_code>/<key>")
def equipment_lending(code, user_code, key):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    if not key_check_key(key):
        log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的登录令牌 {key}")
        return "无效的登录令牌，请重新登录"
    else:
        key_timeadd(key)
        username = login_key[key]["username"]
    if equipment(code)[0] == "Error:查询失败":
        log(type=1,event="借出设备",ip=get_ip(flask.request),msg=f"操作无法完成：找不到该设备：{code}",username=username)
        return "找不到该设备"
    if user(user_code)[0] == "Error:查询失败":
        log(type=1,event="借出设备",ip=get_ip(flask.request),msg=f"操作无法完成：指派了一个不存在的用户({user_code})用于借出设备({code})",username=username)
        return "找不到该用户"
    if login_key[key]["username"] != user_code and login_key[key]["admin"] != 1:
        log(type=1,event="借出设备",ip=get_ip(flask.request),msg=f"操作无法完成：没有权限为其他用户({user_code})借出设备({code})",username=username)
        return "你没有权限为别人借出设备"
    with pymysql.connect(**mysql_config) as conn:
        with conn.cursor() as cursor:
            sql = 'select * from record where equipment_code = %s and user_code = %s and status = 1'
            cursor.execute(sql, (escape_string(code),
                           escape_string(user_code)))
            result = cursor.fetchone()
            if result:
                log(type=1,event="借出设备",ip=get_ip(flask.request),msg=f"操作无法完成：设备({code})已在用户({user_code})登记过借出",username=username)
                return f"该设备已经登记过借出！"

        sha = hash_256(code+key+str(start_time)+start_date)
        with conn.cursor() as cursor:
            sql = 'UPDATE record SET status = 0,return_date = %s,return_user_code = %s WHERE equipment_code = %s and status = 1'
            cursor.execute(
                sql, (get_time_str(), user_code, escape_string(code)))
            sql = 'INSERT INTO record (user_code, equipment_code, date, status, sha) VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(sql, (escape_string(user_code), escape_string(
                code), escape_string(get_time_str()), 1, sha))
            sql = 'UPDATE equipment SET status = %s WHERE code = %s'
            cursor.execute(sql, (sha, escape_string(code)))

        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO dashboardDATA (usercode, eqcode, week, day, date, timestramp) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (escape_string(user_code), escape_string(code), get_weekofyear(), get_dayofweek(), escape_string(get_time_str()), get_time()))
        except:
            log(type=1,event="借出设备-储存",ip=get_ip(flask.request),msg=traceback.format_exc())

    log(type=1,event="借出设备",ip=get_ip(flask.request),msg=f"设备({code})已在用户({user_code})借出成功",username=username)
    return "借出登记完成"

# 归还登记
@app.route("/return/<code>/<user_code>/<key>")
def equipment_return(code, user_code, key):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    if not key_check_key(key):
        log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的登录令牌 {key}")
        return "无效的登录令牌，请重新登录"
    else:
        key_timeadd(key)
        username = login_key[key]["username"]
    if equipment(code)[0] == "Error:查询失败":
        log(type=1,event="归还设备",ip=get_ip(flask.request),msg=f"操作无法完成：找不到该设备：{code}",username=username)
        return "找不到该设备"
    if user(user_code)[0] == "Error:查询失败":
        log(type=1,event="归还设备",ip=get_ip(flask.request),msg=f"操作无法完成：指派了一个不存在的用户({user_code})用于归还设备({code})",username=username)
        return "找不到该用户"
    if login_key[key]["username"] != user_code and login_key[key]["admin"] != 1:
        log(type=1,event="归还设备",ip=get_ip(flask.request),msg=f"操作无法完成：没有权限为其他用户({user_code})归还设备({code})",username=username)
        return "你没有权限为别人归还设备"

    with pymysql.connect(**mysql_config) as conn:
        with conn.cursor() as cursor:
            sql = 'select * from record where equipment_code = %s and status = 1'
            cursor.execute(sql, (escape_string(code)))
            result = cursor.fetchone()
            if not result:
                log(type=1,event="归还设备",ip=get_ip(flask.request),msg=f"操作无法完成：设备({code})已登记过归还",username=username)
                return f"该设备已经登记归还"
            if result[1] != user_code and login_key[key]["admin"] != 1:
                log(type=1,event="归还设备",ip=get_ip(flask.request),msg=f"操作无法完成：没有权限为其他用户({user_code})归还设备({code})",username=username)
                return "你没有权限为别人归还设备"

        with conn.cursor() as cursor:
            sql = 'UPDATE record SET status = 0,return_date = %s,return_user_code = %s WHERE equipment_code = %s and status = 1'
            cursor.execute(
                sql, (get_time_str(), user_code, escape_string(code)))
            sql = 'UPDATE equipment SET status = NULL WHERE code = %s'
            cursor.execute(sql, (escape_string(code)))

    log(type=1,event="归还设备",ip=get_ip(flask.request),msg=f"设备({code})已在用户({user_code})归还成功",username=username)
    return "归还登记完成"

# 密码更改接口
@app.route("/repasswd/<key>/<old_passwd>/<new_passwd>")
def repasswd(key, old_passwd, new_passwd):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    if not key_check_key(key):
        log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的登录令牌 {key}")
        return "无效的登录令牌，请重新登录"
    else:
        key_timeadd(key)
        username = login_key[key]["username"]

    old_passwd_h = hash_256(old_passwd)
    new_passwd_h = hash_256(new_passwd)

    if old_passwd == "" or new_passwd == "":
        return "数据为空"

    if old_passwd_h == "" or new_passwd_h == "":
        return "无法加密密码信息"

    user_code = login_key[key]["username"]

    with pymysql.connect(**mysql_config) as conn:
        with conn.cursor() as cursor:
            sql = 'select * from user where code = %s'
            cursor.execute(sql, (escape_string(user_code)))
            result = cursor.fetchone()
            if not result:
                log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的用户 {key}")
                return f"找不到用户"
            if result[5] != old_passwd_h:
                log(type=1,event="更改密码-客户端",ip=get_ip(flask.request),msg=f"操作无法完成：旧密码错误",username=username)
                return "旧密码错误"

        with conn.cursor() as cursor:
            sql = 'UPDATE user SET password = %s WHERE code = %s'
            cursor.execute(sql, (new_passwd_h, escape_string(user_code)))

    log(type=1,event="更改密码-客户端",ip=get_ip(flask.request),msg=f"密码更改完成",username=username)
    return "账号密码修改成功"

# 查询设备借出状态
@app.route("/record/equipment/<code>")
def record(code):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    try:
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from record where equipment_code = %s'
                cursor.execute(sql, escape_string(code))
                result = cursor.fetchone()
                status = result[6]
                back = f"{status},编号:{result[0]} 设备Code:{result[2]} 使用人Code:{result[1]} 借出日期:{result[5]} 归还日期:{result[7]}"
                log(event="查询数据-record",ip=get_ip(flask.request),url=flask.request.url)
                return back
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        return ("Error:查询失败", 500)

# 新接口区-开始
###########
# 标准返回内容：{"errcode":ERRCODE,"errmsg":ERRMSG,"data":DATA}

# 设备管理系统未还列表
@app.route('/json/recordlist')
def json_recordlist():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    errcode = 0
    errmsg = 'ok'
    return_json = {}
    try:
        key_clean_timeout()
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from record where status = 1 ORDER BY id;'
                cursor.execute(sql)
                result = cursor.fetchall()
                if result != None:
                    data_no = 0
                    for i in result:
                        user_code = i[1]
                        eq_code = i[2]
                        sql = 'select * from user where code = %s'
                        cursor.execute(sql, escape_string(user_code))
                        result_s = cursor.fetchone()
                        if result_s != None:
                            user_name = result_s[3]
                        else:
                            user_name = "Error:UserCode不存在"
                        sql = 'select * from equipment where code = %s'
                        cursor.execute(sql, escape_string(eq_code))
                        result_s = cursor.fetchone()
                        if result_s != None:
                            eq_name = result_s[3]
                        else:
                            eq_name = "Error:设备Code不存在"
                        return_json[data_no]={"id":i[0],"user_name":user_name,"eq_name":eq_name,"eq_code":eq_code,"date":i[3]}
                        data_no += 1
    except Exception as err:
        errcode = -1
        errmsg = "未知的错误"
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
    return flask.jsonify(errcode=errcode,errmsg=errmsg,data=return_json,length=len(result))

# 获取头部数据(设备总数、借出次数、未还次数，在线人数)
@app.route('/json/getinfo/topdata')
def getinfo_topdata():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    a = {}
    errcodes = 0
    errm = "ok"
    try:
        if maintain_enable == 1:
            int_1 = "维护"
            int_2 = "维护"
            int_3 = "维护"
            int_4 = "维护"
            a = {"lendtime":int_2,"total":int_1,"unreturned":int_3,"onlineuser":int_4}
            errcodes = -666
        else:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = 'select count(id) from equipment'
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    int_1 = str(result[0])
                    sql = 'select count(id) from record'
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    int_2 = str(result[0])
                    sql = 'select count(id) from record where status = 1'
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    int_3 = str(result[0])
                    int_4 = key_online_int()
                    a = {"lendtime":int_2,"total":int_1,"unreturned":int_3,"onlineuser":int_4}
    except Exception as err:
        int_1 = "0"
        int_2 = "0"
        int_3 = "0"
        int_4 = "0"
        a = {"lendtime":int_2,"total":int_1,"unreturned":int_3,"onlineuser":int_4}
        errcodes = -1
        errm = Exception
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
    return flask.jsonify(errcode=errcodes,errmsg=errm,data=a)

# 借出记录查询JSON
@app.route('/json/record/date/<query_date>')
def json_record(query_date):
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    return_json = {}
    status = 0
    data_len = 0
    error=""
    try:
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from record where date like %s"%%"'
                cursor.execute(sql, escape_string(query_date))
                result = cursor.fetchall()
                table_list = ""
                if result != None:
                    data_len = len(result)
                    data_no = 0
                    for i in result:
                        user_code = i[1]
                        eq_code = i[2]
                        sql = 'select * from user where code = %s'
                        cursor.execute(sql, escape_string(user_code))
                        result_s = cursor.fetchone()
                        if result_s != None:
                            user_name = result_s[3]
                            user_name = name_waf(user_name,user_code)
                        else:
                            user_name = "Error:UserCode不存在"
                        
                        return_user_code = i[6]
                        if return_user_code != None:
                            sql = 'select * from user where code = %s'
                            cursor.execute(sql, escape_string(return_user_code))
                            result_s = cursor.fetchone()
                            if result_s != None:
                                return_user_name = result_s[3]
                                return_user_name = name_waf(user_name,return_user_code)
                            else:
                                return_user_name = "Error:UserCode不存在"
                        else:
                            return_user_name = "None"
                        
                        sql = 'select * from equipment where code = %s'
                        cursor.execute(sql, escape_string(eq_code))
                        result_s = cursor.fetchone()
                        if result_s != None:
                            eq_name = result_s[3]
                            eq_name = name_waf(eq_name,eq_code)
                        else:
                            eq_name = "Error:设备Code不存在"
                        return_json[data_no]={"id":i[0],"user_name":user_name,"user_code":user_code,"eq_name":eq_name,"eq_code":eq_code,"lend_date":i[3],"return_date":i[5],"return_user_name":return_user_name,"return_user_code":return_user_code}
                        data_no += 1
    except Exception as err:
        traceback.print_exc()
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error,data=return_json,data_len=data_len)

# 登陆接口JSON
@app.route('/json/login', methods=["POST"])
def json_login():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    try:
        r_data = request.form
        key = ""
        try:
            code = str(r_data.get("username"))
            password = str(r_data.get("password"))
        except:
            status = -1001
            return_code = 200
            error = "缺少参数"
            return flask.jsonify(errcode=status,errmsg=error),return_code
        if maintain_enable == 1:
            status = -666
            return_code = 200
            error = maintain_reason
            return flask.jsonify(errcode=status,errmsg=error),return_code
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = 'select * from user where code = %s and password = %s'
                    cursor.execute(sql, (escape_string(code),
                                escape_string(hash_256(password))))
                    result = cursor.fetchone()
                    if result:
                        key = key_login(username=code, password=password,
                                        class_str=result[2], name=result[3], admin=result[4], login_from="json")
                        log(type=1,event="JSON接口登陆",ip=get_ip(flask.request),url=flask.request.url,username=code)
                        data = login_key[key]
                        data["password"] = None
                        with conn.cursor() as cursor:
                            sql = "INSERT INTO dashboardDATA2 (name, code, date, week, day, timestramp) VALUES (%s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql, (escape_string(result[3]), escape_string(code), escape_string(get_time_str()), get_weekofyear(),get_dayofweek(), get_time()))
                            log(type=1,event="JSON登陆-储存",ip=get_ip(flask.request),msg=traceback.format_exc())
                    else:
                        log(type=1,event="JSON接口登陆-密码错误",ip=get_ip(flask.request),url=flask.request.url,username=code,msg=f"错误的密码：{password}")
                        status = -2001
                        return_code = 200
                        error = "操作失败：账户或密码错误"
                        return flask.jsonify(errcode=status,errmsg=error),return_code
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error,data=data,key=key),return_code

# 登出接口JSON
@app.route('/json/logout', methods=["POST"])
def json_logout():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
        except:
            status = -1001
            return_code = 200
        if status == 0:
            if key_check_key(key):
                username = login_key[key]["username"]
                key_logout_key(key)
                log(type=1,event="JSON接口登出",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error),return_code

# 设备列表获取JSON
@app.route('/json/equipment/list', methods=["POST"])
def json_equipment_list():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
        except:
            status = -1001
            return_code = 200
            error = "缺少参数"
            return flask.jsonify(errcode=status,errmsg=error),return_code
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key超时或不存在"
            return flask.jsonify(errcode=status,errmsg=error),return_code
        else:
            # if login_key[key]["admin"] != 1:
            #     status = -1003
            #     return_code = 403
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = 'select * from equipment'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    data["len"] = len(result)
                    no = 0
                    for i in result:
                        # data[no] = f"{status},编号:{result[0]} 设备Code:{result[2]} 使用人Code:{result[1]} 借出日期:{result[5]} 归还日期:{result[7]}"
                        data[str(no)] = {"id":i[0],"eq_code":i[1],"ascription":i[2],"name":i[3],"model":i[4],"sn":i[5],"type":i[6],"record_sha":i[7]}
                        no += 1
                    log(type=1,event="获取数据-json_equipment_list",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error,data=data),return_code

# 用户列表获取JSON

@app.route('/json/user/list', methods=["POST"])
def json_user_list():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
        except:
            status = -1001
            return_code = 200
            error = "缺少参数"
            return flask.jsonify(errcode=status,errmsg=error),return_code
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key超时或不存在"
            return flask.jsonify(errcode=status,errmsg=error),return_code
        else:
            # if login_key[key]["admin"] != 1:
            #     status = -1003
            #     return_code = 403
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = 'select * from user'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    data["len"] = len(result)
                    no = 0
                    for i in result:
                        # data[no] = f"{status},编号:{result[0]} 设备Code:{result[2]} 使用人Code:{result[1]} 借出日期:{result[5]} 归还日期:{result[7]}"
                        data[str(no)] = {"id":i[0],"usercode":i[1],"class":i[2],"username":i[3],"admin":i[4],"password":i[5]}
                        no += 1
                    log(type=1,event="获取数据-json_user_list",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error,data=data),return_code

# 检查key
@app.route('/json/key/check', methods=["POST"])
def json_check_key():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = ""
    return_code = 200
    data = {}
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
        except:
            status = -1001
            return_code = 200
            error = "缺少参数"
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key超时或不存在"
        if status == 0:
            data = login_key[key]
            data["password"] = None
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(status=status,error=error,data=data),return_code

# 借出设备-JSON
@app.route("/json/equipment/lend", methods=["POST"])
def json_equipment_lend():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    r_data = request.form
    try:
        try:
            key = str(r_data.get("key"))
            user_code = str(r_data.get("user"))
            code = str(r_data.get("code"))
        except:
            status = -1001
            return_code = 200
            error = "缺少参数"
        
        if not key_check_key(key):
            log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的登录令牌 {key}")
            status = -1003
            error = "key超时或不存在"
        else:
            key_timeadd(key)
            username = login_key[key]["username"]

        if login_key[key]["username"] != user_code and login_key[key]["admin"] != 1:
            log(type=1,event="借出设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：没有权限为其他用户({user_code})借出设备({code})",username=username)
            status = -3003
            error = "操作失败：权限不足，你没有权限为别人借出设备"

        if user(user_code)[0] == "Error:查询失败":
            log(type=1,event="借出设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：指派了一个不存在的用户({user_code})用于借出设备({code})",username=username)
            status = -3001
            error = "找不到该用户"
            data["lenduser"] = "未知用户"
        else:
            data["lenduser"] = get_user_name(user_code)

        if equipment(code)[0] == "Error:查询失败" or equipment(code)[0] == "Error:找不到数据":
            log(type=1,event="借出设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：找不到该设备：{code}",username=username)
            status = -3002
            error = "找不到该设备"
            data["lendcode"] = code
            data["lendname"] = "未知设备"
        else:
            with pymysql.connect(**mysql_config) as conn2:
                with conn2.cursor() as cursor2:
                    sql = 'select * from equipment where code = %s'
                    cursor2.execute(sql, escape_string(code))
                    result2 = cursor2.fetchone()
                    data["lendcode"] = result2[1]
                    data["lendname"] = result2[3]
        #update(json_lend): 阻止的方式
        if status < 0:
            return flask.jsonify(errcode=status,errmsg=error,data=data),return_code
        
        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from record where equipment_code = %s and user_code = %s and status = 1'
                cursor.execute(sql, (escape_string(code),
                            escape_string(user_code)))
                result = cursor.fetchone()
                if result:
                    log(type=1,event="借出设备",ip=get_ip(flask.request),msg=f"操作无法完成：设备({code})已在用户({user_code})登记过借出",username=username)
                    status = -3004
                    error = "操作失败：该设备已经登记借出！"
            sha = hash_256(code+key+str(start_time)+start_date)
            with conn.cursor() as cursor:
                sql = 'UPDATE record SET status = 0,return_date = %s,return_user_code = %s WHERE equipment_code = %s and status = 1'
                cursor.execute(
                    sql, (get_time_str(), user_code, escape_string(code)))
                sql = 'INSERT INTO record (user_code, equipment_code, date, status, sha) VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(sql, (escape_string(user_code), escape_string(
                    code), escape_string(get_time_str()), 1, sha))
                sql = 'UPDATE equipment SET status = %s WHERE code = %s'
                cursor.execute(sql, (sha, escape_string(code)))
            try:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO dashboardDATA (usercode, eqcode, week, day, date, timestramp) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (escape_string(user_code), escape_string(code), get_weekofyear(), get_dayofweek(), escape_string(get_time_str()), get_time()))
            except:
                log(type=1,event="借出设备-储存",ip=get_ip(flask.request),msg=traceback.format_exc())
        log(type=1,event="借出设备-JSON",ip=get_ip(flask.request),msg=f"设备({code})已在用户({user_code})借出成功",username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error,data=data),return_code

# 归还登记
@app.route("/json/equipment/return", methods=["POST"])
def json_equipment_return():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    r_data = request.form
    try:
        key = str(r_data.get("key"))
        user_code = str(r_data.get("user"))
        code = str(r_data.get("code"))
    except:
        status = -1001
        return_code = 200
        error = "缺少参数"
    if not key_check_key(key):
        log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的登录令牌 {key}")
        status = -1003
        error = "key超时或不存在"
    else:
        key_timeadd(key)
        username = login_key[key]["username"]
    try:
        if equipment(code)[0] == "Error:查询失败" or equipment(code)[0] == "Error:找不到数据":
            log(type=1,event="归还设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：找不到该设备：{code}",username=username)
            status = -3006
            error = "找不到该设备"
            data["returncode"] = code
            data["returnname"] = "未知设备"
        else:
            with pymysql.connect(**mysql_config) as conn2:
                with conn2.cursor() as cursor2:
                    sql = 'select * from equipment where code = %s'
                    cursor2.execute(sql, escape_string(code))
                    result2 = cursor2.fetchone()
                    data["returncode"] = code
                    data["returnname"] = result2[3]
        if user(user_code)[0] == "Error:查询失败":
            log(type=1,event="归还设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：指派了一个不存在的用户({user_code})用于归还设备({code})",username=username)
            status = -3005
            error = "找不到该用户"
            data["returnuser"] = "未知用户"
        else:
            data["returnuser"] = get_user_name(user_code)
        if login_key[key]["username"] != user_code and login_key[key]["admin"] != 1:
            log(type=1,event="归还设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：没有权限为其他用户({user_code})归还设备({code})",username=username)
            status = -3007
            error = "操作失败：权限不足"
        if status < 0:
            return flask.jsonify(errcode=status,errmsg=error,data=data),return_code

        with pymysql.connect(**mysql_config) as conn:
            with conn.cursor() as cursor:
                sql = 'select * from record where equipment_code = %s and status = 1'
                cursor.execute(sql, (escape_string(code)))
                result = cursor.fetchone()
                if not result:
                    log(type=1,event="归还设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：设备({code})已登记过归还",username=username)
                    status = -3008
                    error = "操作失败：该设备已经登记归还！"
                elif result[1] != user_code and login_key[key]["admin"] != 1:
                    log(type=1,event="归还设备-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：没有权限为其他用户({user_code})归还设备({code})",username=username)
                    status = -3007
                    error = "操作失败：权限不足"
            with conn.cursor() as cursor:
                sql = 'UPDATE record SET status = 0,return_date = %s,return_user_code = %s WHERE equipment_code = %s and status = 1'
                cursor.execute(
                    sql, (get_time_str(), user_code, escape_string(code)))
                sql = 'UPDATE equipment SET status = NULL WHERE code = %s'
                cursor.execute(sql, (escape_string(code)))
                sql = 'select * from equipment where code = %s'
                cursor.execute(sql, escape_string(code))
                result = cursor.fetchone()

        log(type=1,event="归还设备-JSON",ip=get_ip(flask.request),msg=f"设备({code})已在用户({user_code})归还成功",username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error,data=data),return_code

# 密码更改接口JSON
@app.route("/json/changepassword", methods=["POST"])
def changepassword():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    r_data = request.form
    try:
        key = str(r_data.get("key"))
        old_passwd = str(r_data.get("oldpassword"))
        new_passwd = str(r_data.get("newpassword"))
    except:
        status = -1001
        error = "缺少参数"
        return flask.jsonify(errcode=status,errmsg=error),return_code
    if not key_check_key(key):
        log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的登录令牌 {key}")
        status = -1003
        error = "key超时或不存在"
        return flask.jsonify(errcode=status,errmsg=error),return_code
    else:
        key_timeadd(key)
        username = login_key[key]["username"]

    old_passwd_h = hash_256(old_passwd)
    new_passwd_h = hash_256(new_passwd)

    if old_passwd == "" or new_passwd == "":
        status = -1001
        error = "缺少参数"
        return flask.jsonify(errcode=status,errmsg=error),return_code

    if old_passwd_h == "" or new_passwd_h == "":
        status = -2004
        error = "操作失败：无法加密密码信息"
        return flask.jsonify(errcode=status,errmsg=error),return_code

    user_code = login_key[key]["username"]

    with pymysql.connect(**mysql_config) as conn:
        with conn.cursor() as cursor:
            sql = 'select * from user where code = %s'
            cursor.execute(sql, (escape_string(user_code)))
            result = cursor.fetchone()
            if not result:
                log(event="拒绝访问",ip=get_ip(flask.request),url=flask.request.url,msg=f"无效的用户 {key}")
                status = -2003
                error = "操作失败：找不到用户"
                return flask.jsonify(errcode=status,errmsg=error),return_code
            if result[5] != old_passwd_h:
                log(type=1,event="更改密码-JSON",ip=get_ip(flask.request),msg=f"操作无法完成：旧密码错误",username=username)
                status = -2002
                error = "操作失败：原密码错误"
                return flask.jsonify(errcode=status,errmsg=error),return_code

        with conn.cursor() as cursor:
            sql = 'UPDATE user SET password = %s WHERE code = %s'
            cursor.execute(sql, (new_passwd_h, escape_string(user_code)))

    log(type=1,event="更改密码-JSON",ip=get_ip(flask.request),msg=f"密码更改完成",username=username)
    return flask.jsonify(errcode=status,errmsg=error),return_code


# 下面的接口大同小异，只验证了第一个。

# 设备操作接口区-开始
# 添加设备JSON
# key	String	是	用户登录凭据
# eqname	String	是	设备名称
# eqcode	String	是	设备Code
# ascription	String	是	归属
# model	String	是	型号
# sn	String	是	SN码
@app.route('/json/admin/equipment/add', methods=["POST"])
def json_equipment_add():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    name = "null"
    code = "null"
    asc = "null"
    sn = "null"
    model = "null"
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
            name = str(r_data.get("eqname"))
            code = str(r_data.get("eqcode"))
            asc = str(r_data.get("ascription"))
            sn = str(r_data.get("sn"))
            model = str(r_data.get("model"))
        except:
            status = -1001
            return_code = 200
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key无效或已过期"
        else:
            if login_key[key]["admin"] != 1:
                status = -1004
                return_code = 200
                error = "操作失败：无权限"
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO equipment (code, ascription, name, model, sn) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (code,asc,name,model,sn))
                    log(type=1,event="JSON-添加设备",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error),return_code


# 编辑设备JSON
# key	String	是	用户登录凭据
# id	Int	是	数据id
# eqname	String	是	设备名称
# eqcode	String	是	设备Code
# ascription	String	是	归属
# model	String	是	型号
# sn	String	是	SN码
@app.route('/json/admin/equipment/edit', methods=["POST"])
def json_equipment_edit():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    name = "null"
    code = "null"
    asc = "null"
    sn = "null"
    model = "null"
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
            ids = str(r_data.get("id"))
            name = str(r_data.get("eqname"))
            code = str(r_data.get("eqcode"))
            asc = str(r_data.get("ascription"))
            sn = str(r_data.get("sn"))
            model = str(r_data.get("model"))
        except:
            status = -1001
            return_code = 200
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key无效或已过期"
        else:
            if login_key[key]["admin"] != 1:
                status = -1004
                return_code = 200
                error = "操作失败：无权限"
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE equipment SET code=%s,ascription=%s,name=%s,model=%s,sn=%s WHERE id = %s"
                    cursor.execute(sql, (code,asc,name,model,sn,ids))
                    log(type=1,event="JSON-编辑设备",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error),return_code


# 删除设备JSON
# key	String	是	用户登录凭据
# id	Int	是	数据id
@app.route('/json/admin/equipment/del', methods=["POST"])
def json_equipment_del():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
            ids = str(r_data.get("id"))
        except:
            status = -1001
            return_code = 200
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key无效或已过期"
        else:
            if login_key[key]["admin"] != 1:
                status = -1004
                return_code = 200
                error = "操作失败：无权限"
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM equipment WHERE id=%s"
                    cursor.execute(sql, (ids))
                    log(type=1,event="JSON-删除设备",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error),return_code

# 设备操作接口区-结束
# 人员管理接口区-开始


# 添加账号
# key	String	是	用户登录凭据
# name	String	是	用户名称
# code	String	是	用户Code
# class	String	是	班级
# admin	Int	是	是否管理
# password	String	是	SN码
@app.route('/json/admin/user/add', methods=["POST"])
def json_user_add():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    name = "null"
    code = "null"
    cla = "null"
    admin = "null"
    password = "null"
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
            name = str(r_data.get("name"))
            code = str(r_data.get("code"))
            cla = str(r_data.get("class"))
            admin = str(r_data.get("admin"))
            password = str(r_data.get("password"))
        except:
            status = -1001
            return_code = 200
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key无效或已过期"
        else:
            if login_key[key]["admin"] != 1:
                status = -1004
                return_code = 200
                error = "操作失败：无权限"
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO user(code, class, name, admin, password) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (code,cla,name,admin,password))
                    log(type=1,event="JSON-添加账号",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error),return_code


# 编辑账号
# key	String	是	用户登录凭据
# name	String	是	用户名称
# code	String	是	用户Code
# class	String	是	班级
# admin	Int	是	是否管理
# password	String	是	SN码
@app.route('/json/admin/user/edit', methods=["POST"])
def json_user_edit():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    name = "null"
    code = "null"
    cla = "null"
    admin = "null"
    password = "null"
    ids="null"
    try:
        r_data = request.form
        try:
            ids = str(r_data.get("id"))
            key = str(r_data.get("key"))
            name = str(r_data.get("name"))
            code = str(r_data.get("code"))
            cla = str(r_data.get("class"))
            admin = str(r_data.get("admin"))
            password = str(r_data.get("password"))
        except:
            status = -1001
            return_code = 200
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key无效或已过期"
        else:
            if login_key[key]["admin"] != 1:
                status = -1004
                return_code = 200
                error = "操作失败：无权限"
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE user SET code = %s,class = %s,name = %s,admin = %s,password = %s WHERE id = %s"
                    cursor.execute(sql, (code,cla,name,admin,password,ids))
                    log(type=1,event="JSON-编辑账号",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error),return_code


# 删除设备JSON
# key	String	是	用户登录凭据
# id	Int	是	数据id
@app.route('/json/admin/user/del', methods=["POST"])
def json_user_del():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
            ids = str(r_data.get("id"))
        except:
            status = -1001
            return_code = 200
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key无效或已过期"
        else:
            if login_key[key]["admin"] != 1:
                status = -1004
                return_code = 200
                error = "操作失败：无权限"
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM user WHERE id=%s"
                    cursor.execute(sql, (ids))
                    log(type=1,event="JSON-删除账号",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error),return_code

# 人员管理接口区-结束

@app.route('/json/record/list', methods=["POST"])
def json_record_list():
    log(type=2,ip=get_ip(flask.request),url=flask.request.url,event=request.method)
    status = 0
    error = "ok"
    return_code = 200
    data = {}
    try:
        r_data = request.form
        try:
            key = str(r_data.get("key"))
        except:
            status = -1001
            return_code = 200
            error = "缺少参数"
            return flask.jsonify(errcode=status,errmsg=error),return_code
        if not key_check_key(key):
            status = -1003
            return_code = 200
            error = "key超时或不存在"
            return flask.jsonify(errcode=status,errmsg=error),return_code
        else:
            # if login_key[key]["admin"] != 1:
            #     status = -1003
            #     return_code = 403
            username = login_key[key]["username"]
            key_timeadd(key)
        if status == 0:
            with pymysql.connect(**mysql_config) as conn:
                with conn.cursor() as cursor:
                    sql = 'select * from record'
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    data["len"] = len(result)
                    no = 0
                    for i in result:
                        # data[no] = f"{status},编号:{result[0]} 设备Code:{result[2]} 使用人Code:{result[1]} 借出日期:{result[5]} 归还日期:{result[7]}"
                        if i[5] == "" or i[6] == "":
                            data[str(no)] = {"id":i[0],"usercode":i[1],"eqcode":i[2],"date":i[3],"status":i[4],"returndate":"未归还","returnuser":"未归还"}
                        else:
                            data[str(no)] = {"id":i[0],"usercode":i[1],"eqcode":i[2],"date":i[3],"status":i[4],"returndate":i[5],"returnuser":i[6]}
                        no += 1
                    log(type=1,event="获取数据-json_record_list",ip=get_ip(flask.request),url=flask.request.url,username=username)
    except:
        log(event="RouteError",ip=get_ip(flask.request),url=flask.request.url,msg=traceback.format_exc())
        status = -1
        error = "未知的错误"
    return flask.jsonify(errcode=status,errmsg=error,data=data),return_code

# 新接口区结束

# 运行
if __name__ == '__main__':
    log(event="服务器启动",msg="代码加载完成，运行Flask服务")
    app.run(host='0.0.0.0', port=5055, debug=False)