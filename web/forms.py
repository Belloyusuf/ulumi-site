from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from .models import Comment, News



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')
        help_texts = {
            'message': 'We like to hear form you'
        }
        widgets ={
            'name':widgets.TextInput(attrs={
                'class':'form-control col-sm-15',
                'placeholder':'Your name'
            }),

             'email':widgets.EmailInput(attrs={
                'class':'form-control col-sm-15',
                'placeholder':'example@gmail.com'
            }),

            'message':widgets.Textarea(attrs={
                'class':'form-control col-md-15',
                'rows':3,
            })

        }
       