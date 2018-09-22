from django import forms
from django.core import validators

from user.models import User


# 登录表单
class UserForm(forms.Form):
    phone = forms.CharField(
        error_messages={
            "required": "请填写手机号",
            # "unique": "手机号已注册"
        },

        validators=[
            validators.RegexValidator(r'^1[3,9]\d{9}$', "手机号格式不正确")
        ])
    password1 = forms.CharField(max_length=16, min_length=6, error_messages={
        "required": "请填写密码",
        "max_length": "密码不能大于16位",
        "min_length": "密码不能小于6位"
    })
    password2 = forms.CharField(max_length=16, min_length=6, error_messages={
        "required": "请填写密码",
        "max_length": "密码不能大于16位",
        "min_length": "密码不能小于6位"
    })

    # 验证手机号是否注册
    def clean_phone(self):
        # 获取用户输入的电话号码
        phone = self.cleaned_data.get("phone")
        num = User.objects.filter(phone=phone).exists()
        # if len(num) == 1:
        #     raise forms.ValidationError({"phone": "手机号已经注册"})
        # else:
        #     return phone
        rs = User.objects.filter(phone=phone).exists()
        if rs:
            raise forms.ValidationError("该手机号码已经被注册!")
        return phone

    def clean(self):
        # 验证两次密码是否一致
        # 获取数据
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError({"password2": "两次密码不一致"})
        else:
            return self.cleaned_data


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["add_time", "Modify_time", "is_delete", "username"]
