from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice,Vote
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect

# def polls(request):
#         return render(request, 'pages/polls.html')  # Render the contact form template for GET requests

def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        user_vote = None
        if request.user.is_authenticated:
                user_vote = Vote.objects.filter(user=request.user).first()
        context = {
                'latest_question_list': latest_question_list,
                'user_vote': user_vote
                }
        return render(request, 'polls/index.html', context)


def detail(request, question_id):
        question = get_object_or_404(Question,pk = question_id)
        user_vote = None
        if request.user.is_authenticated:
                user_vote = Vote.objects.filter(user=request.user, question=question).first()
        return render(request, 'polls/detail.html', {
                'question': question,
                'user_vote': user_vote
                })


def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question})

@login_required
def vote(request, question_id):
        question = get_object_or_404(Question, pk = question_id)
        try:
                selected_choice = question.choice_set.get(pk = request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
                return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
        
        # Check if the user has already voted
        if Vote.objects.filter(user=request.user, question=question).exists():
                messages.warning(request, 'You have already voted')
                return redirect('votingpolls:index')
         # Record the vote
        else:
                Vote.objects.create(user=request.user, question=question, choice=selected_choice)
                selected_choice.votes += 1
                selected_choice.save()
        
        messages.success(request, 'Your vote has been recorded successfully.')
        return redirect('votingpolls:index')

def all_results(request):
    # Check if the user has voted
    if not request.user.is_authenticated or not Vote.objects.filter(user=request.user).exists():
        # If the user has not voted, redirect them to another page or display a message
        messages.error(request, 'You need to vote first to see the results.')
        return redirect('votingpolls:index')  # Redirect to the index page or any other page
    else:
        # If the user has voted, retrieve all questions and render the results page
        questions = Question.objects.all()
        return render(request, 'pages/result.html', {'questions': questions})
