def read_int(msg):
    while True:
        try:
            value = int(input(f'{msg}: '))
        except KeyboardInterrupt:
            print('User dont type any value\n')
        except ValueError:
            print('Type only int values')
        else:
            return value
