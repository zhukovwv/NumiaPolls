from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Question, Choice, UserResponse
from .forms import ResponseForm


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

                # Create or update UserResponse
                user_response, created = UserResponse.objects.get_or_create(
                    user=request.user,
                    question=question,
                    defaults={'choice': choice}
                )

                if not created:
                    user_response.choice = choice
                    user_response.save()

                # Increment votes for the selected choice
                choice.votes += 1
                choice.save()

            # Redirect or render success message
            return redirect('polls:poll_list')

    return render(request, 'polls/poll_detail.html', {'poll': poll, 'questions': questions, 'form': form})
