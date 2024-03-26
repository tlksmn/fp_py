

# 3 Генератор Функций
# - Создать функцию высшего порядка, которая возвращает другую функцию для
# возведения числа в указанную степень.

def lab_two_high_order_function_fabric(x):
    def fabric_function(y):
        return x ** y;

    return fabric_function;


# print(lab_two_high_order_function_fabric(5)(3));

