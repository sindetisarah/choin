from django.urls import path
from . views import trainer_dashboard
urlpatterns =[
    path('trainer_dashboard/',trainer_dashboard,name='trainer_dashboard')

    ]