# 2021.1.24  txt to mysql 1.0.1版本  人人可用

![在这里插入图片描述](https://img-blog.csdnimg.cn/88255dc400434ad4803fbaae3c3d721a.png)
```bash
.
├── Pipfile  
├── Pipfile.lock
├── Readme.md  
├── Version  # 打包好的程序
│   ├── txt_to_mysql0.1-mac.zip
│   ├── txt_to_mysql0.1-win.zip
│   ├── txt_to_mysql1.0-mac.zip
│   └── txt_to_mysql1.0-win.7z
├── __pycache__
│   └── txt_to_sql.cpython-310.pyc
├── requirements.txt  # 项目使用到的第三方Python包
├── resources  
│   ├── ctd2020-09-27.txt   # 原测试数据文件，已弃用
│   ├── data1  # 程序测试使用数据文件
│   │   ├── 1.txt
│   │   ├── 2.txt
│   │   └── 3.txt
│   └── mysql  # mysql测试使用 创建数据表、插入基本数据
├── start.bat   # .bat windows 下直接运行程序，需要自己配置环境，修改配置
├── txt_to_mysql1.0.py   # 项目代码1.0.1 整体版本
├── txt_to_mysql_config.json   # 项目自动生成的配置文件
├── txt_to_sql.py   # 项目文件 数据处理部分
└── txt_to_sql_gui.py  # 项目文件 图形化操作界面部分
```



进一步优化项目，更具适用性：
- 支持用户直接加载文件夹，一次处理、存储同一文件夹下所有文件（需要文件格式一致、存入一张表的）
- 支持设置自动保存（用户第一次存储成功后，所有输入的配置就会自动保存到本地文件，下次再打开程序会自动加载之前的配置，无需重复输入）
- 支持用户自定义表头（就是文件的数据字段名称，以空格隔开）
- 自从用户自定义数据库链接主机地址+端口号
- 程序出错后，会有弹框提示错误信息（原始），不会直接退出

下一步改进：
- 常见程序错误信息输出直白化（将原始错误信息翻译成人人能看懂，知道怎么改的信息）
- 支持自定义txt数据文件读取的分割符号（目前支持制表符\t分割的）
- 其他需求，欢迎大家提出。。。尽力开发


# 2021.1.21  txt to mysql 0.1版本  仅测试

下午发现打包的虚拟环境其他人下载后也用不好（里面还是引用了我自己本地的环境），然后就用pyinstaller分别在mac和windows下打包了程序，直接下载对应文件夹即可运行。

![在这里插入图片描述](https://img-blog.csdnimg.cn/6261fd9a387d4f959cdea8e6f6f88784.png)


两个代码文件，去除空格和注释，还有51行代码，嘿嘿～
![](https://img-blog.csdnimg.cn/317b240fd2d64b15baee5c7149c7542f.png)
## 功能
- GUI界面，支持选择指定文件、输入数据库用户名 密码 数据库名称 表名。
![在这里插入图片描述](https://img-blog.csdnimg.cn/45f59e8e3e7b4faf96eefbd493b811b3.png)
- 读取指定文件，数据处理后，存入指定的数据库表中，如果表不存在就直接创建一个新表存储数据；否则直接添加数据到数据表中。

## 使用方法
下载本项目代码：https://github.com/XksA-me/txt-to-mysql

解压后打开文件：`python-Jonny`，本文件内包含了所有python代码+测试数据+环境+windows bat运行文件，其他文件为@ 用Java写的txt to mysql方法和相关配置文件，

原项目地址：https://github.com/schatz0-0/txt-to-mysql
原项目B站视频分享地址：https://www.bilibili.com/video/BV12b4y1J7pD

接续介绍如何使用python版本，首先我们需要解压我提供的python环境包，直接解压即可，无需二次安装。
![在这里插入图片描述](https://img-blog.csdnimg.cn/ac702adda50b4d59a878efac99215fc2.png)
上面截图中相关文件解释：
```bash
├── Pipfile  虚拟环境配置文件（不用管）
├── Pipfile.lock  虚拟环境依赖包关系（不用管）
├── __pycache__  （不用管）
│   └── txt_to_sql.cpython-310.pyc （不用管）
├── python-Jonny-tJ_VXFMA.7z （虚拟环境压缩包，需要直接解压）
├── requirements.txt （本项目需要的第三Python包，都已经安装到给的虚拟环境了）
├── resources  （测试数据）
│   └── ctd2020-09-27.txt
├── start.bat  （windwos下可直接运行文件，启动项目）
├── txt_to_sql.py  （Python代码文件，包含数据读取 处理 存储）
└── txt_to_sql_gui.py  （Python代码文件，包含gui界面，在里面调用txt_to_sql.py文件，所以只用运行本文件即可）
```

虚拟环境解压好后，我们需要根据自己本地目录情况，修改下`start.bat`文件，内容如下：
```bash
@echo off
C:
cd C:\Users\Administrator\Desktop\python-Jonny
C:\Users\Administrator\Desktop\python-Jonny\python-Jonny-tJ_VXFMA\Scripts\python txt_to_sql_gui.py

exit
```
这块不是很懂，现学现卖，上面大概意思就是：进入c盘项目目录下，然后利用虚拟环境python可执行文件 运行我能的代码，最后exit退出程序。

大家需要修改的就是里面涉及到的文件目录，和自己本地一致即可，我是在云服务器上写的就放在c盘（只有一个盘），大家可以选择放到其他盘，方便管理。

修改好后，直接点击`start.bat`即可运行项目，会弹出一个黑框（cmd）,和一个gui程序界面，黑框里会显示程序执行输出的日志（就是程序里的print或者报错信息），gui里我们需要先点击按钮选择存储的文件，然后输入数据库相关信息，设置了默认值，然后点击`开始处理`按钮即可运行程序、存储数据，点击退出按钮关闭程序。
![在这里插入图片描述](https://img-blog.csdnimg.cn/b24b7d605d1e47ecba0f70d415bb79c0.png)
## 可以拓展
- 目前只支持txt，而且数据格式为指定类型（空格或者制表符\t分隔的），有时间，大家有需要，可以拓展支持多种格式文件，加一个文件后缀识别即可

- 界面简陋，上午看到up[@是我_是我_就是我](https://space.bilibili.com/40742726)发的视频，就想到用python写也很简单，界面比较一般，不过工具嘛，最开始能实现功能比较重要。

本项目有很多不足和可以改进的地方，欢迎大家进行学习交流～

