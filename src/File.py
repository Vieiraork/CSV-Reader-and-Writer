import csv
from src import input_options


class File:
    def __init__(self) -> None:
        self.file_name = 'Ex1.csv'
        self.columns_name = []
        self.values = []
        self.first_line = []
        self.columns_number = None

    def create_file(self) -> None:
        with open(self.file_name, 'x', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            self.columns_number = input_options.read_int(msg='Type a number of columns')

            for column in range(self.columns_number):
                self.columns_name.append(input(f'Name of {column+1}º column: '))

            # Here type a first line of your csv file
            # Type inside of a list
            writer.writerow(self.columns_name)
            csv_file.close()

    def write(self) -> None:
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

    def reader(self) -> None:
        with open(self.file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            reader.__next__()
            for row in reader:
                for item in row:
                    print(f'{item}', end=' | ')
                print()

            csv_file.close()

    def reader_txt(self) -> None:
        with open(self.file_name, 'r') as txt_file:
            file = txt_file.readlines()

            txt_file.close()

            for first_row in file:
                return first_row

    def create_new_csv(self, name: str) -> None:
        with open(f'{name}.csv', 'x', newline='')  as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

            self.columns_number = input_options.read_int(msg='Type a number of columns')

            for column in range(self.columns_number):
                self.columns_name.append(input(f'Name of {column+1}º column: '))

            writer.writerow(self.columns_name)
            csv_file.close()

    def line(self) -> None:
        print('-' * 60)
