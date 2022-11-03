import sys
import math

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0
    s = ''
    if len(args)==1:
        return(items[j].get(args[0]) for j in range(0,len(items)))
    else:
        my_list = list()
        for i in range(0,len(items)):
            s = '{'
            j = 0
            for arg in args:
                if (j == 0):
                    s = s + str(arg) + ': ' + str(items[i].get(arg))
                else:
                    s = s + ', ' + str(arg) + ': ' + str(items[i].get(arg))
                j+=1
            s = s +'}'
            #print(s)
            my_list.append(s)
        return my_list

def main_f():
    l1 = list(field(goods, 'title')) #должен выдавать 'Ковер', 'Диван для отдыха'
    l2 = field(goods, 'title', 'price') #должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
    print(l1)
    print(l2)

if __name__ == "__main__":
    main_f()
