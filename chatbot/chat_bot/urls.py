from django.urls import path
from . views import chatbot, login, register, logout

urlpatterns = [
     path('', chatbot, name='chatbot'),
     path('login/', login, name='login'),
     path('register/', register, name='register'),
     path('logout/', logout, name='logout')
]