from django.urls import path
from .views import Index, DetailPage

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailPage.as_view() ,name='detail_article'),
]
