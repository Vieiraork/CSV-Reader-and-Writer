from src import File
from src import Op
from src import Input_options
from os import path

file = File.File_CSV()
menu = Op.Options['menu']
list_options = Op.Options['menu_options']

if not path.exists(file.file_name):
    file.create_file()

if __name__ == '__main__':
    while True:
        print(menu)

        options = Input_options.read_int(msg='Type a option')

        if list_options.__contains__(options):
            if options == 1:
                file.write()
            elif options == 2:
                file.read()
            elif options == 3:
                break
            else:
                print('Error: invalid option')
