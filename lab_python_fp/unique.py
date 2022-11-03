from lab_python_fp.gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = False, Aбв и АБВ - разные строки
        #           ignore_case = True, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.used_elements = set()
        #self.data = items
        self.iterator = iter(items)
        self.ignore_case = False
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        # Нужно реализовать __next__  
        while True:
            try:
                current = next(self.iterator)
            except StopIteration:
                raise StopIteration
            else: 
                cur_line = str(current)
                if self.ignore_case == True:
                    if cur_line.lower() not in self.used_elements:
                        self.used_elements.add(cur_line.lower())
                        return current
                else:
                    if cur_line not in self.used_elements:
                        self.used_elements.add(cur_line)
                        return current

    def __iter__(self):
        return self


def main_u():
    # будет последовательно возвращать только 1 и 2
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for i in Unique(data):
        print(i, end = " ")
    print()
    # будет последовательно возвращать только 1, 2 и 3
    data = gen_random(10, 1, 3)
    for i in Unique(data):
        print(i, end = " ")
    print()
    # будет последовательно возвращать только a, A, b, B
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data):
        print(i, end = " ")
    print()
    # будет последовательно возвращать только a, b
    for i in Unique(data, ignore_case = True):
        print(i, end = " ")
    print()

if __name__ == "__main__":
    main_u()