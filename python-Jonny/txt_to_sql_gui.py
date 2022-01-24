# 写个GUI
from xml.etree.ElementInclude import default_loader
import PySimpleGUI as sg
from txt_to_sql import txt_to_sql
import os
import json


if not os.path.isfile('txt_to_mysql_config.json'):
    # 设置GUI布局
    layout = [
        [sg.Text('读取指定文件内容，处理后存入指定数据库表中～')],
        [sg.FolderBrowse('点击选取数据所在文件夹', key='filepath', target='file', size=(20, 1)), sg.Text(key='file')],
        [sg.Text('数据表字段名（字段之间请使用空格隔开）'), sg.InputText(key='columns', default_text='xxx xxx xxx', size=(40, 1))],
        [sg.Text('登录用户名'), sg.InputText(key='user', default_text='root', size=(15, 1))],
        [sg.Text('登录密码'), sg.InputText(key='password', default_text='Zjh!1997', size=(15, 1))],
        [sg.Text('主机地址'), sg.InputText(key='host', default_text='localhost', size=(8, 1)), sg.Text('端口号'), sg.InputText(key='port', default_text='3306', size=(8, 1))],
        [sg.Text('数据库名称'), sg.InputText(key='database', default_text='sql_study', size=(8, 1)), sg.Text('存储的表名'), sg.InputText(key='table', default_text='ctd', size=(8, 1))],
        [sg.Button('开始处理'), sg.Button('退出')]
    ]
else:  # 读取配置文件
    with open('txt_to_mysql_config.json', mode='r') as file:
        config_json = json.load(file)
    # 设置GUI布局
    layout = [
        [sg.Text('读取指定文件内容，处理后存入指定数据库表中～')],
        [sg.FolderBrowse('点击选取数据所在文件夹', key='filepath', target='file', size=(20, 1)), sg.Text(config_json['filepath'], key='file')],
        [sg.Text('数据表字段名（字段之间请使用空格隔开）'), sg.InputText(key='columns', default_text=config_json['columns'], size=(40, 1))],
        [sg.Text('登录用户名'), sg.InputText(key='user', default_text=config_json['user'], size=(15, 1))],
        [sg.Text('登录密码'), sg.InputText(key='password', default_text=config_json['password'], size=(15, 1))],
        [sg.Text('主机地址'), sg.InputText(key='host', default_text=config_json['host'], size=(8, 1)), sg.Text('端口号'), sg.InputText(key='port', default_text=config_json['port'], size=(8, 1))],
        [sg.Text('数据库名称'), sg.InputText(key='database', default_text=config_json['database'], size=(8, 1)), sg.Text('存储的表名'), sg.InputText(key='table', default_text=config_json['table'], size=(8, 1))],
        [sg.Button('开始处理'), sg.Button('退出')]
    ]


# 创建窗口程序
window = sg.Window('Txt To MySQL', layout)
while True:
    event, values = window.read()  # 获取数据
    print(values)
    if event=='开始处理':
        # 将输入数据传入数据处理程序
        try:
            if values['filepath']=='':
                values['filepath'] = config_json['filepath']
            txt_to_sql(values['filepath'], values['columns'].split(), values['user'], values['password'], values['host'], values['port'], values['database'], values['table'])
            sg.popup(f'数据已经存储完成啦!!!') 
            # 数据存储成功，将配置写到本地文件，下次读写更方便
            with open('txt_to_mysql_config.json', mode='w') as file:
                json.dump(values, file)

        except Exception as e:
            sg.popup(f'【错误信息】{e}')  
    else:
        # event in (None, '退出'):  # 点击退出 关闭程序
        break
window.close()