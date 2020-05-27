from django.shortcuts import render

# Create your views here.
from .models import Question,Choice



#Get question and display them 
def index(request):
    latest_question_list =Questions.objects.order_by('publish_date')
    return render(request,'polls/index.html')