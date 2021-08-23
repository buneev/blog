from django import forms
from .models import Article
from django.conf.global_settings import DATETIME_INPUT_FORMATS

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'pub_date', 'authors', 'sourse_link', 'tags', 'image')
        labels = {
            'title': 'Название',
            'text': 'Текст',
            'pub_date': 'Дата публикации',
            'authors': 'Автор',
            'sourse_link': 'Ссылка первоисточника',
            'tags': 'Теги',
            'image': 'Ссылка на изображение'
        }
        error_messages = {
            'author': {
                'max_length': "Имя автора слишком длинное",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['pub_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['authors'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})
        self.fields['sourse_link'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    def clean_text(self, *args, **kwargs):
        text = self.cleaned_data.get("text", '')
        if not text:
            raise forms.ValidationError(f"Текст статьи должен быть заполнен")
        if len(text) < 20:
            raise forms.ValidationError("Текст статьи слишком короткий")
        return text


class RunParseSiteForm(forms.Form):
    site_name = forms.CharField(max_length=100)
    
