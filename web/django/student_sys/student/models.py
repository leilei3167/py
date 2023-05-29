import email
from django.db import models


# Create your models here.
class Student(models.Model):
    # 定义了choices的字段,在admin页面自动展示(调用get_status_display()方法),而我们自己的模板需要在模板中手动调用此方法
    SEX_ITEMS = [
        (1, "男"),
        (2, "女"),
        (0, "未知"),
    ]
    STATUS_ITEMS = [
        (0, "申请"),
        (1, "通过"),
        (2, "拒绝"),
    ]

    # 字段
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态")
    created_time = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="创建时间"
    )

    # 定义了一个类方法,用于获取所有的学生信息,后续可以直接使用Student.get_all()来获取所有学生信息
    # 这里可以自定义逻辑,如默认返回所有已通过审核的学生信息
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @property
    def sex_show(self):
        # 返回性别的中文表示而不是数值
        return dict(self.SEX_ITEMS)[self.sex]

    def __str__(self) -> str:
        return "<Student: {}>".format(self.name)

    # 展示在admin页面的名称
    class Meta:
        verbose_name = verbose_name_plural = "学员信息"
