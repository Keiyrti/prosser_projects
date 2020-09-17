import tkinter as tkin

def list_checker(_list):
    for item in _list:
        if isinstance(item, str):
            try:
                int(item)
                print("int string!")
            except:
                print("string")
        elif isinstance(item, int):
            print("int")
        else:
            print('null')

test_list: list = ['String1', 2, '3', 'String2']

list_checker(test_list)

_health = 100

def test_func():
    print(_health)

_health_changed = tkin.IntVar()
_health_changed.trace("w", test_func)


