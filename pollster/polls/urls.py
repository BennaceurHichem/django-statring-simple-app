from django.urls import path 
from . import views 

app_name='polls'
urlpatterns=[
    #this mean polls/ will render the polls tempalte 
    path('',views.index,name='index'),




]