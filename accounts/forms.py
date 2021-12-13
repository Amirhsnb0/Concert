from django import forms
from django.forms import fields
from accounts.models import PorfileModel
from django.contrib.auth.forms import UserChangeForm

class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model=PorfileModel
        fields=['Profleimage','credit','status']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=PorfileModel
        fields=['Profleimage','credit','status']

class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields=["first_name","last_name","email"]
    password=None