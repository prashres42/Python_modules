def ft_count_harvest_recursive() -> None:
    a = int(input('Days until harvest: '))

    def helper_function(days):
        if days <= 0:
            return
        print(f"Day {days}")

        helper_function(days - 1)
    helper_function(a)
    print("Harvest time !")
