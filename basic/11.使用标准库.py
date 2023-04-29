# 字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序。要创建字典并记录其
# 中的键—值对的添加顺序，可使用模块collections中的OrderedDict类
from collections import OrderedDict

# 创建实例
favorite_languages = OrderedDict()

# 写入键值对
favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

# 遍历字典
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
