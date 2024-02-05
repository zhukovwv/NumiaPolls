from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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


@login_required
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

                UserResponse.objects.create(
                    user=request.user,
                    question=question,
                    choice=choice,
                    poll=poll
                )

                choice.votes += 1
                choice.save()

            return redirect(reverse('polls:poll_results',
                                    kwargs={'poll_id': poll_id}))

    return render(request, 'polls/poll_detail.html', {'poll': poll, 'questions': questions, 'form': form})


def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    questions = Question.objects.filter(poll=poll)

    question_stats = []
    for question in questions:
        choices = Choice.objects.filter(question=question)
        choice_stats = []

        for choice in choices:
            choice_count = UserResponse.objects.filter(
                poll=poll,
                question=question,
                choice=choice
            ).count()

            choice_stats.append({
                'choice_text': choice.text,
                'choice_count': choice_count
            })

        question_stats.append({
            'question_text': question.text,
            'choices': choice_stats
        })

    return render(request, 'polls/poll_results.html', {'poll': poll, 'question_stats': question_stats})
