from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'blog'

router = DefaultRouter()
router.register("", views.BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]