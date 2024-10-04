from django.urls import path
from . import views

# Define URL patterns for the page1 app
urlpatterns = [
    path('', views.page1_view, name='page1'),
]
