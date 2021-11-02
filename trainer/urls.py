from django.urls import path
from . views import trainer_dashboard,trainer_profile
urlpatterns =[
    path('trainer-dashboard/',trainer_dashboard,name='trainer-dashboard'),
    path('trainer-profile/',trainer_profile,name='trainer-profile'),

    ]