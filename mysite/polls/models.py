from django.db import models

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.choice_text
  
class Post(models.Model):
  post_id = models.IntegerField(),
  title = models.CharField(max_length=1000),
  content = models.CharField(max_length=1000),
  wrtier = models.CharField(max_length=1000),
  created_at = models.DateTimeField('date published'),
  updated_at = models.DateTimeField('date published')