from django.db import models


class Service_Provider(models.Model):
    name            =  models.CharField(max_length=100)
    panno           =  models.CharField(max_length=30)
    about           =  models.TextField(max_length=50)
    location        =  models.CharField(max_length=100)
    contactno       =  models.CharField(max_length=10)
    averageRating   =  models.FloatField()
    image           =  models.ImageField(upload_to='pics')

    #remember to add about us about the service provider

    def __str__(self):
        return self.name + str(self.image)

