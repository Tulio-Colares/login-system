from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #on_DELETE can have values for CASCADE or SET_NULL. CASCADE means that, if the item gets deleted, its 
    title = models.CharField(max_length=200)                                        #children will also get deleted whereas with set_null they will not.
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False) 
    created = models.DateTimeField(auto_now_add=True) #The difference between auto_add and auto_now_add is that the first adds just the date and the second adds the date and the time of posting
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] #whenever we have multiple items in a list, we will order them by the 'complete' value