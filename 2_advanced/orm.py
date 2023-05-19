# 希望用户这么用:
#
# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()


# 表示表的字段名称和字段类型
class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)  # 当前实例的类的名称和实例属性name的值


# 具体的类型,继承自Field
class StringField(Field):
    def __init__(self, name):
        super().__init__(name, "varchar(100)")


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


# 元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":  # Model类不需要特殊处理,他就是个基类
            return type.__new__(cls, name, bases, attrs)

        print("Found model: %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):  # 是否是Field的实例(字段)
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)  # 记录列名和类型的关系之后,从attr中删除Field属性,否则会和实例属性冲突,整合到类的__mappings__属性中
        attrs["__mappings__"] = mappings  # 保存属性和列的映射关系
        attrs["__table__"] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# 基类model,使用元类创建动态的model类
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():  # __mappings__是在元类中定义的,保存属性和列的映射关系
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = "insert into %s (%s) values (%s)" % (
            self.__table__,
            ",".join(fields),
            ",".join(params),
        )
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))


# 使用方法如下:
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")


# 创建一个实例：
u = User(id=12345, name="Michael", email="test@orm.org", password="my-pwd")
# print(u.id, u.name, u.hel) # 实际上调用的是__getattr__方法,在Model类中定义的
# 保存到数据库：
u.save()


# 就可以基于Model创建任意的表了,因为Model是基于元类构建的,是动态的
class Order(Model):
    id = IntegerField("id")
    item = StringField("item")
    price = IntegerField("price")
    quantity = IntegerField("quantity")


o = Order(id=12345, item="apple", price=10, quantity=3)
o.save()
