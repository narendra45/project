from django import forms
from product.models import ProductDetails,Tags

class ProductForms(forms.ModelForm):
    #
    # product_name=forms.CharField(max_length=30)
    # tags=forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple)
    # image = forms.ImageField()
    #
    # CATEGORY_CHOICES = (
    #     ('M', 'mobile'),
    #     ('T', 'tv'),
    #     ('G','grocery')
    # )
    # category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model=ProductDetails
        fields=['product_name','tags','image','category']
