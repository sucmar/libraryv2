from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r"genre", views.GenreViewSet)
router.register(r"language", views.LanguageViewSet)
router.register(r"author", views.AuthorViewSet)
router.register(r"book", views.BookViewSet)

urlpatterns = [
    # path("", views.index, name="index"),
    path('genres/<str:name>', views.GenreCustomAPI.as_view(), name='genres'),
    path('genres/', views.GenreCustomAPI.as_view(), name='genres'),
    path('', include(router.urls)),
]
