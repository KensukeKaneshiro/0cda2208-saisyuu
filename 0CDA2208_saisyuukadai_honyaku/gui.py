import PySimpleGUI as sg 
import deepl 

sg.theme('Reddit')

def main_window():
    layout = [
        [sg.Text('原文(日本語、英語)', size=(37, 2), justification='center', background_color='#37B507'),
         sg.Text('翻訳結果', size=(37, 2), justification='center', background_color='#008b8b')], 
        [sg.Multiline('', key='-original_text-', size=(40, 10)),
         sg.Multiline('', key='-translated_text-', size=(40, 10))],
        [sg.Button('実行', size=(10, 1), key='-run_deepl-', pad=(100, 20))],
        [sg.Text('文字数', size=(10,2), justification='center', background_color='#4169e1')],
        [sg.Multiline('', key='-mozisuu_text-', size=(10, 2))],
    ]

    return sg.Window("最終課題　翻訳アプリ", layout, finalize=True)

def get_usage(window):
    count_result = deepl.char_cnt()
    if count_result is None:
        sg.popup('APIキーを確認して下さい')
    else:
        count_used = count_result['character_count']
        count_limit = count_result['character_limit']

        output_txt = str(count_used) + ' / ' + str(count_limit) + '文字'



