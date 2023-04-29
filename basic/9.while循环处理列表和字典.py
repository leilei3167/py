# for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以
# 跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。通过将while循环同列
# 表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示

print("移动列表元素")
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())  # 此处进行更多的逻辑,如过滤等
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")

print("\n删除包含特定值的所有列表元素")
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print("before: ", pets)

while "cat" in pets:  # while循环中使用remove()来删除列表中的所有特定值
    pets.remove("cat")

print("after remove cat: ", pets)

print("dog" in pets)  # True

print("\n使用用户输入来填充字典")
responses = {}
flag = True

while flag:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/n) ")
    if repeat == "n":
        flag = False

print("\n--- Poll Results ---", responses)
