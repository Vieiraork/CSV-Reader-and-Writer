import csv
from src import Input_options


class File_CSV:
    def __init__(self):
        self.file_name = 'Ex1'
        self.index_columns = []
        self.values = []
        self.samples = []
        self.columns_number = None

    def create_file(self):
        with open(self.file_name, 'x', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            self.columns_number = Input_options.read_int(msg='Type a number of columns')

            for column in range(self.columns_number):
                self.index_columns.append(input(f'Name of {column+1}º column: '))

            # Here type a first line of your csv file
            # Type inside of a list
            writer.writerow(self.index_columns)

            self.samples = ['Sample'] * self.columns_number
            writer.writerow(self.samples)

            csv_file.close()

    def write(self):
        with open(self.file_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            new = self.reader(length=True)

            for items in range(new):
                self.values.append(input(f'Type {items + 1} value: '))

            writer.writerow(self.values)
            self.values.clear()

            csv_file.close()

    def reader(self, length=False):
        with open(self.file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            reader.__next__()
            for row in reader:
                if length:
                    return len(row)
                else:
                    print(row)

            csv_file.close()
