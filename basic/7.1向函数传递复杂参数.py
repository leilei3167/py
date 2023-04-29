def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

print("\n在函数中修改列表")
# 函数中修改列表,会影响到原列表
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print("原列表已经被修改", unprinted_designs)

# 为了不修改原列表,可以传递列表的副本
# 除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创建副本，从
# 而提高效率，在处理大型列表时尤其如此
print("\n传递列表的副本")
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print("原列表没有被修改", unprinted_designs)
