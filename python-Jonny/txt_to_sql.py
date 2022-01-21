# 导包
import pandas as pd
import time
from sqlalchemy import create_engine

# 读取文件
def get_txt_data(filepath):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    data = pd.read_csv(filepath, sep=' |\t',header=None,engine='python')
    # 删除数据全nan的列 （如果确实有这种列，后面可以再加上，不影响）
    data.dropna(axis=1, how='all', inplace=True) 
    # 指定列名
    data.columns = columns
    return data

# 数据处理
def process_data(data):
    # 不包含要处理的列，则直接简单去重后、存入数据库
    data.drop_duplicates(inplace=True)
    return data 


# 链接数据库
def link_mysql(user, password, database):
    # create_engine("数据库类型+数据库驱动://数据库用户名:数据库密码@IP地址:端口/数据库"，其他参数)
    engine = create_engine(f'mysql+pymysql://{user}:{password}@localhost:3306/{database}?charset=utf8')
    return engine

# 存储文件
def data_to_sql(data, user='root', password='Zjh!1997', database='sql_study', table='ctd'):
    engine = link_mysql(user, password, database)
    
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
    
# 从数据库读取数据
def read_mysql(user='root', password='Zjh!1997', database='sql_study', table='ctd'):
    engine = link_mysql(user, password, database)
    # 读取的sql语句
    sql = f'select * from {table} limit 3'
    # 第一个参数：查询sql语句
    # 第二个参数：engine，数据库连接引擎
    pd_read_sql = pd.read_sql(sql, engine)
    return pd_read_sql

# 文本文件存储到mysql
def txt_to_sql(filepath, user='root', password='Zjh!1997', database='sql_study', table='ctd'):
    # 读取文件
    data = get_txt_data(filepath)
    # 数据处理
    data = process_data(data)
    # 数据存储
    data_to_sql(data, user, password, database, table)
