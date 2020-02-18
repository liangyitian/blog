from django.db import models
from django.utils import timezone
import json

class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)
    view_num=models.SmallIntegerField(default=0)
    like_num=models.SmallIntegerField(default=0)
    comment_list=models.TextField(default='')


    class Meta:
        ordering=('-pub_date',)

    def __str__(self):
        return self.title

# Create your models here.
