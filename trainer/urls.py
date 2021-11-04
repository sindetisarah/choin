from django.urls import path
from . views import add_transaction, connect_node, get_chain, is_valid, replace_chain, trainer_home,trainer_profile, trainer_reward, trainer_reward_confirm, trainer_search_student, trainer_trans

urlpatterns =[
    path('get_chain/', get_chain, name="get_chain"),
    path('add_transaction/', add_transaction, name="add_transaction"), #New
    path('is_valid/', is_valid, name="is_valid"), #New
    path('connect_node/', connect_node, name="connect_node"), #New
    path('replace_chain/', replace_chain, name="replace_chain"), #New
    path('reward/',trainer_reward,name='trainer_reward'),
    path('reward_confirm/<int:id>/',trainer_reward_confirm,name='trainer_reward_confirm'),
    path('trans/',trainer_trans,name='trainer_trans'),
    path('search/',trainer_search_student,name='tariner_search_student'),
    path('trainer-home/',trainer_home,name='trainer-home'),
    path('trainer-profile/',trainer_profile,name='trainer-profile'),
    ]

