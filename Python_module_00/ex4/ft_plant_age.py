def ft_plant_age() -> None:
    a = input('Enter plant age in days: ')
    b = int(a)
    if b > 60:
        print('Plant is ready to harvest!')
    else:
        print('Plant needs more time to grow.')
