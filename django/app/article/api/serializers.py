from rest_framework import serializers
from article.models import Article
from rest_framework.settings import api_settings
from ..models import Article

class ArticleSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(input_formats=api_settings.DATETIME_INPUT_FORMATS)
    
    class Meta:
        model = Article
        fields = ('title', 'text', 'pub_date', 'author', 'sourse_link', 'code', 'tags', 'image')
        # fields = '__all__'

    def validate_text(self, value):
        """
        Check that the text not empty
        """
        if len(value) < 20:
            raise serializers.ValidationError("Текст статьи слишком короткий")
        return value

    def validate_code(self, value):
        """
        Check that the article doesn't exist in database
        """
        art = Article.objects.filter(code=value).first()
        if art:
            raise serializers.ValidationError("Статья с данным кодом уже существует")
        return value
