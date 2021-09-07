from django.db import models

# Create your models here.

class Poll(models.Model):
    question=models.TextField()
    opt1=models.CharField(max_length=100)
    opt2=models.CharField(max_length=100)
    opt3=models.CharField(max_length=100)
    opt1_count=models.IntegerField(default=0)
    opt2_count = models.IntegerField(default=0)
    opt3_count = models.IntegerField(default=0)

    def total(self):
        return self.opt1_count+self.opt2_count+self.opt3_count