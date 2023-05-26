# pip install sqlalchemy
# pip install mysql-connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User

# 快速从表结构创建对象,需要使用sqlacodegen
# 该工具暂时不支持新版python,在3.9是能运行的
# pip install sqlacodegen
# 注意,连接方式这里使用mysql-connector-python,注意提前安装
# sqlacodegen mysql+mysqlconnector://root:123456@127.0.0.1:3306/test > models.py


if __name__ == "__main__":
    # 初始化数据库连接驱动:
    engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/test")
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    # 创建所有注册的表:
    Base.metadata.create_all(engine)

    # 需要获取session对象，然后把对象添加到session中，最后提交并关闭session
    session = DBSession()
    new_user = User(id="6", name="Bodsab")
    session.add(new_user)
    session.commit()
