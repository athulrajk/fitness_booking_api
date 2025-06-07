from django.db import models

# Create your models here.
from django.utils import timezone

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()
    active = models.BooleanField()

    def __str__(self):
        return f"{self.name} with {self.instructor} at {self.start_time}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"
