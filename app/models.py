from django.db import models

# Create your models here.
class pastes(models.Model):
    unique_link=models.CharField(max_length=100)
    snippet=models.TextField()
    creation_date=models.DateTimeField(auto_now_add=True)