from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#flag choices
CHOICE = (
        ('BOUGHT', 'BOUGHT'),
        ('NOT AVAILABLE', 'NOT AVAILABLE'),
        ('PENDING', 'PENDING'),
    )


class Items(models.Model):
    '''
    model class for creating db
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)
    status = models.CharField(choices=CHOICE, max_length=40)
    date = models.DateField()

    def __str__(self):
        return self.name
