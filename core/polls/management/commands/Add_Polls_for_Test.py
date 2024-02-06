from django.core.management.base import BaseCommand
from django.utils import timezone

from core.polls.models import Choice, Question, Poll


class Command(BaseCommand):
    help = 'Adding polls for test'

    def handle(self, *args, **options):
        # Создаем первый опрос
        poll1 = Poll.objects.create(
            title='Sample Poll 1',
            description='This is the first sample poll.',
            pub_date=timezone.now()
        )

        # Добавляем вопросы и варианты ответов для первого опроса
        question1_poll1 = Question.objects.create(poll=poll1, text='Question 1 for Poll 1')
        Choice.objects.create(question=question1_poll1, text='Choice A')
        Choice.objects.create(question=question1_poll1, text='Choice B')

        question2_poll1 = Question.objects.create(poll=poll1, text='Question 2 for Poll 1')
        Choice.objects.create(question=question2_poll1, text='Choice X')
        Choice.objects.create(question=question2_poll1, text='Choice Y')

        # Создаем второй опрос
        poll2 = Poll.objects.create(
            title='Sample Poll 2',
            description='This is the second sample poll.',
            pub_date=timezone.now()
        )

        # Добавляем вопросы и варианты ответов для второго опроса
        question1_poll2 = Question.objects.create(poll=poll2, text='Question 1 for Poll 2')
        Choice.objects.create(question=question1_poll2, text='Option 1')
        Choice.objects.create(question=question1_poll2, text='Option 2')

        question2_poll2 = Question.objects.create(poll=poll2, text='Question 2 for Poll 2')
        Choice.objects.create(question=question2_poll2, text='Red')
        Choice.objects.create(question=question2_poll2, text='Blue')

        self.stdout.write(self.style.SUCCESS('Successfully added 2 sample polls.'))