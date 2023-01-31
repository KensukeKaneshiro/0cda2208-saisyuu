import PySimpleGUI as sg
import gui
import deepl


def main():    
    window = gui.main_window()
    gui.get_usage(window)

    while True:
        event, values = window.read()
        if event == '-run_deepl-':
            message = values['-original_text-']

            lng = deepl.lang_set(message)

            trans_result = deepl.translate(message, x_lang=lng)

            window['-translated_text-'].print(trans_result)

            window['-mozisuu_text-'].print(str(len(message)))

        if event == sg.WIN_CLOSED or event == "Exit":
            break

    window.close()


if __name__ == '__main__':
    main()