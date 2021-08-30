from typing import Callable


def notebook() -> dict[str, Callable]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    return {
        'add': add_todo,
        'get': get_all
    }


notebook1 = notebook()
notebook1['add']('sleep')
notebook1['add']('eat')
notebook1['add']('work')
notebook1['add']('do sport')
notebook1['add']('play Civ VI')
print(notebook1['get']())

###################################################################

print(list(filter(lambda x: not (x % 15), [45, 55, 60, 16, 15.5, -15])))

###################################################################

def add_num(num: int) -> int:

    value = 0
    for i in range(1, 4):
        value += int(str(num) * i)
    return value


print(add_num(7))