from django.db import models

# Create your models here.
class Topic(models.Model):
    """User will supply information needed to learn about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    #Specific things that need to be learned about a topic using many to one topic:
    topic = models.ForeignKey("Topic", on_delete=models.PROTECT)
    text = models

