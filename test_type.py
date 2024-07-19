from math import sqrt
from typing import Optional


def add_numbers(x_num: int, y_num: int) -> int:
    return x_num + y_num


def calculate_square_root(Number_X: float) -> float:
    return sqrt(Number_X)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None
    mez_val = calculate_square_root(your_number + 1)
    print(mez_val)
    return calculate_square_root(your_number)


x_num_main = 10
y_num_main = 5

print('Сумма чисел: ', add_numbers(x_num_main, y_num_main))

calc_rez: Optional[str] = calc(25.5)
print('Мы вычислили квадратный корень из введённого вами числа.' 
      f'Это будет: {calc_rez}')