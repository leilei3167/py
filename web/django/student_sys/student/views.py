from distutils.command import clean
from multiprocessing import context
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from student.models import Student
from student.forms import StudentForm
from django.urls import reverse

# Create your views here.


# function view的形式
# 请求request是Django对用户发送过来的HTTP请求的封装
def index(request):
    # 从数据库查出的数据拿来填充
    students = Student.get_all()

    # 如果是POST请求,则先验证表单后向数据库写入,更推荐class-based view,将处理逻辑放在类中
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # # form_cleaned_data是一个字典,包含了用户提交的所有合法数据
            # cleaned_data = form.cleaned_data
            # # 手动构建model
            # student = Student()
            # student.name = cleaned_data["name"]
            # student.sex = cleaned_data["sex"]
            # student.profession = cleaned_data["profession"]
            # student.email = cleaned_data["email"]
            # student.qq = cleaned_data["qq"]
            # student.phone = cleaned_data["phone"]
            # student.save()

            # 由于我们form和model的字段是一一对应的,所以可以直接使用以下方法
            form.save()

            return HttpResponseRedirect(reverse("index"))
    else:
        # get请求,展示表单
        form = StudentForm()

    context = {
        "students": students,
        "form": form,
    }

    # template将会在/templates目录下寻找index.html文件
    return render(request, "index.html", context)


# class view的形式
# 注意,继承自View,在urls.py中需要使用as_view()方法来将类转换为函数
class IndexView(View):
    """
    这样代码更具组织性,不同的HTTP方法现在由同一类的不同方法来处理
    """

    template_name = "index.html"

    def get_context(self):
        students = Student.get_all()
        context = {
            "students": students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        # get请求,没有form表单
        form = StudentForm()
        context.update({"form": form})

        return render(request, self.template_name, context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            # 直接存入数据库,后直接重定向至index路由器(urls中定义)
            form.save()
            return HttpResponseRedirect(reverse("index"))
        context = self.get_context()
        context.update({"form": form})
        return render(request, self.template_name, context)
