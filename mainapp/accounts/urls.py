from django.urls import path, include

from .views import RegisterUser

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', RegisterUser.as_view(), name='register'),
]