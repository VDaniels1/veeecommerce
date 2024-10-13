from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'name':'username',
            'id':'username',
            'placeholder':'Enter Your username',
            'class':'form-group',
            'type':'text'
        })
        self.fields["last_name"].widget.attrs.update({
            'name':'lastname',
            'id':'lastname',
            'placeholder':'Enter Your lastname',
            'class':'form-group',
            'type':'text'
        })
        self.fields["password1"].widget.attrs.update({
            'name':'password',
            'id':'password',
            'placeholder':'Enter Your password',
            'class':'form-group',
            'type':'text'
        })
        self.fields["first_name"].widget.attrs.update({
            'name':'firstname',
            'id':'firstname',
            'placeholder':'Enter Your firstname',
            'class':'form-group',
            'type':'text'
        })
        self.fields["password2"].widget.attrs.update({
            'name':'password',
            'id':'password',
            'placeholder':'Confirm Your password',
            'class':'form-group',
            'type':'text'   
        })
        self.fields["email"].widget.attrs.update({
            'name':'email',
            'id':'email',
            'placeholder':'Enter Your Email',
            'class':'form-group',
            'type':'text'   
        })
        
        

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
