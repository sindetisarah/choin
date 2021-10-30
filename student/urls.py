from django.urls import path
from . views import redeem
from core.views import Profile
urlpatterns =[
    path('redeem/',redeem,name='redeem'),
    path('profile/',Profile,name='student-profile'),
    ]