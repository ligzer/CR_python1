from rest_framework import serializers
from .models import Town, Street, Store, Schedule


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = ('id', 'Name',)


class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = ('id', 'Name', 'Town')


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('DayOfWeek', 'OpenTime', 'CloseTime',)


class StoreSerializer(serializers.ModelSerializer):
    Schedule = ScheduleSerializer(many=True, read_only=True, source='schedule')

    class Meta:
        model = Store
        fields = ('id', 'Name', 'Number', 'Street', 'Schedule')



