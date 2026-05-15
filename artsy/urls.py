from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'my-art',UserArtViewSet,basename='my-art')

urlpatterns = [
    path('', include(router.urls)),
    path('artsy/',ArtsyView.as_view(), name='artsy'),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("bid/", BidView.as_view(), name="bid"),
]