from django.conf.urls import url

from user.views import (LoginView,
                        RegView,
                        ForgetpasswordView,
                        MemberView,
                        quit,
                        InfoView,
                        )

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name="登陆页面"),
    url(r'^reg/', RegView.as_view(), name="注册页面"),
    url(r'^forgetpassword/', ForgetpasswordView.as_view(), name="忘记密码页面"),
    url(r'^member/', MemberView.as_view(), name="个人中心"),
    url(r'^quit/', quit, name="安全退出"),
    url(r'^info/', InfoView.as_view(), name="个人资料")
]
