import numpy as np
import logic
import matplotlib.pyplot as plt


def get_x():
    print('Введите границы через пробел')
    x0, x1 = input().split()
    print('Введите количество точек')
    steps = int(input())
    x = np.linspace(int(x0), int(x1), int(steps))
    y = np.cos(x)
    return get_y(x, y, x0, x1)


def get_y(x, y, x0, x1):
    answer = ''
    for i in y:
        answer = answer + str(i) + ' '
    print('Полученные значения у: ' + answer + '\n Если хотите изменить какое-либо значение, введите 2, иначе 1')
    key = int(input())
    if key == 1:
        plt.scatter(x, y)
        x_new = np.linspace(int(x0), int(x1), 201)
        index = x.searchsorted(x_new)
        plt.plot(x_new, logic.cubic_spline(index, x_new, x, y), color="g")
        x_vals = list(np.cos(x00) for x00 in x_new)
        plt.plot(x_new, x_vals)
        plt.show()
        while 1:
            try:
                print('Чтобы вычислить у для произваольного х из заданного интервала, введите х\n'
                      'Чтобы выйти введите \'e\'')
                x_index = float(input())
                if (x_index >= float(x1)) | (x_index <= float(x0)):
                    print('Число не входит в веденный интервал')
                    continue
                num = logic.cubic_spline(index, x_new, x, y)[np.searchsorted(x_new, [x_index, ], side='right')[0]]
                plt.scatter(x, y)
                plt.plot(x_new, logic.cubic_spline(index, x_new, x, y), color="g")
                plt.plot(x_new, x_vals)
                plt.scatter(x_index, num, color = 'r')
                plt.show()
                print('y(' + str(x_index) + ') = ' + str(num))
            except ValueError:
                print('Завершение работы')
                break
        return 1
    else:
        if key == 2:
            index, value = input('Введите индекс и значение через пробел\n').split()
            y[int(index)] = float(value)
            get_y(x, y, x0, x1)
        else:
            print('Введите 1 или 2')
            get_y(x, y, x0, x1)


get_x()

