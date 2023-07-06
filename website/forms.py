from .models import Order
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("phone_number", "comment")
        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width:400px; max-height:300px;",
                    "placeholder": "Siz istayotgan mahsulot haqida ma'lumot bering",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width:400px;",
                    "placeholder": "Teleforn Raqam",
                }
            ),
        }
