from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

class Entry(models.Model):
    # id = models.AutoField(primary_key=True) ... Django adds by default
    title = models.CharField(max_length=200)
    text = models.TextField()    
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
    
    def published_today(self):
        now = timezone.now()
        time_delta = now - self.pub_date
        return time_delta.days == 0
    published_today.boolean = True
    published_today.short_description = 'Published Today?'


    
