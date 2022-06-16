from django.db import models

# Create your models here.
class Review(models.Model):
    text = models.TextField(max_length=300) 
    created_at = models.DateTimeField(auto_now_add=True)
    surfer = models.ForeignKey(
      'surfers.Surfer', 
      related_name ='reviews',
      on_delete= models.CASCADE
    )