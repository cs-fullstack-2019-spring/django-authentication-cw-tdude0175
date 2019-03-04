from django.urls import path

from . import views


urlpatterns = \
    [
        path('',views.index , name= 'index'),
        path('newUser/',views.newUser, name= 'newUser'),
        path('saveNewUser/', views.saveNewUser, name='saveNewUser')
    #     last path is used only for saving the stuff
    ]