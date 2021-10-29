from src import file
from src import options
from src import input_options
from os import path

# Set variables
file = file.File()
menu = options.Options['menu']
list_options = options.Options['menu_options']
name = ''

if not path.exists(file.file_name):
    file.create_file()
else:
    response = input('Do you want create an new csv file?[y, n] ').lower().strip()[0]

    if response == 'y':
        while len(name) < 1:
            name = input('Type the name of your file without .csv: ').strip()

        file.create_new_csv(name)

if __name__ == '__main__':
    while True:
        print(menu)

        options = input_options.read_int(msg='Type a option')

        if list_options.__contains__(options):
            if options == 1:
                file.write()
            elif options == 2:
                file.reader()
            elif options == 3:
                break
        else:
            print('Error: invalid option')
