from rest_framework import serializers
from watson_comunnication.models import (Question, Answer, QuestionAndAnswer)

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer']

class QuestionAndAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionAndAnswer
        fields = ['user', 'question', 'answer', 'feedback']
