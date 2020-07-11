from django.db import models

import datetime

# Models for Events


class Event(models.Model):
    name =models.CharField('Event Name', max_length=120)
    description=models.CharField('Event Description', max_length=500)
    event_date=models.DateTimeField();
    published_date=models.DateTimeField();
    speaker=models.CharField('Speaker Name', max_length=120)
    event_url=models.CharField('Event Url Name', max_length=120)
    event_ppt_url=models.CharField('Event PPT  Url ', max_length=120)
    event_video_url=models.CharField('Event Video Url ', max_length=120)
    event_poster_url=models.CharField('Event Poster Url ', max_length=120)
    

    def __str__(self):
        return self.name


