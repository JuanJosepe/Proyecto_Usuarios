from django.shortcuts import render

from applications.users.forms import UserRegisterForm
from django.views.generic import(
    CreateView
)

class UserRegisterView(CreateView): 
    template_name = 'users/register.html'
    
    form_class = UserRegisterForm
    
    success_url = '/'