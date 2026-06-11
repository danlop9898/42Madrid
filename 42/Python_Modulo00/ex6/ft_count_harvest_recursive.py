def ft_count_harvest_recursive():
    days = int(input('Days until harvest '))

    def ft_aux(day):
        if day > days:
            print('Harvest time!')
            return
        print('Day ', day)
        ft_aux(day + 1)
    ft_aux(1)
