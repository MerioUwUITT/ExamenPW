from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.menu,name='menu'),
    path('registerP/',views.player_form,name='player_insert'),
    path('<int:id>/',views.player_form,name='player_update'),
    path('deleteP/<int:id>/',views.player_delete,name='player_delete'),
    path('listP/',views.player_list,name='player_list'),
    path('listT/',views.team_list,name='team_list'),
    path('registerT/',views.team_form,name='team_insert'),
    path('updateT/<int:id>/',views.team_form,name='team_update'),
    path('deleteT/<int:id>/',views.team_delete,name='team_delete'),
    path('registerS/',views.stadium_form,name='stadium_insert'),
    path('listS/',views.stadium_list,name='stadium_list'),
    path('updateS/<int:id>/',views.stadium_form,name='stadium_update'),
    path('deleteS/<int:id>/',views.stadium_delete,name='stadium_delete'),
    
    ]