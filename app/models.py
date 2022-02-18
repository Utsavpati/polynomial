from django.db import models

# Create your models here.
class pastes(models.Model):
    unique_link=models.CharField(max_length=100)
    snippet=models.TextField()
    creation_date=models.DateTimeField(auto_now_add=True)
    encrypted=models.BooleanField(default=False)

    class Meta:
        ordering=['-creation_date']


class PasteTextAccess(models.Model):
    accessed = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_text = models.ForeignKey(pastes, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-accessed"]