from django import forms
from django.forms import ModelForm
from .models import homepost
import time

# Create a homepost form
class homepostForm(ModelForm):
    class Meta: 
        model = homepost
        fields = (
            'postname', 
            'introduction', 
            #'writer',
            'website',
            'post_date',
        )
        
        labels = {
            'postname': '',  # 'Enter your postname',
            'introduction': '',  # 'Introduction',
            #'writer': '',  # 'Writer',
            'website': '',  # 'Website',
            'post_date': '',  # 'Post Date',
        } 
        
        widgets = {
            'postname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Enter your postname'}),         
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Introduction'}),
            #'writer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Writer'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'post_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Post Date'}),
        }
