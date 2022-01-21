from django.db import models

class Dog(models.Model):
    '''Dog Model'''
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    home_details = models.TextField(max_length=300)
    about = models.TextField(max_length=500)
    can_live_with_dogs = models.BooleanField(default=False)
    can_live_with_cats = models.BooleanField(default=False)
    can_live_with_kids = models.BooleanField(default=False)
    date_added = models.DateTimeField()
    image_one = models.CharField(max_length=300)
    image_two = models.CharField(max_length=300, null=True, blank=True)
    image_three = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
