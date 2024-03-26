# 8 Проверка Палиндрома
# - Реализовать рекурсивную функцию для проверки, является ли строка
# палиндромом.

def lab_three_palindromic(string = ""):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return lab_three_palindromic(string[1:-1])
    else:
        return False

a = input()
print(lab_three_palindromic(a))


