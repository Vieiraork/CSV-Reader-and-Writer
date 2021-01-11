import csv
from src import Input_options


class File_CSV:
    def __init__(self):
        self.file_name = 'Ex1.csv'
        self.index_columns = []
        self.values = []
        self.samples = []
        self.first_line = []
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
            csv_file.close()

    def write(self):
        with open(self.file_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            if len(self.first_line) < 1:
                self.first_line = self.reader_txt().replace(';', ' ').split()

            self.line()
            for items in self.first_line:
                self.values.append(input(f'Type {items} value: '))

            writer.writerow(self.values)
            self.values.clear()

            csv_file.close()

    def reader(self):
        with open(self.file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            reader.__next__()
            for row in reader:
                print(row)

            csv_file.close()

    def reader_txt(self):
        with open(self.file_name, 'r') as txt_file:
            file = txt_file.readlines()

            for row in file:
                return row

    def line(self):
        print('-' * 60)
