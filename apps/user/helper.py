import hashlib

from django.shortcuts import redirect
from django.urls import reverse

from Supermarket import settings


def set_password(pwd):
    # 密码加密
    token = settings.SECRET_KEY
    password = pwd + token
    h = hashlib.md5(password.encode("utf-8"))
    return h.hexdigest()


def verify_login_required(func):
    def verify_login(request, *args, **kwargs):
        if request.session.get("ID") is None:
            return redirect(reverse("user:登陆页面"))
        return func(request, *args, **kwargs)

    return verify_login

