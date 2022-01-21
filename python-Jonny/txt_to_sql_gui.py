# 写个GUI
import PySimpleGUI as sg
layout = [
    [sg.Text('一 句话概括Python')],
    [sg.Input(key='')],
    [sg.Button('确认'), sg.Button('取消')]
]
window = sg.Window('Txt To MySQL', layout)
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event in (None, '取消'):
        break
window.close()