# Реактивный Счетчик
# - Разработать реактивный счетчик, который увеличивается или уменьшается в
# ответ на пользовательские события.
import rx.operators
from rx.subject import BehaviorSubject
from colorama import init, Fore, Back

init()
eventSource = BehaviorSubject("+")

sub1 = eventSource.pipe(
    rx.operators.map(lambda operation: 1 if operation == "+" else -1),
    rx.operators.scan(lambda state, new: state + new),
    rx.operators.do_action(lambda value: print(Back.BLUE, Fore.LIGHTBLACK_EX, "Текущее значение", Fore.BLACK, value, Back.RESET, Fore.RESET))
).subscribe()

while True:
    print(Back.LIGHTRED_EX, Fore.WHITE, "Введите",  Fore.RED, Back.WHITE, " + ", Fore.RESET, Back.LIGHTRED_EX, Fore.WHITE, "для увеличение счетчика, либо другой для уменьшения", Back.RESET)
    x = input()
    if x == "exit":
        sub1.dispose()
        print(Back.BLUE, Fore.BLACK, "Выход и отписка", Back.RESET, Fore.RESET)
        break;
    eventSource.on_next(x)

print("Hello real procedure world!")