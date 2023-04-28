## 安装虚拟环境

虚拟环境是系统的一个位置，你可以在其 中安装包，并将其与其他Python包隔离

```bash
sudo apt install python3.8-venv

python -m venv ll_env

# 激活虚拟环境 在ll_env中安装的包仅在该环境处于活动状态时才可用
source ll_env/bin/activate

# 停止虚拟环境
deactivate
```

`python -m venv ll_env` 这里运行了模块venv，并使用它来创建一个名为ll_env的虚拟环境

## 安装Django

创建并激活虚拟环境后，就可安装Django了,Django仅在虚拟环境处于活动状态时才可用

```bash
# 虚拟环境中安装Django
pip install Django

# 创建项目
django-admin startproject learning_log .

# 创建数据库
python manage.py migrate

# 查看项目
python manage.py runserver

# 再另一个虚拟环境终端中运行,将会创建应用所需的基础设施
python manage.py startapp learning_logs
```