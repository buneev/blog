from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Article
from .serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
# class ArticleListView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # return Response({"articles": serializer.data})

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # return Response({"articles": serializer.data})

# class ArticleView(generics.APIView):
    # def get(self, request):
        # articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        # serializer = ArticleSerializer(articles, many=True)
        # return Response({"articles": serializer.data})


# from rest_framework.response import Response
# from rest_framework.views import APIView
# from ..models import Article

# class ArticleListView(APIView):
    # def get(self, request):
        # articles = Article.objects.all()
        # return Response({"articles": articles})