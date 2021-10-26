from django.urls import path
from . views import profile_upload, reward, reward_confirm
urlpatterns =[
    path('upload/',profile_upload,name='upload'),
    path('reward/',reward,name='reward'),
    path('reward_confirm/',reward_confirm,name='reward_confirm'),

]