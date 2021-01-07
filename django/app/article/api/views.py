from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..models import Article
from .serializers import ArticleSerializer

class ArticleListView(APIView):
    """
    API endpoint that allows users viewed list all artiles
    """
    def get(self, request, format=None):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        saved_articles = 0
        articles = request.data # выбрать формат json в postman
        for article in articles:
            serializer = ArticleSerializer(data=[article], many=True) # data=request.data
            if serializer.is_valid():
                serializer.save()
                saved_articles += 1
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(f"OK, saved {saved_articles} articles of {len(articles)}", status=status.HTTP_201_CREATED)

class ArticleDetailView(APIView):
    """
    API endpoint that allows users retrieve, update or delete an article
    """
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        