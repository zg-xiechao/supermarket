from django import forms
from django.core import validators

from user.helper import set_password
from user.models import User


# 注册表单
class UserForm(forms.Form):
    phone = forms.CharField(
        error_messages={
            "required": "请填写手机号",
            # "unique": "手机号已注册"
        }

        # validators=[
        #     validators.RegexValidator(r'^1[3,9]\d{9}$', "手机号格式不正确")
        # ]
    )
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
    verify_code = forms.CharField(required=True,
                                  error_messages={
                                      "required": "请填写验证码!"
                                  },
                                  widget=forms.TextInput(attrs={"class": "reg-yzm", "placeholder": "输入验证码"})
                                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 验证手机号码是否正确
        self.fields["phone"].validators.append(validators.RegexValidator(r'^1[3,9]\d{9}$', "手机号格式不正确"))

    # 验证手机号是否注册
    def clean_phone(self):
        # 获取用户输入的电话号码
        phone = self.cleaned_data.get("phone")
        # num = User.objects.filter(phone=phone).exists()
        # if len(num) == 1:
        #     raise forms.ValidationError({"phone": "手机号已经注册"})
        # else:
        #     return phone
        rs = User.objects.filter(phone=phone).exists()
        if rs:
            raise forms.ValidationError("该手机号码已经被注册!")
        return phone

    def clean_verify_code(self):
        # self.cleaned_data.get('verify_code')
        # 获取用户提交的验证码
        verify_code = self.cleaned_data.get('verify_code')
        # 获取原始数据中保存的session验证码
        session_code = self.data.get('session_code')
        if verify_code != session_code:
            raise forms.ValidationError("验证码错误!")
        return verify_code

    def clean(self):
        # 验证两次密码是否一致
        # 获取数据
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError({"password2": "两次密码不一致"})
        else:
            # 两次密码验证一致,对密码进行加密
            if password1:
                cleaned_data['password1'] = set_password(password1)
                return cleaned_data


# 登陆表单验证
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone", "password"]

        error_messages = {
            "phone": {
                "required": "请输入手机号"
            },
            "password": {
                "required": "请输入密码"
            }
        }

    def clean(self):
        # 验证手机号和密码是否正确
        # 获取用户输入的信息
        cleaned_data = super(LoginForm, self).clean()
        phone = cleaned_data.get("phone")
        password = cleaned_data.get("password")
        # 根据输入的信息查询数据库
        user = User.objects.filter(phone=phone).first()
        if user is None:
            raise forms.ValidationError({"phone": "该用户没有注册"})
        else:
            password_in_db = user.password
            password = set_password(password)
            if password_in_db == password:
                cleaned_data["user"] = user
                return cleaned_data
            else:
                raise forms.ValidationError({"password": "密码不正确"})


# 个人资料表单
class InfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["head_photo", "nickname", "gender", "birthday", "school", "location", "hometown", "phone"]
        # 渲染表单
        widgets = {
            # "head_photo": forms.ImageField(),
            "nickname": forms.TextInput(attrs={"class": "infor-tele", "placeholder": "请输入昵称"}),
            "birthday": forms.DateInput(attrs={"class": "infor-tele", 'type': "date", "placeholder": "出生日期"}),
            "gender": forms.RadioSelect(),
            "school": forms.TextInput(attrs={"class": "infor-tele", "placeholder": "就读于哪个学校"}),
            "location": forms.TextInput(attrs={"class": "infor-tele", "placeholder": "详细地址"}),
            "hometown": forms.TextInput(attrs={"class": "infor-tele", "placeholder": "来自哪里"}),
            "phone": forms.TextInput(attrs={"class": "infor-tele", "placeholder": "手机号码"}),
        }

