from django.contrib import admin
from .models import Poll, Question, Choice, UserResponse
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


class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'poll', 'question', 'choice']
    list_filter = ['poll', 'question']
    search_fields = ['user__username', 'poll__title', 'question__text', 'choice__text']
    readonly_fields = ['user', 'poll', 'question', 'choice']

admin.site.register(UserResponse, UserResponseAdmin)
