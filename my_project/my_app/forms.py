from typing import Any, List
from django.forms import ModelForm
from .models import Product
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="Remember me for session")
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "remember_me",
        )

    
class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "is_staff",
        )
    
    def save(self, commit: bool = True) -> Any:
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        
        return user
    
class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = []
        

ProductFormSet = modelformset_factory(Product, exclude=["id",])