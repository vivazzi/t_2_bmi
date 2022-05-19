def _input(mes: str):
    valid = False

    while not valid:
        try:
            v = int(input(mes))

            if v <= 0:
                print('Please input positive number')
                continue

            return v
        except ValueError:
            print('Please only input digits')
