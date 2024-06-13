from django.db import models

# Create your models here.


class School(models.Model):
    sname = models.CharField( max_length=50, primary_key=True)
    sprincy = models.CharField( max_length=50)
    sphno =models.CharField( max_length=50)
    sadd = models.CharField( max_length=50)


    def __str__(self):
        return self.sname
    

    
    