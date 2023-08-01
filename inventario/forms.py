from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
        class Meta:
            model = Productos
            fields = ("nombre","precio","stock","categoria","origen")

# class OrigenForm(forms.ModelForm):
#         class Meta:
#             model=Origen
#             fields= ['origen']
        
#         def __init_subclass__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)

            
#             self.fields['origen'].widget.attrs.update({
#                 'class':'form-control',
#             })