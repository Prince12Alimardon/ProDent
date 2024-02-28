from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactAPIView.as_view(), name='contact'),
    path('info/', ContactInfoAPIView.as_view(), name='info'),
    path('getintouch/', GetInTouchAPIView.as_view(), name='getintouch')
]

