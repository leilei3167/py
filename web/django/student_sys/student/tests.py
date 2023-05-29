from http import client
from django.test import TestCase, Client
from student.models import Student

# Create your tests here.


# 继承测试类,这样会获得一些Django提供的测试方法,如assertEqual,assertIsNone等
class StudentTestCase(TestCase):
    """
    分为:
    1.model层的测试,主要是测试model的属性和方法是否正确,保证数据的写入和查询是可用的,并且在这一层提供的
    方法是符合预期的
    2.view层的测试,这一部分是需要重点关注的,因为view层是主要的核心业务逻辑所在的层,但很多时候往往没有那么
    多时间来编写测试,但是应该始终确保view层的测试是完整的,这样才能保证我们的业务逻辑是正确的,这一部分需要
    引入自动化测试的逻辑,因为api往往会有成百上千个,需要用到Django的Client类来模拟请求,然后对返回的结果进行
    断言
    """

    # 每个测试方法执行前都会执行setUp方法和tearDown方法,可以理解为每个测试方法都是一个独立的环境
    # 用来初始化环境和数据,每个测试方法执行前都会执行setUp方法
    def setUp(self) -> None:
        Student.objects.create(
            name="the5fire",
            sex=1,
            email="djias@163.com",
            profession="程序员",
            qq="333",
            phone="222",
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name="huyang",
            sex=1,
            email="dsaji@djsa.com",
            profession="程序员",
            qq="333",
            phone="248522",
        )
        # 由于我们对sex字段创建时指定了choices,因此此处可以直接使用get_sex_display方法而不是sex_show
        self.assertEqual(student.sex_show, "男", "性别字段内容跟展示不一致")

    def test_filter(self):
        Student.objects.create(
            name="huyang",
            sex=1,
            email="dsaji@dd.com",
            profession="程序员",
            qq="3333",
            phone="222",
        )
        name = "the5fire"
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, "应该只存在一个名称为{}的记录".format(name))

    # ---------------------view层测试----------------------------
    def test_get_index(self):
        # 测试首页可用性
        client = Client()
        response = client.get("/")
        # 断言首页状态码为200
        self.assertEqual(response.status_code, 200, "status code must be 200!")

    def test_post_student(self):
        client = Client()
        # post请求的form表单数据
        data = dict(
            name="test_for_post",
            sex=1,
            email="djisa@jdisa.com",
            profession="程序员",
            qq="333",
            phone="4563",
            status=0,
        )
        response = client.post("/", data)
        # 写入成功会重定向到首页,因此状态码为302
        self.assertEqual(response.status_code, 302, "status code must be 302!")

        # 断言首页是否包含我们提交的数据
        response = client.get("/")
        self.assertTrue(
            b"test_for_post" in response.content,
            "response content must contain 'test_for_post'",
        )
