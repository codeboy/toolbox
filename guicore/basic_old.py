from tkinter import RIGHT, BOTH, RAISED, Text, W, N, E, S, END
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import scrolledtext
import requests
import json
from PIL import Image, ImageTk
import sys


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
        'height': 350
    }

    def __init__(self, parent, options=None, ):
        """
        :param parent: базовый объект Tk
        :param options: параметры вывода
        """
        print('Start init')
        # self.url = 'https://some-random-api.ml/facts/cat'
        self.url = 'http://time.jsontest.com/'
        Frame.__init__(self, parent)
        self.style = Style()
        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        # todo: refactor
        if options:
            self.options.update(options)
        self.create_window()
        self.init_ui()

    def create_window(self):
        """
        создание рабочей области
        задаём размеры и положение окна
        """
        print('Creating window')
        self.parent.title("Flowers")
        self.style.theme_use("winnative")

        w = self.options['width']
        h = self.options['height']
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def init_ui(self):
        """
        здесь создаём сам каркас\grid окна
        """
        frame = Frame(self, relief=RAISED, borderwidth=1) # добавляем новый фрейм для группирования
        frame.pack(fill=BOTH, expand=True)

        frame.columnconfigure(1, weight=1) # формируем столбцы
        frame.columnconfigure(3, pad=7)
        frame.rowconfigure(3, weight=1) # и строки
        frame.rowconfigure(5, pad=7)

        lbl = Label(frame, text="Данные") # текст над выводом
        lbl.grid(sticky=W, pady=4, padx=5)

        # для вывода создаём scrolled поле вместо обычного text
        area = scrolledtext.ScrolledText(frame)
        self.area = area # передаём в класс созданный объект
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E + W + S + N)

        abtn = Button(frame, text="Тест", command=self.load_image) # тестируем загрузку картинки
        abtn.grid(row=1, column=3)

        # cbtn = Button(frame, text="Закрыть", command=self.quit)
        # cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(frame, text="Запрос", command=self.btn_request)
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(frame, text="Готово", command=self.quit)
        obtn.grid(row=5, column=3)

    def add_button(self):
        pass

    def btn_request(self):
        data = self.prepare_data(self.make_request())
        self.msg_print(self.area, data)

    def load_image(self):
        """
        просто тест работы экстренного выхода
        """
        try:
            self.img = Image.open("tatras.jpg")
        except IOError:
            print("Возникла ошибка во время открытия изображения!")
            sys.exit(1)

    def msg_print(self, txt_container, msg):
        """
        Вывод сообщения в поле
        :param txt_container: объект поля для вывода
        :param msg: текст сообщения
        """
        if txt_container['state'] != 'normal': # это нужно для включения поля на запись
            txt_container.configure(state='normal')
        txt_container.insert(END, '{0}\r\n'.format(msg)) # вставляем в конец и добавляем перевод строки
        txt_container.configure(state='disabled') # отключаем для предотвращения редактирования
        txt_container.yview(END) # пролистываем вниз за кареткой

    def make_request(self, url=None):
        """
        запрос к внешнему api
        :return: обработаный вывод
        """
        if not url: url = self.url
        session = requests.Session()
        req = session.get(url)
        stat = req.status_code
        # print(stat)
        # print(req.content)
        data = json.loads(req.content)
        return data

    def prepare_data(self, data):
        pdata = '{} {}'.format(data['date'], data['time'])
        # return data['fact']
        return pdata
