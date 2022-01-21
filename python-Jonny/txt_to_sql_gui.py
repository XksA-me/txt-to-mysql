# 写个GUI
import PySimpleGUI as sg
from txt_to_sql import txt_to_sql
import json


# 设置GUI布局
layout = [
    [sg.Text('读取指定文件内容，处理后存入指定数据库表中～')],
    [sg.FileBrowse('点击选取文件', key='filepath', target='file'), sg.Text(key='file')],
    [sg.Text('登录用户名'), sg.InputText(key='user', default_text='root', )],
    [sg.Text('登录密码'), sg.InputText(key='password', default_text='Zjh!1997')],
    [sg.Text('数据库名称'), sg.InputText(key='database', default_text='sql_study')],
    [sg.Text('存储的表名'), sg.InputText(key='table', default_text='ctd')],

    [sg.Button('开始处理'), sg.Button('退出')]
]

# 创建窗口程序
window = sg.Window('Txt To MySQL', layout, default_element_size=(100,))
while True:
    event, values = window.read()  # 获取数据
    # print(event)
    if event=='开始处理':
        # 将输入数据传入数据处理程序
        txt_to_sql(values['filepath'], values['user'], values['password'], values['database'], values['table'])
    else:
        # event in (None, '退出'):  # 点击退出 关闭程序
        break
window.close()