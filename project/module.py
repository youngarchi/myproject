"""
Модуль для обчислення основних елементраних функцій
"""
import numpy as np
import matplotlib.pyplot as plt


type_error_msg_1 = 'Please input int, float, list or ndarray'

def factorial(n=-1):
    """
    додаткова функція - факторіал
    """
    if not isinstance(n, (int, float)):
        return 'Factorial must be integer'
    elif n < 0:
        return 'Factorial cannot be negative or empty'
    else:
        fact = 1
        for num in range(2, int(n) + 1):
            fact *= num
        return fact


def cos(x, graph=True):
    """
    Тригонометрична функція - косинус.
    На вхід подаються значення аргументу функції(Х)- тип данних-
    список([54,2,32,4]) або одне число(10;25;3..)
    На виході отримуємо косинус кожного числа з масиву а також графік косинуса.
    """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1

    def _cos(x2):
        if isinstance(x2, list):
            x2 = np.array(x2)
        elif isinstance(x2, (int, float)):
            x2 = np.array([x2])
        g = (x2 + np.pi) % (np.pi * 2) - np.pi
        result = 0
        positive = 1
        power_internal = 0
        for i in range(10):
            result += (g ** power_internal) / factorial(power_internal) * positive
            positive *= -1
            power_internal += 2
        return result

    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1
    cos_from_x = _cos(x)
    array_of_x_points = np.arange(-np.pi * 2, np.pi * 2, 0.01)
    array_of_y_points = _cos(array_of_x_points)
    fig = plt.figure()
    if graph:
        ax = fig.add_subplot()
        ax.set_title('Cos')
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(array_of_x_points, array_of_y_points)
        plt.show()
    else:
        plt.close(fig)
    return cos_from_x


def sin(x, graph=True):
    """
    Тригонометрична функція - синус.
    На вхід подаються значення аргументу функції(Х)- тип данних-
    список([54,2,32,4]) або одне число(10;25;3..)
    На виході отримуємо синус кожного числа з масиву а також графік синуса.
    """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1

    def _sin(x2):
        if isinstance(x2, list):
            x2 = np.array(x2)
        elif isinstance(x2, (int, float)):
            x2 = np.array([x2])
        g = (x2 + np.pi) % (np.pi * 2) - np.pi
        result = 0
        positive = 1
        power_internal = 1
        for i in range(10):
            result += (g ** power_internal) / factorial(power_internal) * positive
            positive *= -1
            power_internal += 2
        return result
    sin_from_x = _sin(x)
    array_of_x_points = np.arange(-np.pi * 2, np.pi * 2, 0.01)
    array_of_y_points = _sin(array_of_x_points)
    fig = plt.figure()
    if graph:
        ax = fig.add_subplot()
        ax.set_title('Sin')
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(array_of_x_points, array_of_y_points)
        plt.show()
    else:
        plt.close(fig)
    return sin_from_x


def tan(x, graph=True):
    """
    Тригонометрична функція - тангенс.
    На вхід подаються значення аргументу функції(Х)- тип данних-
    список([54,2,32,4]) або одне число(10;25;3..)
    На виході отримуємо тангенс кожного числа з масиву а також графік тангенса.
    """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1

    if isinstance(x,list):
        x = np.array(x)
        x.sort()
    else:
        x = np.array([x])
    tg = sin(x, False) / cos(x, False)
    x1 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    fig = plt.figure()
    if graph:
        ax = fig.add_subplot()
        ax.set_title('tan')
        ax.plot(x1, np.tan(x1))
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(0, 0)
        plt.show()
    else:
        plt.close(fig)
    return np.round(tg, 9)


def cotan(x, graph=True):
    """
    Тригонометрична функція - котангенс.
    На вхід подаються значення аргументу функції(Х)- тип данних-
    список([54,2,32,4]) або одне число(10;25;3..)
    На виході отримуємо котангенс кожного числа з масиву а також
    графік котангенса.
    """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1

    if isinstance(x,list):
        x = np.array(x)
        x.sort()
    else:
        x = np.array([x])

    for i in x:
        if i == 0:
            return 'x cannot be 0'

    ctg = cos(x, False) / sin(x, False)
    x1 = np.linspace(-2 * np.pi+0.0001, 2 * np.pi+0.0001, 1000)
    ctg_plot = cos(x1, False) / sin(x1, False)
    fig = plt.figure()
    if graph:
        ax = fig.add_subplot()
        ax.set_title('cot')
        ax.plot(x1, ctg_plot)
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(1, 1)
        plt.show()
    else:
        plt.close(fig)
    ctg = np.round(ctg, 9)
    return ctg


