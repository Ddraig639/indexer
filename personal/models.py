from django.db import models

# Create your models here.

class Movie(models.Model):
    username                    = models.CharField(max_length=50)
    mdate = models.CharField(max_length=4)

    #what u want them to log in with
    #USERNAME_FIELD = 'mdate'

    #any other field dat must be required
    #REQUIRED_FIELDS = ['username','mdate',]


    def __str__(self):
        return self.username

    class Meta:
        verbose_name="movie"
        verbose_name_plural="movies"