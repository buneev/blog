from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','text','pub_date', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

