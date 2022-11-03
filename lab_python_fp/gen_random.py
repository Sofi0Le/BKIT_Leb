import sys
import random

# Hint: типовая реализация занимает 2 строки
def gen_random(num_count, begin, end):
    #return(random.randint(begin, end) for j in range(0, num_count))
    for i in range(0, num_count):
        yield random.randint(begin, end)


def main_rand():
    l = list(gen_random(5, 1, 3))
    print(l)

if __name__ == "__main__":
    main_rand()
