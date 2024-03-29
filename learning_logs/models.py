from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """User will supply information needed to learn about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE) #Establishing a foreign key relationship in order to establish topics with a unique user

    def __str__(self):
        return self.text

class Entry(models.Model):
    #Specific things that need to be learned about a topic using many to one topic:
    topic = models.ForeignKey("Topic", on_delete=models.PROTECT)
    text = models.TextField()
    date_added  = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "entries"
    
    def __str__(self):
        #This will return a string representation of the model:
        return self.text[:50] + "..."



