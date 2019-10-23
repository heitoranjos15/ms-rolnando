from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from watson_comunnication.models import Question, Answer, QuestionAndAnswer, User
from watson_comunnication.api.serializers import QuestionSerializer, AnswerSerializer
from watson_comunnication.watson.watson import Watson



@api_view(['POST'])
def make_question(request, question):
    return generate_answer(question)

@api_view(['PUT'])
def give_feedback(request, answer, like):
    try:
        answer = Answer.objects.get(pk=answer)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        q_and_a = QuestionAndAnswer.objects.get(pk=answer.pk)
        q_and_a.feedback = like == 'yes'
        q_and_a.save()
        return Response(status= status.HTTP_204_NO_CONTENT)
    except QuestionAndAnswer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def make_question_by_sound(request):
    watson_cli = Watson('Hyl6G5lgweo7Cz1VgZbrG7bAdqmMyaPi5i63WfVJCljF')
    f = open('./file.wav', 'wb')
    f.write(request.body.get('audio'))
    f.close()
    question = watson_cli.get_question()
    return generate_answer(question)


def generate_answer(question):
    question = Question(question= question)
    if question:
        question.save()
        watson_cli = Watson('7BSPukrBopB1OvFJZGPhjTIrnuENtr_BvVFkqMoY8am8', '44da4824-c00e-4c0a-87e4-d34e4485546e')
        response_answer = watson_cli.get_answer(question.question)
        if response_answer:
            answer = Answer(answer=response_answer)
            answer.save()
            q_and_a = QuestionAndAnswer()
            q_and_a.user = User.objects.get(pk=1)
            q_and_a.answer = answer
            q_and_a.question = question
            q_and_a.feedback = True
            q_and_a.save()
            return Response({'answer': response_answer, 'question_and_response_code': q_and_a.pk}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(question, status=status.HTTP_400_BAD_REQUEST)
