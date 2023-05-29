from distutils.command import clean
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render

from student.models import Student
from student.forms import StudentForm
from django.urls import reverse

# Create your views here.


# 请求request是Django对用户发送过来的HTTP请求的封装
def index(request):
    # 从数据库查出的数据拿来填充
    students = Student.get_all()

    # 如果是POST请求,则先验证表单后向数据库写入
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
