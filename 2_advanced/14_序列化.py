import json


# python中的dict可以直接序列化为json

d = {"name": "Bob", "age": 20, "job": ["学生", "teacher"]}
# ensure_ascii=False可以让中文正常显示
# indent=2可以让json字符串格式化显示
jsond = json.dumps(d, ensure_ascii=False, indent=2)
print(type(jsond), jsond)  # 直接序列化为json字符串


# 然而很多时候我们希望能将一个class直接序列化


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("Bob", 20, 100)
# json.dumps(s)  # TypeError: Object of type 'Student' is not JSON serializable
# 因为默认情况下dumps不知道如何将一个class转化为dict,因此需要提供一个转化函数
# 通常class都有一个__dict__属性，它就是一个dict，用来存储实例变量

print(json.dumps(s, default=lambda obj: obj.__dict__, ensure_ascii=False, indent=2))


# 当然也可以自己定义一个转化函数
def student2json(obj):
    return {"name": obj.name, "age": obj.age, "score": obj.score}


s = json.dumps(s, default=student2json, ensure_ascii=False, indent=2)
print(s)


# 同理,要将一个json字符串反序列化为一个class,也需要提供一个转化函数即object_hook
def json2student(json_str):
    # 返回一个实例
    return Student(json_str["name"], json_str["age"], json_str["score"])


t = json.loads(s, object_hook=json2student)
print(type(t), t, t.name, t.age, t.score)


print("--------------------------------------------------")
print("dump和load可以用于file-like Object,即有read()和write()方法的对象")

# 序列化到文件
with open("test_dump.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)


# 从文件反序列化
with open("test_dump.json", "r", encoding="utf-8") as f:
    d = json.load(f)
    print(type(d), d)
