# polls/admin.py
from django.contrib import admin
from .models import Poll, Question, Choice
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ChoiceInline(NestedStackedInline):
    model = Choice
    readonly_fields = ['votes']
    extra = 1


class QuestionInline(NestedStackedInline):
    model = Question
    inlines = [ChoiceInline]
    extra = 1


class PollAdmin(NestedModelAdmin):
    list_display = ["title", "pub_date"]
    inlines = [QuestionInline]


admin.site.register(Poll, PollAdmin)
