from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
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

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {"question": question, "error_message": "You didn't selected a choice!"}
        return(request, "detail.html", context)
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return redirect("polls:results", question_id=question.id)
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, 'results.html', context)