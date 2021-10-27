from django.urls import path
from . views import profile_upload, reward, reward_confirm,trainer_profile_upload

urlpatterns =[
    path('upload/',profile_upload,name='upload'),
    path('trainer-upload/',trainer_profile_upload,name='trainer-upload'),
    path('reward/',reward,name='reward'),
    path('reward_confirm/',reward_confirm,name='reward_confirm'),

]