def linear(k, x, b=0, graph=True):
    """
    Лінійна функція. На вхід подається коефіцієнт k у вигляді одного
    числа (1,2,3..).
    Також значення аргументу функції(Х)- тип данних- список([54,2,32,4])
    або одне число(10;25;3..). Та зсув b у вигляі 1 числа(1,2,3..).
    По стандарту для b задано значення 0.
    На виході отримуємо значення функції для кожного елементу з масиву Х
    також у вигляді масиву.
    Якщо кількість елементів масиву дорівнює 1, то будуємо графік
    відносно аргументів з масиву [-5:5].
    В протилежному випадку креслимо графік відносно точок, які нам задані.
    """
    for i in x, k, b:
        if not isinstance(i, (int, float, list, np.ndarray)):
            return type_error_msg_1

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title('Linear func')

    if isinstance(x, (int, float)):
        x = np.array([x])
    elif isinstance(x, list):
        x = np.array(x)
    elif isinstance(x, np.ndarray):
        pass

    if len(x) == 1:
        x1 = np.arange(-5, 5)
        y1 = k * x1 + b
        y = k * x + b
        ax.plot(x1, y1)
    else:
        x.sort()
        y = k * x + b
        ax.plot(x, y)

    if graph:
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(1, 1)
        plt.show()
    else:
        plt.close(fig)
    return y


def power(x, n, a=1, b=0, c=0, graph=True):
    """
    Квадтратична та степеневі функції. На вхід подаються значення
    аргументу функції(Х)- тип данних- список([54,2,32,4]) або одне
    число (10;25;3..).
    Також степінь n у вигляді одного числа(1,2,3, -1, 1/2, -1/2..).
    Коефіцієнти a,b,c задаються у випадку квадратичної функції.
     Приймають значення одного числа(1,2,3). По стандарту
     a=1, b=0 ,c=0. При n=2 функція виконує роль квадратичної функції.
     У випадку n!=2 функція виконує роль степеневої функції.
     На виході отримуємо значення функції(в залежності від n -
     квадратичної або степеневої) для кожного елементу з масиву Х
     також у вигляді масиву.
     Якщо кількість елементів масиву дорівнює 1, то будуємо графік
     відносно аргументів з масиву [-100:100].
     В протилежному випадку будуємо графік відносно точок, які нам задані.
    """
    for i in x, n, a, b, c:
        if not isinstance(i, (int, float, list, np.ndarray)):
            return type_error_msg_1

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title('Power function')
    if (type(x) == int) or (type(x) == float) or (len(x) == 1):
        x = np.array([x])
        x1 = np.arange(1, 100, dtype=float)
        if n == 2:
            y = a * x * x + b * x + c
            y1 = a * x1 * x1 + b * x1 + c
        else:
            y = x ** n
            y1 = x1 ** n
        ax.plot(x1, y1)
    else:
        x = np.array(x)
        x.sort()
        if n == 2:
            y = a * x * x + b * x + c
        else:
            y = x ** n
        ax.plot(x, y)
    if graph:
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(1, 1)
        plt.show()
    else:
        plt.close(fig)
    return y


def exponential(x, a, graph=True):
    """
    Показникова функція.На вхід подаються значення аргументу
    функції(Х)- тип данних- список([54,2,32,4]) або одне
    число(10;25;3 ..).
    Також степінь a у вигляді одного числа (2,3, 1/2,5/3).
    а!=1 та а>0.
    На виході отримуємо значення функції для кожного елементу
    з масиву Х також у вигляді масиву.
    Якщо кількість елементів масиву дорівнює 1, то будуємо
    графік відносно аргументів з масиву [1, 20].
    В протилежному випадку креслимо графік відносно точок,
    які нам задані.
    """
    for i in x, a:
        if not isinstance(i, (int, float, list, np.ndarray)):
            return type_error_msg_1

    if a == 1 or a <= 0:
        return 'a should be !=1 and >0'
    else:
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set_title('Exponential function')
        if (type(x) == int) or (type(x) == float) or (len(x) == 1):
            x = np.array([x], dtype=np.float32)
            x1 = np.arange(1, 20)
            y1 = a ** x1
            y = a ** x
            ax.plot(x1, y1)
        else:
            x = np.array(x, dtype=np.float32)
            x.sort()
            y = a ** x
            ax.plot(x, y)
        if graph:
            ax.spines.left.set_position('zero')
            ax.spines.right.set_color('none')
            ax.spines.bottom.set_position('zero')
            ax.spines.top.set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.margins(3, 3)
            plt.show()
        else:
            plt.close(fig)
        return y


