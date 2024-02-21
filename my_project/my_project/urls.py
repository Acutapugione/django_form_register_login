
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('my_app.urls')),
    path('new_app/', include('new_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
]
