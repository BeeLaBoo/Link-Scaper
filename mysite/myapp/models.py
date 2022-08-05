from django.db import models

class Link(models.Model):
    def __str__(self) :
        return self.name
    
    
    address = models.CharField(max_length=1000, blank=True,null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
