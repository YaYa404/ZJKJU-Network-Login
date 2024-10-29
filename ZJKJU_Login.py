import time
import requests
import logging
from requests.exceptions import RequestException

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 配置参数
CONFIG = {
    "INFURL": 'http://10.80.80.249/eportal/InterFace.do?method=getOnlineUserInfo',
    "LOGINURL": "http://10.80.80.249/eportal/InterFace.do?method=login",
    "HEADERS": {
        "Content-Type": "填写Content-Type",
        "Referer": "填写Referer",
        "User-Agent": "填写User-Agent",
    },
    "LOGINDATA": {
        "userId": "填写userId",
        "password": "填写password",
        "service": "填写service",
        "queryString": "填写queryString",
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": "",
        "passwordEncrypt": "true",
    },
    "PINGTIME": 600
}

def fetch_user_info():
    """获取用户信息并检查连接状态"""
    try:
        response = requests.get(CONFIG['INFURL'])
        response.raise_for_status()  # 抛出HTTP错误

        data = response.json()
        user_index = data.get('userIndex')
        
        if user_index:
            logging.info("连接正常，userIndex：%s", user_index)
        else:
            perform_login()

    except RequestException as e:
        logging.error("请求失败: %s", e)
    except ValueError:
        logging.error("响应内容无法解析为JSON")
    except Exception as e:
        logging.error("发生未知错误: %s", e)

def perform_login():
    """执行登录请求"""
    try:
        response = requests.post(CONFIG['LOGINURL'], headers=CONFIG['HEADERS'], data=CONFIG['LOGINDATA'])
        response.raise_for_status()  # 抛出HTTP错误

        logging.info("登录请求成功，状态码：%s", response.status_code)
        logging.info("响应内容：%s", response.text)

    except RequestException as e:
        logging.error("登录请求失败: %s", e)
    except Exception as e:
        logging.error("发生未知错误: %s", e)

def main():
    """主循环"""
    while True:
        fetch_user_info()
        time.sleep(CONFIG['PINGTIME'])

if __name__ == "__main__":
    main()
