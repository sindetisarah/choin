from django.urls import path
from . views import trainer_home,trainer_profile
urlpatterns =[
    path('trainer-home/',trainer_home,name='trainer-home'),
    path('trainer-profile/',trainer_profile,name='trainer-profile'),
    ]