from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Expansions(models.Model):
    expansion_name = models.CharField(max_length = 50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.expansion_name

    def display_creator(self):
        return 'Created by ' + str(self.creator)

    def get_absolute_url(self):
        return reverse('expansions_detail', args=[str(self.pk)])


class Locations(models.Model):
    expansion = models.ForeignKey('Expansions', on_delete=models.CASCADE, )
    location_name = models.CharField(unique = True, max_length = 50)
    district = models.CharField(max_length = 50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location_name


    def get_absolute_url(self):
        return reverse('locations_detail', args=[str(self.pk)])


class Contacts(models.Model):
    expansion = models.ForeignKey('Expansions', on_delete=models.CASCADE)
    location = models.ForeignKey("Locations", on_delete=models.CASCADE)
    incident = models.TextField(unique = True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.incident + 'Created by ' + str(self.creator)

    def get_absolute_url(self):
        return reverse('contacts_detail', args=[str(self.pk)])