import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    
    try:
        coef = float(coef_str)
    except ValueError:
        print("Неверный ввод. Введите повторно")
        while True:
            try:
                print(prompt)
                coef_str = input()
                coef = float(coef_str)
            except ValueError:
                print("Неверный ввод. Введите повторно")
            else: 
                break
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if (len_roots == 0) or (len_roots == 1 and (roots[0] < 0)) or (len_roots == 2 and (roots[0] < 0) and (roots[1] < 0)):
        print('Нет корней')
    elif len_roots == 1:
        if roots[0] == 0:
            print('Один корень: {}'.format(roots[0]))
        else:
            print('Два корня: {} и {}'.format(math.sqrt(roots[0]) * -1, math.sqrt(roots[0])))
    elif len_roots == 2:
        if roots[0] * roots[1] > 0:
            if roots[0] > roots[1]:
                print('Четыре корня: {}, {}, {} и {}'.format(-1 * math.sqrt(roots[0]), -1 * math.sqrt(roots[1]), math.sqrt(roots[1]), math.sqrt(roots[0])))
            else:
                print('Четыре корня:{}, {}, {} и {}'.format(-1 * math.sqrt(roots[1]), -1* math.sqrt(roots[0]), math.sqrt(roots[0]), math.sqrt(roots[1])))
        elif roots[0] * roots[1] < 0:
            if roots[0] > roots[1]:
                print('Два корня: {} и {}'.format(-1 * math.sqrt(roots[0]), math.sqrt(roots[0])))
            else:
                print('Два корня: {} и {}'.format(-1 * math.sqrt(roots[1]), math.sqrt(roots[1])))
        elif roots[0] * roots[1] == 0:
            if roots[0] > roots[1]:
                if roots[0] == 0:
                    print('Один корень: {}'.format(roots[0]))
                else:
                    print('Три корня: {}, {} и {}'.format(-1 * math.sqrt(roots[0]), roots[1], math.sqrt(roots[0])))
            elif roots[1] == 0:
                print('Один корень: {}'.format(roots[1]))
            else:
                print('Три корня: {}, {} и {}'.format(-1 * math.sqrt(roots[1]), roots[0], math.sqrt(roots[1])))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
