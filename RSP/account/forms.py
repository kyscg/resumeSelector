from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields

from .models import User, Document


class UploadResumeForm(UserChangeForm):
    # pdf_resume = forms.FileField(
    #     widget=forms.FileInput(
    #         attrs={
    #             'class':'form-control',
    #         }
    #     )
    # )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'pdf_resume',
            'password'
        )


class EditUserProfileForm(UserChangeForm):
    

    class Meta:
        model = User
        fields = (
            'username', 
            'password', 
            'email', 
            'is_applicant', 
            'is_recruiter', 
            # 'pdf_resume',
        )




class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control dark',

            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',

            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                
            }
        )
    )
    skills = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'data-role' : 'tagsinput'
                
            }
        )
    )
    accept_t_n_c = forms.BooleanField(required = True)
    #     attrs={
    #         'Required':
            
    #     }
    # )

    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'password1', 
            'password2', 
            'is_recruiter', 
            'is_applicant', 
            'gender',
            'skills',
            'accept_t_n_c'
        )


class QueryForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control dark',

            }
        )
    )