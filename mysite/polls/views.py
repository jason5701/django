from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer

from .models import Question, Choice, Post

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list
  }
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(template.render(context, request))
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404('Question does not exist')
  # return render(request, 'polls/detail.html', {'question':question})
  # return HttpResponse('you are looking at question %s.' % question_id)

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  # response = 'you are looking at the results of question %s.'
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
      selected_choice = question.choice_set.get(pk=request.POST['choice'])#key, value값으로 데이터 받아옴
  except (KeyError, Choice.DoesNotExist):
      # Redisplay the question voting form.
      return render(request, 'polls/detail.html', {
          'question': question,
          'error_message': "You didn't select a choice.",
      })
  else:
      selected_choice.votes += 1
      selected_choice.save()
      # Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.
      return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@api_view(['GET'])
def get_api(request):
  posts = Post.objects.all()
  serialzed_posts = PostSerializer(posts, many=True)
  return Response(serialzed_posts.data)

@api_view(['POST'])
def post_api(request):
  if request.method == 'GET':
    return HttpResponse(status=200)
  if request.method == 'POST':
    serializer = PostSerializer(data=request.data, many=True)
    if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=200)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)