from tkinter import BOTH, RAISED
from tkinter.ttk import Frame, Style



class GuiBasic(Frame):
    """
    Базовый класс для окна
    запрос к api и вывод данных в лог

    :param options:
        width: ширина
        height: высота
    """

    options = {
        'width': 500,
        'height': 350,
        'title': 'Program',
        'win_style': 'winnative'
    }

    def __init__(self, parent, options=None, ):
        """
        :param parent: базовый объект Tk
        :param options: параметры вывода
        """
        print('Start init')
        self.parent = parent
        self.base_frame = Frame(parent)
        self.style = Style()
        self.parent = parent
        # self.pack(fill=BOTH, expand=1)
        self.base_frame.pack(fill=BOTH)
        # todo: refactor params and concate
        if options:
            self.options.update(options)
        self.create_window()
        # self.init_ui()

    def create_window(self):
        """
        создание рабочей области
        задаём размеры и положение окна
        """
        print('Creating window')
        self.parent.title(self.options['title'])
        self.style.theme_use(self.options['win_style'])

        w = self.options['width']
        h = self.options['height']
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('{0}x{1}+{2:.0f}+{3:.0f}'.format(w, h, x, y))

        # gui_frame = Frame(relief=RAISED, borderwidth=3)  # добавляем новый фрейм для группирования
        # gui_frame.pack(fill=BOTH, expand=True)
        # self.gui_frame = gui_frame
        return True

    def init_ui(self):
        """
        здесь создаём сам каркас\grid окна
        """
        pass

    def add_button(self):
        pass

    def btn_quit(self):
        """
        завершение работы с выводом сообщения
        """
        print('Program end')
        self.quit()
