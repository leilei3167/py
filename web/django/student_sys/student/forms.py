import profile
from django import forms
from .models import Student


# 此处定义表单,

# 手动定义表单
# class StudentForm(forms.ModelForm):
#     name = forms.CharField(label="姓名", max_length=128)
#     sex = forms.ChoiceField(label="性别", choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label="职业", max_length=128)
#     email = forms.EmailField(label="Email", max_length=128)
#     qq = forms.CharField(label="QQ", max_length=128)
#     phone = forms.CharField(label="电话", max_length=128)


# 如果form和model的定义很类似,实际上也可以复用model的定义,不需要向上面一样重复定义很多字段
class StudentForm(forms.ModelForm):
    # 对于某个字段的个性化定制,可以在此处定义,clean_xxx,如clean_phone
    def clean_qq(self):
        # clean_qq是clean_字段名的特殊方法,用于对单个字段进行数据清洗
        # 通过cleaned_data获取用户提交的数据
        cleaned_data = self.cleaned_data["qq"]
        # 判断是否全是数字
        if not cleaned_data.isdigit():
            raise forms.ValidationError("必须是数字!")
        # 返回清洗后的数据
        return int(cleaned_data)

    class Meta:
        model = Student
        # 需要验证的字段
        fields = ("name", "sex", "profession", "email", "qq", "phone")
