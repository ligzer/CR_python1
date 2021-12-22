from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Town(models.Model):
    """Town is a town"""
    Name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.Name


class Street(models.Model):
    """Street is a street of a town"""

    class Meta:
        unique_together = [['Town', 'Name']]

    Town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='streets')
    Name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Town.Name}, {self.Name}"


class Store(models.Model):
    """Store is a store on a street in a town"""
    Street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='stores')
    Name = models.CharField(max_length=200)
    Number = models.CharField(max_length=10)
    Comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.Street.Town.Name}, {self.Street.Name} {self.Number}, {self.Name}"


class Schedule(models.Model):
    """Schedule of a store on a street in a town"""
    OpenTime = models.TimeField()
    CloseTime = models.TimeField()
    # TODO: Add check of unique DayOfWeek for one Store
    DayOfWeek = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)])
    Store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='Schedule')
