from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Question, Choice

# Create your views here.
def index(request):
    all_questions = Question.objects.all().order_by("-publish_date") # select * from question order by publish_date desc
    context = {"all_questions":all_questions}
    return render(request, "index.html", context)

def detail(request, question_id):
    try:
        current_question = Question.objects.get(pk=question_id) # select * from question where id = question_id
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist!")
    context = {"question":current_question}
    return render(request, "detail.html", context)