from django.urls import path 
from . import views 

app_name='polls'
urlpatterns=[
    #this mean polls/ will render the polls tempalte 
    path('',views.index,name='index'),
    #opening the detail page wbased on the question id 
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='results')




]