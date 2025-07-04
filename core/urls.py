from django.contrib import admin
from django.urls import path
from main.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

schema_view = get_schema_view(
    openapi.Info(
        title="News API",
        default_version='v1',
        description="Test News API",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Simple JWT
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),

    # Profile
    path('register/', RegisterAPIView.as_view()),
    path('profile/', ProfileRetrieveUpdateDestroyView.as_view()),

    # Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    # Category
    path('categorys/', CategoryListCreateAPIView.as_view()),
    path('categorys/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),

    # News
    path('news/', NewsListCreateAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroyAPIView.as_view()),

    # Media
    path('medias/', MediaListCreateAPIView.as_view()),
    path('medias/<int:pk>/', MediaRetrieveUpdateDestroyAPIView.as_view()),

    # Advertisement
    path('advertisements/', AdvertisementListCreateAPIView.as_view()),
    path('advertisements/<int:pk>/', AdvertisementRetrieveUpdateDestroyAPIView.as_view()),

    # Subscription
    path('subscription/', SubscriptionListCreateAPIView.as_view()),

    # Visits
    path('visits/', VisitsListCreateAPIView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
