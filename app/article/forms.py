from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'pub_date', 'author', 'tags']
        labels = {
            'title': 'Название',
            'text': 'Текст',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'tags': 'Теги',
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
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})

    def clean_text(self, *args, **kwargs):
        text = self.cleaned_data.get("text", '')
        if not text:
            raise forms.ValidationError(f"Текст статьи должен быть заполнен")
        return text


