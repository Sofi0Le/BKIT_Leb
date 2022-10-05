from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 8, 8)
    c = Circle("зеленого", 8)
    s = Square("красного", 8)
    print(r)
    print(c)
    print(s)

    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

if __name__ == "__main__":
    main()
