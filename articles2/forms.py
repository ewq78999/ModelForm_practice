from django import forms
from .models import Article2

class Article2Form(forms.ModelForm):

        class Meta:
                model = Article2
                fields = '__all__'