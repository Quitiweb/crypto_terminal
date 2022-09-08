import csv
import os

from django.core.management.base import BaseCommand

from crypto_terminal.settings import BASE_DIR
from ...models import CryptoCoin


class Command(BaseCommand):
    help = "Load coin data into the SQL database from a CSV file"

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.path = None

    def handle(self, *args, **kwargs):
        data_path = os.path.join('data', 'archive')
        self.path = os.path.join(BASE_DIR, 'archive')
        print(self.path)
        return
        self.load_coins()

    def load_coins(self):
        for fn in os.listdir(self.path):
            with open(fn) as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    _, created = CryptoCoin.objects.get_or_create(
                        serial_number=row[0], name=row[1], symbol=row[2], date=row[3],
                        high=row[4], low=row[5], open=row[6], close=row[7],
                        volume=row[8], market_cap=row[9]
                    )
