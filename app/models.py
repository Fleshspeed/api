from django.db import models

class Data(models.Model):
    pros = models.CharField(max_length=255)
    videokarta = models.CharField(max_length=255)




    def __str__(self):
        return self.pros