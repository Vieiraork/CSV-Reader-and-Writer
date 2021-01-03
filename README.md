# CSV-Reader-and-Writer

This project is a simple csv manipulator in python.

## Tecnologies

Python 3.8.2

## How to run

1. Inside of **File.py** change the attribute **self.file_name** for name of your file
  ```
        def __init__(self):
          self.file_name = 'name of your file.CSV'
  ```
2. Inside of **File.py** in function **create_file** change the line what contains **writer.writerow**
  ```
        def create_file(self):
          with open(self.file_name, 'x', newline='') as csv_file:
              writer = csv.writer(csv_file, delimiter=';')

              # Here type a first line of your csv file
              # Type inside of a list
              writer.writerow(['Columns name in first line of CSV file'])

        csv_file.close()
  ```
3. In **File.py** inside of **write** function you have to edit the vaiables to set the structure of your file
  ```
        def write(self):
          name = input('Type your name: ')
          age = Input_options.read_int(msg='Type your age')
          # You can add more values to insert in your file

          with open(self.file_name, 'a', newline='') as csv_file:
              writer = csv.writer(csv_file, delimiter=';')
              
              # You can separete values by comma
              writer.writerow([name, age])

          csv_file.close()
  ```
4. Run **main.py** and enjoy!


