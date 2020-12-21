import csv
import os
from src import Input_options


class File_CSV:
    def __init__(self):
        self.file_name = 'Ex1'

    def create_file(self):
        with open(self.file_name, 'x', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            # Here type a first line of your csv file
            # Type inside of a list
            writer.writerow(['Name', 'Age'])

        csv_file.close()

    def write(self):
        name = input('Type your name: ')
        age = Input_options.read_int(msg='Type your age')

        with open(self.file_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            writer.writerow([name, age])

        csv_file.close()

    def read(self):
        with open(self.file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            reader.__next__()

            for row in reader:
                print(row)

            csv_file.close()
