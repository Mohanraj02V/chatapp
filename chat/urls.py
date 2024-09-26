# chat/urls.py

from django.urls import path
from .views import signup_view, login_view, chat_view, logout_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('chat/', chat_view, name='chat'),
    path('logout/', logout_view, name='logout'),
]

