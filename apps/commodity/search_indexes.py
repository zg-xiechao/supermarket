# 导入全文检索框架索引类
from haystack import indexes

from commodity.models import GoodsSku


class GoodSKUSearchIndex(indexes.SearchIndex, indexes.Indexable):
    # 设置需要检索的主要字段内容 use_template表示字段内容在模板中
    text = indexes.CharField(document=True, use_template=True)

    # 获取检索对应的模型
    def get_model(self):
        return GoodsSku

    # 设置检索需要使用的查询集
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
