from django.db import models

class Meet(models.Model):
    meets_name= models.CharField(max_length=300)
    meets_date= models.DateField()
    meets_speaker= models.CharField(max_length=100)
    meets_venue=models.CharField(max_length=300)
    meets_description= models.CharField(max_length=300)

    def __str__(self):
        return self.meets_name


class Speaker(models.Model):
    speaker_name=models.CharField(max_length=100)
    speaker_linkedin=models.CharField(max_length=100)

    def __str__(self):
        return self.speaker_name


