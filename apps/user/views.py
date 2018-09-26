import os
import re
import random
from os.path import join

from django import forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from Supermarket.settings import BASE_DIR
from user.forms import UserForm, LoginForm, InfoForm
from user.helper import verify_login_required
from user.models import User


class LoginView(View):
    # 登陆界面
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            # 获取用户信息
            user = form.cleaned_data.get("user")
            # 发送session
            request.session['ID'] = user.pk
            request.session['phone'] = user.phone
            # 设置有效期, 关闭浏览器就 重新登录
            request.session.set_expiry(0)
            return redirect(reverse("user:个人中心"))
        return render(request, "user/login.html", {"form": form})
        # 获取数据
        # phone = request.POST.get("phone")
        # password = request.POST.get("password")
        # if all((phone, password)):
        #     # 用户输入了数据
        #     # 将数据拿到数据库进行比对
        #     x = User.objects.filter(phone=phone).first()
        #     if password == x.password:
        #         # 验证通过
        #         # 设置sesson
        #         request.session['phone'] = phone
        #         request.session.set_expiry(0)
        #         url = reverse("user:个人中心")
        #         return redirect(url)
        #     else:
        #         # 验证不通过
        #         context = {
        #             "errors": "账号或密码错误,请重新输入"
        #         }
        #         return render(request, "user/login.html", context)
        # else:
        #     # 用户没有输入数据
        #     context = {
        #         "errors": "请输入手机号或密码"
        #     }
        # return render(request, "user/login.html")


class RegView(View):
    # 注册界面
    def get(self, request):
        form = UserForm()
        return render(request, "user/reg.html", {"form": form})

    def post(self, request):
        session_code = request.session.get('random_code')
        # 强制转换成真正的字典
        print(session_code)
        data = request.POST.dict()
        data['session_code'] = session_code
        # 2. 处理数据
        form = UserForm(data)
        # code = data.cleaned_data.get("verify_code")
        print(form)
        if form.is_valid():
            # 参数合法
            # 获取值
            data = form.cleaned_data
            phone = data.get('phone')
            password = data.get('password1')
            # 写入数据
            User.objects.create(phone=phone, password=password)
            url = reverse("user:登陆页面")
            return redirect(url)
        else:
            # 参数不合法
            # 获取错误信息
            context = {
                "form": form
            }
            return render(request, "user/reg.html", context)


class ForgetpasswordView(View):
    # 忘记密码
    def get(self, request):
        return render(request, "user/forgetpassword.html")

    def post(self, request):
        pass


class MemberView(View):
    # 个人中心
    # @method_decorator(verify_login_required)
    def get(self, request):
        # # 获取session,根据键读取值
        # phone = request.session.get("phone", 0)
        # if phone:
        #     # 有session传过来
        #     # 根据username获取参数
        phone = request.session.get("phone")
        # 根据phone获取用户信息
        data = User.objects.filter(phone=phone).first()
        context = {
            "data": data,
        }
        return render(request, "user/member.html", context)

    # else:
    #     # 没有session,跳转到登陆页面
    #     return render(request, "user/login.html")

    def post(self, request):
        pass

    @method_decorator(verify_login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def quit(request):
    # 安全退出
    # 清除session
    request.session.flush()
    url = reverse("user:登陆页面")
    return redirect(url)


# 个人资料  性别回显未完成
class InfoView(View):
    def get(self, request):
        # 获取session值
        id = request.session.get("ID")
        user = User.objects.filter(id=id).first()
        form = InfoForm(instance=user)
        context = {
            "form": form,
            "user": user
        }
        return render(request, "user/infor.html", context)

    def post(self, request):
        # 获取session中的参数
        id = request.session.get("ID")
        # 接收用户修改的数据
        data = request.POST
        # form = InfoForm(data)
        # if form.is_valid():
        nickname = data.get("nickname")
        gender = data.get("gender")
        birthday = data.get("birthday")
        school = data.get("school")
        location = data.get("location")
        hometown = data.get("hometown")
        phone = data.get("phone")
        # 将参数修改到数据库  这里需要判断用户修改了哪些吗
        User.objects.filter(id=id).update(
            nickname=nickname,
            gender=gender,
            birthday=birthday,
            school=school,
            location=location,
            hometown=hometown,
            phone=phone
        )
        return redirect(reverse("user:个人资料"))


# 头像上传

@csrf_exempt
def head_photo(request):
    if request.method == "POST":
        # 接收用户id
        id = request.session.get("ID")
        user = User.objects.filter(id=id)
        user.head_photo = request.FILES["file"]
        user.save()

        return JsonResponse({"error": 0})
    else:
        return JsonResponse({"error": 1})


# 收货地址
class Gladdress(View):
    def get(self, request):
        return render(request, "user/gladdress.html")

    def post(self, request):
        pass


# 安全设置
class Saftystep(View):
    def get(self, request):
        return render(request, "user/saftystep.html")

    def post(self, request):
        pass


class Money(View):
    def get(self, request):
        return render(request, "user/money.html")

    def post(self, request):
        pass


# 验证码
class authCodeView(View):
    # def get(self, request):
    #     pass

    def post(self, request):
        # 1. 接收参数
        #     1.1 接收用户手机号
        data = request.POST
        phone = data.get("phone", "")
        # 2.处理参数
        #     2.1 验证手机号格式是否正确
        phone_re = re.compile("^1[3-9]\d{9}$")
        res = re.search(phone_re, phone)
        if res is None:
            # 手机号码格式错误
            return JsonResponse({"ststic": 100, "mes": "手机号码格式错误"})
        #     2.2 验证手机号是否已经注册
        #         根据手机号查询用户信息
        user = User.objects.filter(phone=phone).exists()
        if user:
            # 手机号已经注册
            return JsonResponse({"static": 300, "mes": "手机号已经注册"})
        # 设置一个随机值
        random_code = "".join([str(random.randint(0, 9)) for _ in range(4)])
        print(random_code)
        # 把验证码保存到session中
        request.session['random_code'] = random_code
        request.session.set_expiry(60)
        # 3. 响应 json , 告知 ajax是否发送成功
        return JsonResponse({"status": "200"})
        # 3.响应  是用json格式进行响应
