from .views import IndexView, create, register, logout_view, login_view
from django.urls import path, include

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('create/', create, name="create"),
    
    path('sign_in/', login_view, name="login"),
    path('sign_up/', register, name="register"),
    path('sign_out/', logout_view, name="logout"),
]
