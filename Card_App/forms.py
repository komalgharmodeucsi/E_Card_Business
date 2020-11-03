from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Design
#from django import forms
#from .models import Image
#class PersonForm(forms.ModelForm):
 #   class Meta:
  #      model= Person
   #     fields= ["pr_name", "pr_lastname", "address", "mob_no", "email","password", "confirm_password"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class DesignForm(forms.ModelForm):
    class Meta:
        model= Design
        fields= ["name", "id", "image"]
