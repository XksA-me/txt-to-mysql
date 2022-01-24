# 导包
import pandas as pd
import time
from sqlalchemy import create_engine
import os

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

# txt_to_sql(filepath='./resources/data1/1.txt', columns=['a', 'b', 'c', 'd'])