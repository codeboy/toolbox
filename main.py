from toolbox.guicore.start_gui import create_gui


def main():
    options = {
        'width': 700,
        'height': 450,
        'title': 'Testing'
    }

    # можностаровать пустое окно
    # exec = GuiBasic(root, options)

    # или базовый запуск
    exec = create_gui(options)

    # выполнение базового лупа
    exec.mainloop()

if __name__ == '__main__':
    main()
