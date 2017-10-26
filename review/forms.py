from django import forms

from .models import Company_Reviews

class PostForm(forms.ModelForm):

    class Meta:
        model = Company_Reviews
        fields = ('companykey','title','review',)