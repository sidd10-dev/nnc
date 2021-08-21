from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import TextInput, Textarea
from .models import *

class UserForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ('username','email','password1','password2')
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs= {
            'class': "u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white",
            'placeholder': "Enter an Username",
            'id':"name-e91f",
            'name':"usernameda"
        }
    ))
    email = forms.CharField(max_length=50, required=True, widget = forms.TextInput(
        attrs = {
            'class':"u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white",
            'name':"email",
            'id':"email-e91f",
            'placeholder':"Enter a valid email address",
            'type':"email"
        }
    ))
    password1 = forms.CharField(required=True, widget = forms.PasswordInput(
        attrs= {
            'placeholder':"Enter a password",
            'id':"text-e114",
            'name':"pass1",
            'class':"u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white"
        }
    ))
    password2 = forms.CharField(required=True, widget = forms.PasswordInput(
        attrs= {
            'placeholder':"Confirm Password",
            'id':"text-e114",
            'name':"pass1",
            'class':"u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white"
        }
    ))

class CustomerForm(forms.Form):
    address = forms.CharField(required=True, widget = forms.Textarea(
        attrs= {
            'rows':"4",
            'cols':"50",
            'id':"textarea-6b48",
            'name':"address",
            'class':"u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white",
            'placeholder':'Enter Delivery Address'
        }
    ))
    phone_no = forms.CharField(required = True, widget= forms.TextInput(
        attrs = {
            'pattern':"\+?\d{0,3}[\s\(\-]?([0-9]{2,3})[\s\)\-]?([\s\-]?)([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?([0-9]{2})",
            'placeholder':"Enter your phone number",
            'id':"phone-d55a",
            'name':"phone",
            'class':"u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white"
        }
    ))

class Loginform(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(
        attrs = {
            'placeholder':"Enter Username",
            'id':"name-e91f",
            'name':"usernameda",
            'class':"u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white",
            'required':"required"
            }))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'placeholder':"Enter Password",
            'id':"text-6e34",
            'name':"passwordda",
            'class':"u-border-1 u-border-grey-30 u-custom-font u-font-montserrat u-input u-input-rectangle u-radius-17 u-white",
            'required':"required"
            }))
        