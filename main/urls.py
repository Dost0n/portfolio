from main.views import home, category
from django.urls import path


urlpatterns = [
    path('', home, name = "homepage"),
    path('category/', category, name = 'filter'),
]