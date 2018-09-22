import os

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from Supermarket.settings import BASE_DIR
from user.forms import UserForm, UserModelForm
from user.models import User


class LoginView(View):
    # 登陆界面
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # 获取数据
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        if all((phone, password)):
            # 用户输入了数据
            # 将数据拿到数据库进行比对
            x = User.objects.filter(phone=phone).first()
            if password == x.password:
                # 验证通过
                # 设置sesson
                request.session['phone'] = phone
                request.session.set_expiry(0)
                url = reverse("user:个人中心")
                return redirect(url)
            else:
                # 验证不通过
                context = {
                    "errors": "账号或密码错误,请重新输入"
                }
                return render(request, "user/login.html", context)
        else:
            # 用户没有输入数据
            context = {
                "errors": "请输入手机号或密码"
            }
            return render(request, "user/login.html", context)


class RegView(View):
    # 注册界面
    def get(self, request):
        return render(request, "user/reg.html")

    def post(self, request):
        # 完成注册
        # 接收数据
        data = request.POST
        form = UserForm(data)  # 实例化对象
        if form.is_valid():
            # 参数合法
            # 获取值
            data = form.cleaned_data
            phone = data.get('phone')

            print(str)
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
            print(form)
            return render(request, "user/reg.html", context)


class ForgetpasswordView(View):
    # 忘记密码
    def get(self, request):
        return render(request, "user/forgetpassword.html")

    def post(self, request):
        pass


class MemberView(View):
    # 个人中心
    def get(self, request):
        # 获取session,根据键读取值
        phone = request.session.get("phone", 0)
        if phone:
            # 有session传过来
            # 根据username获取参数
            data = User.objects.filter(phone=phone).first()
            context = {
                "data": data,
            }
            return render(request, "user/member.html", context)
        else:
            # 没有session,跳转到登陆页面
            return render(request, "user/login.html")

    def post(self, request):
        pass


def quit(request):
    # 安全退出
    # 清除session
    request.session.flush()
    url = reverse("user:登陆页面")
    return redirect(url)


class InfoView(View):
    def get(self, request):
        # 获取session值
        phone = request.session.get("phone")
        data = User.objects.filter(phone=phone)
        form = UserModelForm(data)
        context = {
            "form": form
        }
        return render(request, "user/infor.html")

    def post(self, request):
        pass
