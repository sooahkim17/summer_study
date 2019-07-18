from django import forms
from .models import Board,Comment
from django.forms import ModelForm
from django.contrib.auth.models import User

class BoardForm(forms.ModelForm):
    class Meta:
        model=Board
        fields=['title','body']

#회원가입
class SignupForm(ModelForm):
    password_check=forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order=['username','password','password_check','last_name','first_name','email']
    class Meta:
        model=User
        widgets={'password':forms.PasswordInput}
        fields=['username','password','last_name','first_name','email']

#로그인
class SigninForm(ModelForm): 
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields= ['username','password']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label="댓글"
