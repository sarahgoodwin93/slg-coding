from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Home app
    path('page1/', include('page1.urls')),  # Page 1 app
    path('__debug__/', include('debug_toolbar.urls')),
]
