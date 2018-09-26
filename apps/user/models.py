from django.core import validators
from django.db import models


# Create your models here.
# 冗余继承表
class BoseModel(models.Model):
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")
    Modify_time = models.DateField(auto_now=True, verbose_name="修改时间")
    is_delete = models.BooleanField(default=0, verbose_name="是否删除")  # 0为未删除 1为删除

    class Meta:
        abstract = True


# 个人资料回显
class User(BoseModel):
    # 性别选项
    sex_choices = (
        (1, "男"),
        (2, "女"),
        (3, "保密"),
    )
    username = models.CharField(max_length=16, validators=[validators.MinLengthValidator(6)], verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    phone = models.CharField(max_length=11, verbose_name="手机号")
    nickname = models.CharField(max_length=16, null=True, blank=True, verbose_name="昵称")
    # 默认1为男 2为女 3为保密
    gender = models.SmallIntegerField(choices=sex_choices, default=3, verbose_name="性别")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    school = models.CharField(max_length=50, null=True, blank=True, verbose_name="学校")
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name="位置")
    hometown = models.CharField(max_length=255, null=True, blank=True, verbose_name="故乡")
    head_photo = models.ImageField(upload_to="user/%Y%m/%d", default="user/infortx.png", verbose_name="用户头像")



