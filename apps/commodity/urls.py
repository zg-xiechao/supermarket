from django.conf.urls import url

from commodity.views import (Category,
                             SlideShowView,
                             DetailView,
                             IndexView,
                             VillageView,)

urlpatterns = [
    url(r'^SlideShowView/', SlideShowView.as_view(), name="轮播"),
    url(r'^Category/(?P<cate_id>\d+)_(?P<order>\d+)', Category.as_view(), name="超市"),
    url(r'^detail/(?P<id>\d+)', DetailView.as_view(), name="详情"),
    url(r'^index/', IndexView.as_view(), name="首页"),
    url(r'^Village/', VillageView.as_view(), name="首页搜索"),
]
