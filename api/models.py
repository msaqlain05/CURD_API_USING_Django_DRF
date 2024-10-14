from django.db import models

# Create your models here.


# this class is Student Mode class this is create sql data
class Student(models.Model):
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    Class=models.CharField(max_length=10)
    roll_no=models.IntegerField()

    def __str__(self):
        return self.name
    

