from django.contrib import admin

# Register your models here.
from user.models import User


class UserAdmin(admin.TabularInline):
    model = User


@admin.register(User)
class RegionAdmin(admin.ModelAdmin):
    # 设置每页显示多少条
    list_per_page = 5
    # 设置控制工具的位置
    actions_on_bottom = False
    actions_on_top = True

    # # 设置显示的字段
    # list_display = ['id', 'phone', "nickname", "head_photo" ,"add_time"]

    # # 设置字段链接
    # list_display_links = ['id', 'phone', "nickname", "add_time"]

    # 右侧过滤
    list_filter = ['username']

    # 设置搜索的字段
    search_fields = ['username']

    # 自定义编辑显示
    # fields = ['name',"parent"]
    # fieldsets = (
    #     ("基本信息", {"fields": ("username",)}),
    #     ("详细信息", {"fields": ("username",)})
    # )
