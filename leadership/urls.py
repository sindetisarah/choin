from django.urls import path
from . views import delete_metric, edit_metric, profile_upload, reward, reward_confirm,trainer_profile_upload,addMetric
urlpatterns =[
    path('upload/',profile_upload,name='upload'),
    path('trainer-upload/',trainer_profile_upload,name='trainer-upload'),
    path('reward/',reward,name='reward'),
    path('reward_confirm/',reward_confirm,name='reward_confirm'),
    path('metrics/',addMetric,name='metrics'),
    path('delete_metric/<int:id>',delete_metric,name='delete'),
    path('edit_metric/<int:id>',edit_metric,name='edit'),

   

]