from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from core.forms import BootstrapFormMixin
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    pass
    # user = None
    # email = forms.EmailField(
    # )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(),
    # )

    # def clean_password(self):
    #     self.user = authenticate(
    #         email=self.cleaned_data['email'],
    #         password=self.cleaned_data['password'],
    #     )
    #
    #     if not self.user:
    #         raise ValidationError('Email and/or password incorrect')
    #
    # def save(self):
    #     return self.user


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', )
