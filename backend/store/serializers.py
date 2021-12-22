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
    Schedule = ScheduleSerializer(many=True, read_only=False)
    Town = serializers.CharField(source='Street.Town.Name')
    Street = serializers.CharField(source='Street.Name')

    class Meta:
        model = Store
        fields = ('id', 'Name', 'Comment', 'Town', 'Street', 'Number', 'Street', 'Schedule')

    def create(self, validated_data):
        if 'Schedule' in validated_data:
            schedule = validated_data['Schedule']
            del validated_data['Schedule']
        if 'Street' in validated_data:
            street_name = validated_data['Street'].get('Name', '')
            if 'Town' in validated_data['Street']:
                town_name = validated_data['Street']['Town'].get('Name', '')
        if not street_name or not town_name:
            raise serializers.ValidationError

        town, created = Town.objects.get_or_create(Name=town_name)
        validated_data['Street'], created = Street.objects.get_or_create(Town=town, Name=street_name)
        instance = Store.objects.create(**validated_data)
        for schedule_validated_data in schedule:
            Schedule.objects.create(Store=instance, **schedule_validated_data)
        return instance
