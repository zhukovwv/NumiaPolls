from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    """
    Think about it!
    
    parent_question = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child_questions')
    depends_on_choice = models.ForeignKey('Choice', null=True, blank=True, on_delete=models.CASCADE, related_name='dependent_questions')

    def get_child_questions(self, selected_choice):
        if self.child_questions.exists() and selected_choice == self.depends_on_choice:
            return self.child_questions.all()
        return []
    """
    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} answered the question '{self.question.text}' in the poll '{self.poll.title}' with the choice '{self.choice.text}'"
