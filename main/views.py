from rest_framework.generics import *
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter


# CATEGORY VIEWS
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# NEWS VIEWS
class NewsListCreateAPIView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'views', 'created_date']


class NewsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save(update_fields=["views"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# MEDIA VIEWS
class MediaListCreateAPIView(ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


# ADVERTISEMENT VIEWS
class AdvertisementListCreateAPIView(ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
