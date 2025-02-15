from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserDetail




class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=254,help_text='Required .Imform a valid email address.')

    class Meta:
        model=User
        fields =('username','email','password1','password2')





class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['firstname', 'lastname', 'contact', 'address','profile_photo']


class LoginForm(AuthenticationForm):
    pass  # Uses default Django authentication form

class ChangePasswordForm(PasswordChangeForm):
    pass  # Uses default Django password change form

