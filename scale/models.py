from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    height = models.IntegerField(default=170)
    gender = models.CharField(max_length=1, default='M')
    hex_color = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return self.name

class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return '{} - {}: {}kgs'.format(self.date, self.user.name, self.value)
    