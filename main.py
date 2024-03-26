# Бесконечные Арифметические Последовательности
# - Реализовать генератор бесконечной арифметической последовательности с
# использованием ленивых вычислений.

def lab_five_arithmetic_order(step=1, start=0):
    accum = start
    while True:
        yield accum
        accum += step


temp_order = lab_five_arithmetic_order(20, 10)
for i in range(5):
    print(next(temp_order))
