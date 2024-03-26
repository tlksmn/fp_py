## ABDIEV SHAKHAN
from functools import reduce


# 4. Форматирование Строк
# - Преобразовать список строк в заглавный регистр, отфильтровать строки длиннее 5
# символов и объединить их в одну строку.

def lab_one_format_string(array=[]):
    upper_cased_array = map(lambda x: x.upper(), array);
    filtered_array_length_more_five = filter(lambda x: len(x) > 5, upper_cased_array);
    return reduce(lambda x, y: x + y, filtered_array_length_more_five);


print(lab_one_format_string(["assssssssssss", "2342342dffvdf", "efjeibgierugieurgiergiuer", "123"]));


