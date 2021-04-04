from django.db import models
from django.utils import timezone
from django.utils.timezone import utc

# Create your models here.

class codingsession(models.Model):
	name = models.CharField(max_length=1824, unique=True)
	language= models.CharField(max_length=1824)
	link = models.CharField(max_length=2848)
	starting_time = models.DateTimeField(default=timezone.now, blank=True)
