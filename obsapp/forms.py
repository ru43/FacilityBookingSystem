from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
