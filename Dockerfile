# 使用官方 Python 3.8-slim-buster 作为基础镜像
FROM python:3.8-slim-buster

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 和 Python 脚本到工作目录
COPY requirements.txt requirements.txt
COPY ZJKJU_Login.py ZJKJU_Login.py

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 追加设置时区为上海
ENV TZ=Asia/Shanghai

# 设置容器启动时执行的命令
CMD ["python", "ZJKJU_Login.py"]