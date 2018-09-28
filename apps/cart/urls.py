from django.conf.urls import url

from cart.views import AddGoodsView, DelGoodsView, ShopCartView

urlpatterns = [
    url(r'^AddGoods', AddGoodsView.as_view(), name="增加商品"),
    url(r'^DelGoods', DelGoodsView.as_view(), name="删除商品"),
    url(r'^ShopCart', ShopCartView.as_view(), name="购物车"),

]
