from django.db import models


# Create your models here.
class WhyItem(models.Model):
    why_title = models.CharField(max_length=250)
    why_text = models.TextField(max_length=500)
    why_image = models.ImageField(upload_to='IMG')

    def __str__(self):
        return self.why_title


class Team(models.Model):
    team_name = models.CharField(max_length=120)
    team_text = models.TextField(max_length=250)
    team_image = models.ImageField(upload_to='IMG')

    def __str__(self):
        return self.team_name