def ln(x, graph=True):
    """
    Функція натурального логарифму.
    На вхід подаються значення аргументу функції(Х)-
    тип данних- список([54,2,32,4]) або одне число(10;25;3..).
    Данні повинні бути додатними.
    На виході отримуємо значення функції для кожного елементу
    з масиву Х також у вигляді масиву.
    Якщо кількість елементів масиву дорівнює 1, то будуємо графік
    відносно аргументів з масиву [1:100].
    В протилежному випадку креслимо графік відносно точок,
    які нам задані.
    """
    if not isinstance(x, (int, float, list, np.ndarray)):
            return type_error_msg_1

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title('ln function')
    negative_x_error = 'x should be > 0'

    if isinstance(x, (int, float)):
        if x > 0:
            x = np.array([x])
            x1 = np.arange(1, 100, dtype=float)
            y1 = 99999999 * (x1 ** (1 / 99999999) - 1)
            y = 99999999 * (x ** (1 / 99999999) - 1)
            ax.plot(x1, y1)
            return y
        else:
            return negative_x_error

    elif isinstance(x, list):
        if len(x) == 1:
            x = np.array([x])
            x1 = np.arange(1, 100, dtype=float)
            y1 = 99999999 * (x1 ** (1 / 99999999) - 1)
            y = 99999999 * (x ** (1 / 99999999) - 1)
            ax.plot(x1, y1)
            return y
        elif len(x) > 1:
            for i in x:
                if i <= 0:
                    return negative_x_error
            x = np.array(x)
            x.sort()
            y = 99999999 * (x ** (1 / 99999999) - 1)
            ax.plot(x, y)
    if graph:
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(2, 2)
        plt.show()
    else:
        plt.close(fig)
    return y


def log(x, base, graph=True):
    """
    Функція логарифму з основою натурального числа.
    На вхід подаються значення аргументу функції(Х)- тип данних- список([54,2,32,4]) або одне число(10;25;3..). X>0
    Також задається основа логарифму(base) у вигляді натурального числа(2,3..). a>0
    На виході отримуємо значення функції для кожного елементу з масиву Х також у вигляді масиву.
    Якщо кількість елементів масиву дорівнює 1, то будуємо графік відносно аргументів з масиву [1:100].
    В протилежному випадку креслимо графік відносно точок, які нам задані.
    """
    for i in x, base:
        if not isinstance(i, (int, float, list, np.ndarray)):
                return type_error_msg_1

    flag = False
    if base <= 0 or base == 1:
        print('Value error')
        flag = True
    else:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('ln function')
        if (type(x) == int) or (type(x) == float) or (len(x) == 1):
            if x <= 0:
                print("Value Error")
                flag = True
            else:
                x = np.array([x])
                x1 = np.arange(1, 100, dtype=float)
                ln_x1 = 99999999 * (x1 ** (1 / 99999999) - 1)
                ln_x = 99999999 * (x ** (1 / 99999999) - 1)
                ln_base = 99999999 * (base ** (1 / 99999999) - 1)
                y1 = ln_x1 / ln_base
                y = ln_x / ln_base
                ax.plot(x1, y1)
        else:
            for i in x:
                if i <= 0:
                    print('Value Error')
                    flag = True
                    break
            if not flag:
                x = np.array(x)
                x.sort()
                ln_x = 99999999 * (x ** (1 / 99999999) - 1)
                ln_base = 99999999 * (base ** (1 / 99999999) - 1)
                y = ln_x / ln_base
                ax.plot(x, y)
        if not flag:
            if graph:
                ax.spines.left.set_position('zero')
                ax.spines.right.set_color('none')
                ax.spines.bottom.set_position('zero')
                ax.spines.top.set_color('none')
                ax.xaxis.set_ticks_position('bottom')
                ax.yaxis.set_ticks_position('left')
                ax.margins(2, 2)
                plt.show()
            else:
                plt.close(fig)
            return y


def continued_faction_arctan(x):
    x2 = x*x
    d = 10 * 2 + 1
    for k in range(10, 0, -1):
        f = k * 2 - 1
        d = f + k*k*x2/d
    return x / d


