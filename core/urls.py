from django.urls import path
from . views import  *

urlpatterns=[
    path('',LoginView.as_view(),name='login'),
    path('home/',index,name='index'),
    path('/profile',Profile,name='user_profile')
    ]