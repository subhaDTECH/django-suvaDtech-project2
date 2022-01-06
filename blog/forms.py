from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import post


class SignupForm(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="password (again)",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        lebels={'username':'Name','fisrt_name':"First_Name",'last_name':'Last_Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
        
        }

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))      

class PostForm(forms.ModelForm):
    class Meta:
        model=post 
        fields={'id','title','desc'}
        lables={'title':'Title','desc':"DESC"}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.TextInput(attrs={'class':'form-control'})
        
        }

