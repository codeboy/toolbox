from tkinter import RIGHT, BOTH, RAISED, Text, W, N, E, S, END
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import scrolledtext
import requests
import json
from PIL import Image, ImageTk
import sys
from .basic import GuiBasic


class Construct(GuiBasic):
    def __init__(self, parent, options=None):
        super().__init__(parent, options)
        self.creation1()

    def creation2(self):
        # frame = self.gui_frame

        # добавляем новый фрейм для группирования
        frame = Frame(
            master=self.base_frame, # указываем родителем базовый фрейм
            relief=RAISED, # стиль рамки FLAT SUNKEN RAISED GROOVE RIDGE
            borderwidth=2 # ширина рамки в пикселях
        )
        frame.pack(fill=BOTH)
        print('111', self.base_frame.winfo_height())
        print('222', frame.winfo_screenmmheight())
        print('333', frame.winfo_height())
        # print(dir(self.parent))

        frame.columnconfigure(0)  # формируем столбцы
        frame.columnconfigure(1)
        frame.rowconfigure(0, minsize=30)  # и строки
        # wdt = self.frame.winfo_screenmmheight() - self.options['height']
        frame.rowconfigure(1, minsize=frame.winfo_screenmmheight())
        frame.rowconfigure(2, minsize=30)

        # for i in dir(frame):
        #     if i.startswith('winfo_'): print(i)

        lbl_title = Label(master=frame, text="Данные")  # текст над выводом
        lbl_title.grid(row=2, column=1)


    def creation1(self):
        frame = Frame(
            master=self.base_frame,  # указываем родителем базовый фрейм
            relief=RAISED,  # стиль рамки FLAT SUNKEN RAISED GROOVE RIDGE
            borderwidth=2  # ширина рамки в пикселях
        )
        frame.pack()
        frame.columnconfigure(1, weight=1) # формируем столбцы
        frame.columnconfigure(3, pad=7)
        frame.rowconfigure(3, weight=1) # и строки
        frame.rowconfigure(5, pad=7)

        lbl = Label(frame, text="Данные")  # текст над выводом
        lbl.grid(sticky=W, pady=4, padx=5)

        # для вывода создаём scrolled поле вместо обычного text
        area = scrolledtext.ScrolledText(frame)
        self.area = area  # передаём в класс созданный объект
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E + W + S + N)

        abtn = Button(frame, text="Тест", command=self.load_image)  # тестируем загрузку картинки
        abtn.grid(row=1, column=3)

        # cbtn = Button(frame, text="Закрыть", command=self.quit)
        # cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(frame, text="Запрос", command=self.btn_request)
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(frame, text="Готово", command=self.btn_quit)
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
        s_url = 'https://some-random-api.ml/facts/cat'
        # s_url = 'http://time.jsontest.com/'
        if not url: url = s_url
        session = requests.Session()
        req = session.get(url)
        stat = req.status_code
        # print(stat)
        # print(req.content)
        data = json.loads(req.content)
        return data

    def prepare_data(self, data):
        # pdata = '{} {}'.format(data['date'], data['time'])
        pdata = data['fact']
        return pdata
