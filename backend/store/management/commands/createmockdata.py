from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import random
from store.models import Town, Street, Store, Schedule
from datetime import time


class Command(BaseCommand):
    help = 'Create fake data'

    def handle(self, *args, **options):
        # TODO: add arguments to command
        # TODO: replace magic constants
        fake = Faker()

        def random_bool():
            return random.random() > 0.1

        towns_created = 0
        while towns_created < 10 or (towns_created < 300 and random_bool()):
            Town.objects.create(Name=fake.city())
            towns_created += 1
        self.stdout.write(f'Created {towns_created} random towns')

        towns = Town.objects.all()
        streets_created = 0

        while streets_created < 30 or (streets_created < 900 and random_bool()):
            Street.objects.create(Name=fake.street_name(), Town=random.choice(towns))
            streets_created += 1
        self.stdout.write(f'Created {streets_created} random streets')

        streets = Street.objects.all()
        stores_created = 0

        while stores_created < 90 or (stores_created < 2700 and random_bool()):
            store = Store.objects.create(
                Name=fake.bs(),
                Street=random.choice(streets),
                Number=fake.building_number(),
                Comment=fake.catch_phrase(),
            )
            stores_created += 1
            for DayOfWeek in range(0, 7):
                if random_bool():
                    Schedule.objects.create(
                        Store=store,
                        DayOfWeek=DayOfWeek,
                        OpenTime=time(random.randint(0, 23), random.randint(0, 11) * 5),
                        CloseTime=time(random.randint(0, 23), random.randint(0, 11) * 5),
                    )
        self.stdout.write(f'Created {stores_created} random stores')
