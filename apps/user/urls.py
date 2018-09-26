from django.conf.urls import url

from user.views import (LoginView,
                        RegView,
                        ForgetpasswordView,
                        MemberView,
                        quit,
                        InfoView,
                        Gladdress,
                        Saftystep,
                        Money,
                        authCodeView,
                        head_photo)

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name="登陆页面"),
    url(r'^reg/', RegView.as_view(), name="注册页面"),
    url(r'^forgetpassword/', ForgetpasswordView.as_view(), name="忘记密码页面"),
    url(r'^member/', MemberView.as_view(), name="个人中心"),
    url(r'^quit/', quit, name="安全退出"),
    url(r'^info/', InfoView.as_view(), name="个人资料"),
    url(r'^gladdress/', Gladdress.as_view(), name="收货地址"),
    url(r'^saftystep/', Saftystep.as_view(), name="安全设置"),
    url(r'^money/', Money.as_view(), name="我的钱包"),
    url(r'^authCodeView/', authCodeView.as_view(), name="登陆验证"),
    url(r'^head_photo/', head_photo, name="图片上传"),

]
