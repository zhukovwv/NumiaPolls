from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Poll, Question, Choice, UserResponse
from .forms import ResponseForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('polls:poll_list'))
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})


def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    questions = Question.objects.filter(poll=poll)
    form = ResponseForm(questions=questions)

    if request.method == 'POST':
        form = ResponseForm(questions=questions, data=request.POST)
        if form.is_valid():
            for question in questions:
                choice_id = form.cleaned_data[f'question_{question.id}']
                choice = get_object_or_404(Choice, pk=choice_id)

                user_response, created = UserResponse.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={'choice': choice}
                )

                choice.votes += 1
                choice.save()

            return redirect(reverse('polls:poll_list'))

    return render(request, 'polls/poll_detail.html', {'poll': poll, 'questions': questions, 'form': form})
