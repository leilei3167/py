from django.contrib import admin

# Register your models here.
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "sex",
        "profession",
        "email",
        "qq",
        "phone",
        "status",
        "created_time",
    )
    # 定义admin右侧的过滤器,性别,状态,创建时间
    list_filter = ("sex", "status", "created_time")
    search_fields = ("name", "profession")
    #  调整创建学员信息时, 以特定的形式展示
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    ("sex", "profession"),
                    ("email", "qq", "phone"),
                    "status",
                )
            },
        ),
    )


admin.site.register(Student, StudentAdmin)
