from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','text','published_date', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

