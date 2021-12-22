from django.db import models

# Create your models here.


class Town(models.Model):
    """Town is a town"""
    Name = models.CharField(max_length=200)


class Street(models.Model):
    """Street is a street of a town"""
    Town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='streets')
    Name = models.CharField(max_length=200)


class Store(models.Model):
    """Store is a store on a street in a town"""
    Street = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='stores')
    Name = models.CharField(max_length=200)
    Number = models.CharField(max_length=10)


class Schedule(models.Model):
    """Schedule of a store on a street in a town"""
    # TODO: Add check Begin > End
    Begin = models.TimeField()
    End = models.TimeField()
    # TODO: Add check of unique DayOfWeek for one Store
    # TODO: Add check 0<=DayOfWeek<=7
    DayOfWeek = models.IntegerField()
    Store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='schedules')


