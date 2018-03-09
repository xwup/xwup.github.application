from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=150)        # 博客标题，最大150字
    body = models.TextField()                       # 博客的正文部分
    timestamp = models.DateTimeField()              # 博客的时间