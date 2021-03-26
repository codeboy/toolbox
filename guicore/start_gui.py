from tkinter import Tk
from .basic import GuiBasic
from .service_gui import Construct

# todo: rename classes and vars
def create_gui(options=None):
    """
     Формирует окно Tk
    :param options: параметры вывода
    :return: экземпляр объекта
    """
    root = Tk()
    base_gui = GuiBasic(root, options)
    service_gui = Construct(root, options)

    return root