from django.db import models

from authors.models import Author


# Create your models here.
class Song (models.Model):
    title = models.CharField( max_length= 100)
    duration = models.IntegerField()
    genre = models.CharField (max_length= 80)
    release_date = models.DateField(help_text= "Song release date")
    # kada sukurtas ir koreguotas irasas
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # ka daryti kai bus istrintas autorius. cia aprasoma
    # kad bus istrintos ir dainos to autoriaus
    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return f"{self.title} {self.genre}"