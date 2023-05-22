import hashlib

s1 = "abc".encode("utf-8")
s2 = "abcc".encode("utf-8")


# 摘要函数是一个单向函数，不可逆,可用于数据防篡改

# md5
md5 = hashlib.md5()

md5.update(s1)
print(type(md5.hexdigest()))
print("s1: ", md5.hexdigest())  # 返回到目前为止传递给 update() 方法的数据的摘要。它是一个字符串对象，其内容是一串十六进制数字


# pip install bcrypt
import bcrypt

salt = bcrypt.gensalt()

user_password = "admin123".encode("utf-8")
hashed_password = bcrypt.hashpw(user_password, salt)
print("hashed_password: ", hashed_password.decode("utf-8"))


def check_pw(input_password):
    stored_password = b"$2b$12$T3ut5wCszsrRw87k7CCNTuQ5a1diMUtgtbORKFxy5Y2wIth5WFlgO"
    return bcrypt.checkpw(input_password.encode("utf-8"), stored_password)


if __name__ == "__main__":
    print(check_pw("admin123"))
    print(check_pw("admin1234"))
