# 导包
import pandas as pd
import time
from sqlalchemy import create_engine
import os
import PySimpleGUI as sg
import json

# 读取文件
def get_txt_data(filepath, columns):
    files = os.listdir(filepath)
    files = [i for i in files if 'txt' in i]  # 筛选出txt文件
    df_all = []
    for file in files:
        # columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        data = pd.read_csv(filepath+'/'+file, sep='\t', header=None, engine='python')
        # 删除数据全nan的列 （如果确实有这种列，后面可以再加上，不影响）
        data.dropna(axis=1, how='all', inplace=True) 
        # 指定列名
        data.columns = columns
        df_all.append(data)
    result = pd.concat(df_all)
    return result

# 数据处理
def process_data(data):
    # 不包含要处理的列，则直接简单去重后、存入数据库
    data.drop_duplicates(inplace=True)
    return data 


# 链接数据库
def link_mysql(user, password, host, port, database):
    # create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口/数据库"，其他参数)
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8')
    return engine

# 存储文件
def data_to_sql(data, user='root', password='Zjh!1997', host='localhost', port='3306', database='sql_study', table='ctd'):
    engine = link_mysql(user, password, host, port, database)
    
    # 调用pandas 的 to_sql 存储数据
    t1 = time.time()  # 时间戳 单位秒
    print('数据插入开始时间：{0}'.format(t1))
    # 第一个参数：表名
    # 第二个参数：数据库连接引擎
    # 第三个参数：是否存储索引
    # 第四个参数：如果表存在 就追加数据
    data.to_sql(table, engine, index=False, if_exists='append')
    t2 = time.time()  # 时间戳 单位秒
    print('数据插入结束时间：{0}'.format(t2))
    print('成功插入数据%d条，'%len(data), '耗费时间：%.5f秒。'%(t2-t1))

# 文本文件存储到mysql
def txt_to_sql(filepath, columns, user='root', password='Zjh!1997', host='localhost', port='3306', database='sql_study', table='ctd'):
    # 读取文件
    data = get_txt_data(filepath, columns)
    # 数据处理
    data = process_data(data)
    # 数据存储
    data_to_sql(data, user, password, host, port, database, table)


'''
图形可视化操作界面 GUI
'''
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