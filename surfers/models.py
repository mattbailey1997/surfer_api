from django.db import models

# Create your models here.
class Surfer(models.Model):
    nationality = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=100, default=None)
    age = models.PositiveIntegerField(default=None)
    rank = models.PositiveBigIntegerField(blank=True, null=True)
    still_active = models.BooleanField(default=True)
    styles = models.ManyToManyField(
        'styles.Style',
        related_name='surfers'
    )

    def __str__(self):
        return f"{self.nationality} - {self.name} - {self.age}yrs"