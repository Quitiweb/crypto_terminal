import csv
import datetime
import os

from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from crypto_terminal.settings import BASE_DIR
from crypto_tools.models import CryptoCoin


class Command(BaseCommand):
    help = "Load coin data into the SQL database from a CSV file"

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.path = None

    def handle(self, *args, **kwargs):
        data_path = os.path.join('data', 'archive')
        self.path = os.path.join(BASE_DIR, data_path)
        self.load_coins()

    def load_coins(self):
        print()
        print("Processing all the data. This make take a while. Please, be patient ...")
        print()
        files = os.listdir(self.path)
        len_files = len(files)
        for count, fn in enumerate(files):
            print("Loading file {} of {}".format(count+1, len_files))
            fpath = os.path.join(self.path, fn)
            with open(fpath) as f:
                reader = csv.reader(f, delimiter=",")
                next(reader, None)  # skip the headers
                for row in reader:
                    date_time = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                    time_aware = make_aware(date_time)
                    _, created = CryptoCoin.objects.get_or_create(
                        serial_number=row[0], name=row[1], symbol=row[2], date=time_aware,
                        high=row[4], low=row[5], open=row[6], close=row[7],
                        volume=row[8], market_cap=row[9]
                    )

        print("All files have been processed successfully")
