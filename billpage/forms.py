from django import forms 
from billpage.models import Buyproduct

class BuyproductForm(forms.ModelForm):    
    class Meta:
        model = Buyproduct
        fields="__all__"