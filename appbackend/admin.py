from django.contrib import admin
from appbackend.models import Book
from appbackend.models import Users
# from appbackend.models import FriendsList
from appbackend.models import EmailVerifyCode

# Register your models here

admin.site.register(Book)
# admin.site.register(FriendsList)
admin.site.register(EmailVerifyCode)


class UsersAdmin(admin.ModelAdmin):
    list_display = 'user_name', 'first_name', 'last_name', 'date_of_birth'


admin.site.register(Users, UsersAdmin)


# 定义Admin管理类
# class UsersAdmin(object):
#     # 制定action
#     # actions = [MyAction, ]
#
#     # options选项：
#     # 1. 注册用户列表页都显示哪些字段
#     list_display = ('user_name', 'company', 'create_time', 'isdelete', 'email')
#
#     # 2. 列表页过滤器
#     list_filter = ('company', 'isdelete', 'create_time')
#
#     # 3. 列表页每页显示几个
#     list_per_page = 20
#
#     # 4. 注意search_fields里不能出现以时间定义的字段，如Date，DateTime等
#     search_fields = ['user_name', 'email', 'company', 'phone']
#
#     # 5. 这些字段可以点击显示详细信息
#     show_detail_fields = ['user_name']
#
#     # 6. 这些字段可以在列表页即时数据编辑，不用进change页面去编辑，ajax无刷新
#     list_editable = ['isdelete']
#
#     # 7. change页只能读取不能更改的数据
#     # readonly_fields = ['user_name']
