from django import forms
from commodity.models import GoodsSku


class Search(forms.ModelForm):
    class Meta:
        model = GoodsSku

