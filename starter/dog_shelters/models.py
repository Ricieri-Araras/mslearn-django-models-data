from django.db import models
from django.urls import reverse


# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name

class Dog(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=50, default="Unknown")
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    intake_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('dog_detail', kwargs={"pk": self.pk})