def arctan(x, graph=True):
    """
        Функція арктангенса.
        На вхід подаються значення аргументу функції(Х)- тип данних- список([54,2,32,4]) або одне число(10;25;3..). X- будь яке.
        На виході отримуємо значення функції для кожного елементу з масиву Х також у вигляді масиву.
        Якщо кількість елементів масиву дорівнює 1, то графік не будується.
        В протилежному випадку креслимо графік відносно точок, які нам задані.
        """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1
    if isinstance(x,np.ndarray):
        x.sort()
    elif isinstance(x,list):
        x = np.array(x)
        x.sort()
    else:
        x = np.array([x])
    list_res = []
    for i in range(0, len(x)):
        if x[i] >= 2.0:
            y = np.pi / 2.0 - continued_faction_arctan(1/ x[i])
            list_res.append(y)
        else:
            y = continued_faction_arctan( x[i])
            list_res.append(y)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Arctan function')
    if graph:
        ax.plot(x, list_res)
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(1,1)
        plt.show()
    else:
        plt.close(fig)
    print(x)
    list_res = np.array(list_res)
    print(list_res)
    return list_res


def arccot(x, graph=True):
    """
            Функція арккотангенса.
            На вхід подаються значення аргументу функції(Х)- тип данних- список([54,2,32,4]) або одне число(10;25;3..). X- будь яке.
            На виході отримуємо значення функції для кожного елементу з масиву Х також у вигляді масиву.
            Якщо кількість елементів масиву дорівнює 1, то графік не будується.
            В протилежному випадку креслимо графік відносно точок, які нам задані.
            """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1
    if isinstance(x, np.ndarray):
        x.sort()
    elif isinstance(x, list):
        x = np.array(x)
        x.sort()
    else:
        x = np.array([x])
    list_res = []
    for i in range(0,len(x)):
        if x[i] == 0:
            return print('Value Error')
        if x[i] < 0:
            list_res.append(np.pi - continued_faction_arctan(1/np.abs(x[i])))
        elif x[i] > 1.0:
            list_res.append(continued_faction_arctan(1/x[i]))
        else:
            list_res.append(continued_faction_arctan(1/x[i]))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Arccotan function')
    if graph:
        ax.plot(x, list_res)
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(2, 2)
        plt.show()
    else:
        plt.close(fig)
    print(x)
    list_res = np.array(list_res)
    print(list_res)
    return list_res


def arcsin(x, graph=True):

    """
            Функція арксинус.
            На вхід подаються значення аргументу функції(Х)- тип данних- список([54,2,32,4]) або одне число(10;25;3..).
            X<1 i X>-1.
            На виході отримуємо значення функції для кожного елементу з масиву Х також у вигляді масиву.
            Якщо кількість елементів масиву дорівнює 1, то графік не будується.
            В протилежному випадку креслимо графік відносно точок, які нам задані.
            """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1
    if isinstance(x, np.ndarray):
        x.sort()
    elif isinstance(x, list):
        x = np.array(x)
        x.sort()
    else:
        x = np.array([x])
    list_res=[]
    for i in range(0, len(x)):
      if x[i] == 1:
        list_res.append(1.5708)
      elif x[i] == -1:
        list_res.append(-1.5708)
      elif x[i]**2 > 1:
        return print('Value Error')
      else:
        x1 = x[i]/np.sqrt(1 - x[i]**2)
        list_res.append(continued_faction_arctan(x1))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Arcsin function')
    if graph:
        ax.plot(x, list_res)
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(2, 2)
        plt.show()
    else:
        plt.close(fig)
    list_res = np.array(list_res)
    print(list_res)

    return list_res


def arccos(x, graph=False):
    """
                Функція арккосинус.
                На вхід подаються значення аргументу функції(Х)- тип данних- список([54,2,32,4]) або одне число(10;25;3..).
                X<1 i X>-1, Х!=0.
                На виході отримуємо значення функції для кожного елементу з масиву Х також у вигляді масиву.
                Якщо кількість елементів масиву дорівнює 1, то графік не будується.
                В протилежному випадку креслимо графік відносно точок, які нам задані.
                """
    if not isinstance(x, (int, float, list, np.ndarray)):
        return type_error_msg_1
    if isinstance(x, np.ndarray):
        x.sort()
    elif isinstance(x, list):
        x = np.array(x)
        x.sort()
    else:
        x = np.array([x])
    list_res=[]
    for i in range(0,len(x)):
        if x[i] < -1 or x[i] > 1 or x[i] == 0:
            return print('Value Error')
        elif x[i] > 0:
            x1 = np.sqrt(1 - (x[i])**2) / x[i]
            list_res.append(continued_faction_arctan(x1))
        elif x[i] < 0:
            x1 = np.sqrt(1 - (x[i])**2)/(x[i])
            list_res.append(np.pi + continued_faction_arctan(x1))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Arccos function')
    if graph:
        y = np.arccos(x)
        ax.plot(x, y)
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.margins(2, 2)
        plt.show()
    else:
        plt.close(fig)
    list_res = np.array(list_res)
    print(list_res)

    return list_res