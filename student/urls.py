from django.urls import path
from . views import redeem,profile
# from core.views import Profile
urlpatterns =[
    path('redeem/',redeem,name='redeem'),
    path('student-profile/',profile,name='student-profile'),
    ]