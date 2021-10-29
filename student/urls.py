from django.urls import path
from . views import redeem
urlpatterns =[
    path('redeem/',redeem,name='redeem')

    ]