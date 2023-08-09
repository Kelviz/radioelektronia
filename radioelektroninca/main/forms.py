from .models import Order
from django.forms import ModelForm, TextInput, Textarea

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name","email","subject","text"]
        widgets = {
            "name": TextInput(attrs={
                "class": "KvoMHf has-custom-focus wixui-text-input__input",
                "placeholder":"Введите свое имя"
            }),
            "email": TextInput(attrs={
                "class": "KvoMHf has-custom-focus wixui-text-input__input",
                "placeholder":"Добавьте эл. почту"
            }),
            "subject": TextInput(attrs={
                "class": "KvoMHf has-custom-focus wixui-text-input__input",
                "placeholder":"Укажите тему"
            }),
            "text": Textarea(attrs={
                "class": "rEindN has-custom-focus wixui-text-box__input",
                "placeholder":"Добавьте сообщение..."
            })
        }