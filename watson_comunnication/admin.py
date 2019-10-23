from django.contrib import admin
from watson_comunnication.models import (Answer, Question, User, QuestionAndAnswer)

class QuestionAndAnswerDisplay(admin.ModelAdmin):
    list_display = ('question', 'answer', 'user', 'feedback', 'data')

admin.site.register(QuestionAndAnswer, QuestionAndAnswerDisplay)
admin.site.register(Answer)
admin.site.register(Question)