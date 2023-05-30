# 默认的Django配置文件settings.py只有一份,无法区分dev,test,prod环境
# 因此需要将settings.py拆分成三份,分别为settings/dev.py,settings/test.py,settings/prod.py
# 在manage.py和wsgi.py中指定环境变量来加载不同的配置文件
