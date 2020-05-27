from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Question,Choice



#Get question and display them 
def index(request):
    latest_question_list =Question.objects.order_by('publish_date')[:5]
    #context is what we want to pas to the template 
    context =  {'latest_question_list':latest_question_list}
    #passing cotnext to the tempalte
    return render(request,'polls/index.html',context)



def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")

    return render(request,'polls/detail.html',{'question':question})

#get question and dispaly result,
#  we pass quetion as acontext and dispaly result.html
def results(request,question_id):
    question= get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})


def vote(request,question_id):
    