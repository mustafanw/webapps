from django import forms
from .models import Products


class ProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('product_url','affiliate_tag')
        labels = {
            'product_url':'Product URL',
            'affiliate_tag':'Affiliate Tag'
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
