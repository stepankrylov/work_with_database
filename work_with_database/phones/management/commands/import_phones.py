import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                rec = Phone(
                            id=line[0],
                            name=line[1],
                            image=line[2],
                            price=line[3],
                            release_date=datetime.strptime(line[4], '%Y-%m-%d'),
                            lte_exists=line[5],
                            slug=slugify(line[1])
                            )
                rec.save()





